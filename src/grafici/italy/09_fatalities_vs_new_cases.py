#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
Chart n°: 9
Title: Daily Fatality vs. New Cases
Description: This chart shows a bar chart with daily deaths and a scatter line with new daily cases in Italy
"""
# todo: fix y axis misalignment
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Daily Fatality vs. New Cases"

# column names
x_name = 'data'
y_name = 'nuovi_positivi'

df = pd.read_csv(url, usecols=[x_name, 'deceduti', y_name])
df['daily_deaths'] = df.deceduti.diff().fillna(df.deceduti)

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df[x_name], y=df['daily_deaths'],
           name='Daily deaths',
           marker_color='orange'),
    secondary_y=True
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_name],
               name='New daily cases',
               line=dict(color='blue')),
    secondary_y=False,
)  # fill='tozeroy',

# Add title
fig.update_layout(
    title_text=chart_title
)

# set x axis name
fig.update_xaxes(title_text="Days")

fig.update_yaxes(rangemode='tozeroy')

fig.show()
