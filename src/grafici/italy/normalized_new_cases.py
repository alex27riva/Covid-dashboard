#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 7
Title: Normalizzed new daily cases in Italy
Description: This chart shows a bar chart and 7 day average of normalized new cases in Italy
"""
# todo: remove italy.csv

dataset = '../../../dataset/italy.csv'
# chart title
chart_title = "Normalized new daily cases in Italy (+ 7 day avg)"

# column names
x_name = 'date'
y_name = 'delta_cases_norm'
y_moving_7gg = 'delta_cases_average'

df = pd.read_csv(dataset, usecols=[x_name, y_name])
df = df[77:]
# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='New cases')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='7 day average')
)

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
