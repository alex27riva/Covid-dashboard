#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/lombardia.csv'

df = pd.read_csv(dataset, index_col=[], usecols=['data', 'ew_cases_normalized'])
df = df[136:]
fig = go.Figure(
    go.Bar(x=df['data'], y=df['ew_cases_normalized'],
           name='nuovi positivi')
)
# Add title
fig.update_layout(
    title_text="Normalized new daily cases RL"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Normalized dayly cases")

fig.show()
