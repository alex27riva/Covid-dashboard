#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Chart n°: 7
Title: Normalizzed new daily cases in Italy
Description: This chart shows a bar chart and 7 day average of normalized new cases in Italy
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "Normalized new daily cases in Italy (+ 7 day avg)"

MIN_DELTA_TAMP = 964  # =MIN(Q$7:Q$119)    Q = delta_tamp
REF_TAMP = 48000  # reference value

# column names
x_name = 'data'
y_moving_7gg = 'delta_cases_average'

df = pd.read_csv(url, usecols=[x_name, 'tamponi', 'nuovi_positivi'])
df = df[77:]
df['delta_tamponi'] = df.tamponi.diff().fillna(df.tamponi)
df['tamp_norm'] = MIN_DELTA_TAMP / df['delta_tamponi'] * df['nuovi_positivi']
df['nuovi_casi_norm'] = df['nuovi_positivi'] * REF_TAMP / df['delta_tamponi']

# rolling average 7gg
df[y_moving_7gg] = df['nuovi_casi_norm'].rolling(7).mean()

fig = go.Figure(
    go.Bar(x=df[x_name], y=df['nuovi_casi_norm'].astype(int),  # convert to int
           name='New cases')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='7 day average')
)

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
