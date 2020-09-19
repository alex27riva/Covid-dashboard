#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

url_andamento_nazionale = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'

df = pd.read_csv(url_andamento_nazionale, index_col=[], usecols=['data', 'totale_positivi', 'nuovi_positivi'])

graph_data = [
    go.Bar(
        x=df['data'],
        y=df['nuovi_positivi']
    ),
    go.Scatter(
        x=df['data'],
        y=df['totale_positivi']
    )

]

layout = go.Layout(
    barmode='stack',
    title='Stacked Bar with Pandas'
)

fig = go.Figure(data=graph_data, layout=layout)

fig.show()
