#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
Title: Daily Fatality vs. New Cases
Description: This chart shows a bar chart with daily deaths and a scatter line with new daily cases in Italy
"""
dataset = '../../../dataset/italy.csv'

# chart title
chart_title = "Daily Fatality vs. New Cases"

# column names
x_name = 'date'
y_name = 'daily_deaths'
y_secondary_name = 'new_daily_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name, y_secondary_name])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Daily deaths',
           marker_color='orange'),
    secondary_y=True
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_secondary_name],
               name='New daily cases',
               line=dict(color='blue'),
               fill='tozeroy')
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()
