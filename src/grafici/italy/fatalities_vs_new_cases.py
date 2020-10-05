#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Daily Fatality vs. New Cases
"""

dataset = '../../../dataset/italy.csv'

# column names
x_name = 'date'
y_name = 'daily_deaths'
y_secondary_name = 'new_daily_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name, y_secondary_name])

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Daily fatalities')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_secondary_name],
               name='New daily cases',
               line=dict(color='blue'))
)
# Add title
fig.update_layout(
    title_text="Daily Fatality vs. New Cases"
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
