#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Title: % New Cases / Swab Tests in Regione Lombardia
Description: This chart shows the percentahe of new cases and total cases in Lombardia
"""

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
# chart title
chart_title = "% New Cases / Swab Tests in Regione Lombardia"

# column names
x_name = 'data'
y_total_cases = 'positive_swabs_percentage'

df = pd.read_csv(url)

df = df.loc[df['denominazione_regione'] == 'Lombardia']
# df = df[65:]
# calculation
df['delta_casi_testati'] = df.casi_testati.diff().fillna(df.casi_testati)
df['incr_tamponi'] = df.tamponi.diff().fillna(df.tamponi)
df['perc_positivi_tamponi'] = (df['nuovi_positivi'] / df['incr_tamponi']) * 100  # AB
df['perc_positivi_test'] = (df['nuovi_positivi'] / df['delta_casi_testati']) * 100  # AD

# calculate rolling average 3gg
df['perc_positivi_tamponi_avg'] = df['perc_positivi_tamponi'].rolling(3).mean()
df['perc_positivi_test_avg'] = df['perc_positivi_test'].rolling(3).mean()

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df[x_name], y=df['perc_positivi_test'],  # AD
               name='New cases tested',
               line=dict(color='orange'))
)

fig.add_trace(
    go.Scatter(x=df[x_name], y=df['perc_positivi_tamponi'],  # AB
               name='Total cases tested',
               line=dict(color='blue'))
)

fig.add_trace(go.Scatter(x=df[x_name], y=df['perc_positivi_test_avg'], name='New cases (3 day average)',
                         line=dict(color='orange', dash='dot')))

fig.add_trace(go.Scatter(x=df[x_name], y=df['perc_positivi_test_avg'], name='Total cases (3 day average)',
                         line=dict(color='blue', dash='dot')))

# Add title
fig.update_layout(
    title_text=chart_title,
    xaxis_range=['2020-04-22', '2020-10-15']
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Percentage %")

fig.show()
