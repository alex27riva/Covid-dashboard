#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 13
Title: Home isolation
Description: This chart shows a bar chart with total ICU patients and 7 day moving average in Italy
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = 'Home isolation'

# column names
x_name = 'data'
y_name = 'isolamento_domiciliare'

df = pd.read_csv(url, usecols=[x_name, y_name])
df = df[101:]

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Home Isolation',
           marker_color='SlateGray')

)

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.show()
