#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 4
Title: Hospitalized daily (with symptoms and ICU)
Description: This chart shows a bar chart with daily total hospitalized patients in Italy
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Hospitalized daily (with symptoms and ICU)"

# column names
x_name = 'data'
y_name = 'delta_hospitalized'

df = pd.read_csv(url, usecols=[x_name, 'totale_ospedalizzati'])
# df = df[136:]
df[y_name] = df.totale_ospedalizzati.diff().shift(-1)

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='New cases')
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(
    title_text='Days',
    dtick="M1"
)

fig.show()
