#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Chart n°: 5
Title: Daily Recoveries vs fatalities
Description: This chart shows two bar charts with dead and recoveries and their moving averages.
"""
dataset = '../../../dataset/italy.csv'
days = 5

# chart title
chart_title = 'Daily Recoveries vs fatalities'

# column names
x_name = 'date'
y_deaths = 'daily_deaths'
y_recoveries = 'daily_recoveries'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_deaths, y_recoveries])
# calculate rolling average
df['deaths_rolling'] = df[y_deaths].rolling(days).mean()
df['recoveries_rolling'] = df[y_recoveries].rolling(days).mean()

fig = go.Figure()

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_deaths],
           name='Daily Fatalities',
           marker_color='blue')
)

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_recoveries],
           name='Daily Recoveries',
           marker_color='orange')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df['deaths_rolling'],
               name='Moving avg (Daily Fatalities',
               line=dict(color='blue', dash='dot')
               ))

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df['recoveries_rolling'],
               name='Moving avg (Daily Recoveries',
               line=dict(color='orange', dash='dot')
               ))
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()
