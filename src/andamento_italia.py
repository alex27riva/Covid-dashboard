#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

url_andamento_nazionale = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'

df = pd.read_csv(url_andamento_nazionale, index_col=[], usecols=['data', 'totale_positivi', 'nuovi_positivi'])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df['data'], y=df['nuovi_positivi'],
           name='nuovi positivi'),
    secondary_y=True)

fig.add_trace(
    go.Scatter(x=df['data'],
               y=df['totale_positivi'],
               name='totale positivi'),
    secondary_y=False,
)
# Add title
fig.update_layout(
    title_text="Andamento dei contagi Italia",
    barmode='stack',
    autosize=True
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi totali", secondary_y=False)
fig.update_yaxes(title_text="Contagi giornalieri", secondary_y=True)

fig.show()
