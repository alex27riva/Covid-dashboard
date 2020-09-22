#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/lombardia.csv'

# column names
x_name = 'data'
y_name = 'new_cases_normalized'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])
# trim lines (missing data)
df = df[136:]

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='New cases')
)
# Add title
fig.update_layout(
    title_text="Normalized new daily cases RL"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
