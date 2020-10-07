#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
Chart n°: 1
Title: Covid-19 Swab Tests and New Cases in Italy
Description: This chart shows a bar chart with daily deaths and a scatter line with new daily cases in Italy
"""
dataset = '../../../dataset/italy_us.csv'

# chart title
chart_title = 'Covid-19 Swab Tests and New Cases in Italy'

# column names
x_name = 'date'
y_name = 'new_daily_cases'
y_name_2 = 'delta_swabs'
y_secondary_name = 'swabs_and_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name, y_name_2, y_secondary_name])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_name],
           name='New Cases',
           marker_color='blue'),
    secondary_y=False
)

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_name_2],
           name='Tests',
           marker_color='orange'),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_secondary_name],
               name='% Cases/Tests',
               line=dict(color='SlateGray')),
    secondary_y=True
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.update_yaxes(title_text="%", secondary_y=True)

fig.show()
