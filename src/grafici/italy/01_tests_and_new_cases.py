#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
Chart n°: 1
Title: Covid-19 Swab Tests and New Cases in Italy
Description: This chart shows a bar chart with daily deaths and a scatter line with new daily cases in Italy
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = 'Covid-19 Swab Tests and New Cases in Italy'

# column names
x_name = 'data'

df = pd.read_csv(url, usecols=[x_name, 'tamponi', 'nuovi_positivi'])
df['incr_tamponi'] = df.tamponi.diff().fillna(df.tamponi)
df['cases_tests_ratio'] = (df['nuovi_positivi'] / df['incr_tamponi']) * 100

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df[x_name], y=df['nuovi_positivi'],
           name='New Cases',
           marker_color='blue'),
    secondary_y=False
)

fig.add_trace(
    go.Bar(x=df[x_name], y=df['incr_tamponi'],
           name='Tests',
           marker_color='orange'),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df['cases_tests_ratio'],
               name='% Cases/Tests',
               line=dict(color='SlateGray')),
    secondary_y=True
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")

fig.update_yaxes(title_text="%",
                 secondary_y=True,
                 rangemode='tozero')

fig.show()
