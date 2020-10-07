#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Chart n°: 3
Title: Total cases
Description: This chart shows a bar chart with total cases in Italy
"""
dataset = '../../../dataset/italy.csv'

# chart title
chart_title = "Total Cases"

# column names
x_name = 'date'
y_name = 'total_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Total cases',
           marker_color='OrangeRed')
)


# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()