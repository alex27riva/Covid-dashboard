#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Fatality Rate percentage
Description: This chart shows a scatter chart of fatality rate percentage in Italy
"""

dataset = '../../../dataset/italy_us.csv'

# chart title
chart_title = "Fatality Rate (%) COVID-19 ITA"

# column names
x_name = 'date'
y_name = 'death_index'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])

fig = go.Figure(
    go.Scatter(x=df[x_name],
               y=df[y_name],
               name='Fatality rate',
               line=dict(color='blue'))
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
