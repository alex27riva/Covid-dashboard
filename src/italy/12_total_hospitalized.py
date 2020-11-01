#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 12
Title: ICU + severe disease
Description: This chart shows a bar chart of total hospitalized patients and 7 day moving average in Italy
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "ICU + severe disease"

# column names
x_name = 'data'
y_name = 'totale_ospedalizzati'
y_moving_7gg = '7_day_moving_average'

df = pd.read_csv(url, usecols=[x_name, y_name])
df = df[120:]

# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Total hospitalized',
           marker_color='grey')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='7 day average',
               line=dict(color='red',
                         dash='dot'))
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()