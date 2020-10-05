#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Daily Fatality vs. New Cases
Description: This chart shows a bar chart with daily deaths and a scatter line with new daily cases in Italy
"""
# TODO: add secondary scale and fill Scatter
dataset = '../../../dataset/italy.csv'

# chart title
chart_title = "Daily Fatality vs. New Cases"

# column names
x_name = 'date'
y_name = 'daily_deaths'
y_secondary_name = 'new_daily_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name, y_secondary_name])

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Daily deaths')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_secondary_name],
               name='New daily cases',
               line=dict(color='orange'))
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
