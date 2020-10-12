#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 5
Title: Daily Recoveries vs fatalities
Description: This chart shows two bar charts with dead and recoveries and their moving averages.
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

days = 5

# chart title
chart_title = 'Daily Recoveries vs fatalities'

# column names
x_name = 'data'

df = pd.read_csv(url, usecols=[x_name, 'deceduti', 'dimessi_guariti'])
# calculate delta
df['daily_deaths'] = df.deceduti.diff().fillna(df.deceduti)
df['daily_recoveries'] = df.dimessi_guariti.diff().fillna(df.dimessi_guariti)
# calculate rolling average
df['deaths_rolling'] = df['daily_deaths'].rolling(days).mean()
df['recoveries_rolling'] = df['daily_recoveries'].rolling(days).mean()

fig = go.Figure()

fig.add_trace(
    go.Bar(x=df[x_name], y=df['daily_deaths'],
           name='Daily Fatalities',
           marker_color='blue')
)

fig.add_trace(
    go.Bar(x=df[x_name], y=df['daily_recoveries'],
           name='Daily Recoveries',
           marker_color='orange')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df['deaths_rolling'],
               name='Daily Fatalities ({} day avg)'.format(days),
               line=dict(color='blue', dash='dot')
               ))

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df['recoveries_rolling'],
               name='Daily Recoveries ({} day avg)'.format(days),
               line=dict(color='orange', dash='dot')
               ))
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()
