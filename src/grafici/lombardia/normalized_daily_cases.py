#!/usr/bin/python3
from datetime import date

import pandas as pd
import plotly.graph_objects as go

"""
Title: Normalizzed new daily cases in Regione Lombardia
Description: This chart shows a bar chart of normalized new cases in Lombardia
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
REF_TAMP = 9000  # reference value
today = date.today()

# chart title
chart_title = "Normalized new daily cases in Regione Lombardia"

df = pd.read_csv(url)
df = df.loc[df['denominazione_regione'] == 'Lombardia']

# df = df[136:]

# calculate
df['incr_tamponi'] = df.tamponi.diff().fillna(df.tamponi)
df['nuovi_casi_norm'] = df['nuovi_positivi'] * REF_TAMP / df['incr_tamponi']

fig = go.Figure(
    go.Bar(x=df['data'], y=df['nuovi_casi_norm'],
           name='New cases normalized')
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Giorni",
                 type='date',
                 range=['2020-07-02', today])
# set y axis title
fig.update_yaxes(title_text="Normalized daily cases",
                 range=[80, 3000])

fig.show()
