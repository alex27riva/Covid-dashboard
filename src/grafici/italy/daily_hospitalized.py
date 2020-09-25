#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/italy.csv'

# column names
x_name = 'date'
y_name = 'delta_hospitalized'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])
# trim lines (missing data)
# df = df[136:]

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='New cases')
)
# Add title
fig.update_layout(
    title_text="Hospitalized daily (with symptoms and ICU)"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
