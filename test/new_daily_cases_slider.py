#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
"""
Title: Slider test
Description: This is a test for the date range slider selector
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'

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
    title_text="Andamento dei contagi Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi giornalieri")

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=3,
                     label="3m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1a",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()
