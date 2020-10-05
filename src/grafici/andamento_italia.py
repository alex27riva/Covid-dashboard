#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
"""
Title: Andamento dei contagi in Italia
Description: This chart show Italy new cases trend
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Andamento dei contagi Italia"

df = pd.read_csv(url, index_col=[], usecols=['data', 'totale_positivi', 'nuovi_positivi'])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df['data'], y=df['nuovi_positivi'],
           name='Nuovi positivi'),
    secondary_y=True)

fig.add_trace(
    go.Scatter(x=df['data'],
               y=df['totale_positivi'],
               name='Totale positivi'),
    secondary_y=False,
)
# Add title
fig.update_layout(
    title_text=chart_title,
    barmode='stack',
    autosize=True
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi totali", secondary_y=False)
fig.update_yaxes(title_text="Contagi giornalieri", secondary_y=True)

fig.show()
