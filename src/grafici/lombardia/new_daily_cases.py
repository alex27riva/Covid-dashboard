#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Andamento dei contagi in Lombardia
Description: This chart shows new cases and 7 day moving average in Lombardia
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'

# chart title
chart_title = "Andamento dei contagi Lombardia"

# column names
x_name = 'data'
y_name = 'nuovi_positivi'
y_moving_7gg = 'nuovi_positivi_avg'

df = pd.read_csv(url, usecols=[x_name, y_name, 'denominazione_regione'])
df = df.loc[df['denominazione_regione'] == 'Lombardia']
# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure()

fig.add_trace(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Nuovi casi')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='Media 7 giorni')
)
# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi giornalieri")

fig.show()
