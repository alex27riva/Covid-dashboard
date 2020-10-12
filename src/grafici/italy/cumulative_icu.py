#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 11
Title: ICU Cumulative
Description: This chart shows a bar chart with total ICU patients and 7 day moving average in Italy
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "ICU Cumulative"

# column names
x_name = 'data'
y_name = 'terapia_intensiva'
y_moving_7gg = '7_day_moving_average'

df = pd.read_csv(url, index_col=[], usecols=[x_name, y_name])
df = df[101:]

# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='ICU patients',
           marker_color='orange')

)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='7 day average',
               line=dict(color='blue',
                         dash='dot'))
)
fig.update_layout(
    title_text=chart_title
)
fig.update_xaxes(
    title_text="Days",
    dtick="M1",
    tickformat="%b\n%Y")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
