#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Chart n°: 3
Title: Total cases
Description: This chart shows a bar chart with total cases in Italy
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Total Cases"

# column names
x_name = 'data'
y_name = 'totale_casi'

df = pd.read_csv(url, usecols=[x_name, y_name])

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Total cases',
           marker_color='orange')
)

# Add title
fig.update_layout(
    title_text=chart_title
)
# change y date tick
fig.update_xaxes(
    dtick="M1"
)

# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()
