#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 6
Title: Fatality Rate percentage
Description: This chart shows a scatter chart of fatality rate percentage in Italy
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Fatality Rate (%) COVID-19 ITA"

# column names
x_name = 'data'
y_name = 'deaths_perc'

df = pd.read_csv(url, usecols=[x_name, 'totale_casi', 'deceduti'])
df[y_name] = df['deceduti'] / df['totale_casi']

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

fig.show()
