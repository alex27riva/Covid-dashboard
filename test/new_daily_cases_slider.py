#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Slider test
Description: This is a test for the date range slider selector
"""

dataset = '../dataset/lombardia_us_date.csv'

# column names
x_name = 'data'
y_name = 'delta_cases'
y_moving_7gg = 'new_cases_average'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])
# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure()

fig.add_trace(
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
    title_text="Andamento dei contagi Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi totali")
fig.update_yaxes(title_text="Contagi giornalieri")

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=3,
                     label="3m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()
