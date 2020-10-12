#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Chart n°: 8
Title: Ratio (%) New Positives / cases tested by swabs
Description: This chart shows new cases and daily deaths with respective 7 day moving average
"""
# todo: check if axis are correct

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'
# chart title
chart_title = 'Ratio (%) New Positives / cases tested by swabs'

# column names
x_name = 'data'

df = pd.read_csv(url, index_col=[], usecols=[x_name, 'casi_testati', 'nuovi_positivi', 'tamponi'])
df = df[59:]  # trim data
df['delta_casi_testati'] = df.casi_testati.diff().shift(-1)  # U
df['tamponi_meno_casi_testati'] = df['tamponi'] - df['casi_testati']  # S
df['delta_tamponi_casi'] = df.tamponi_meno_casi_testati.diff().shift(-1)  # T
# y axis
df['ratio_cases_tests'] = (df['nuovi_positivi'] / df['delta_casi_testati']) * 100
df['perc_tamponi_meno_testati'] = (df['nuovi_positivi'] / df['tamponi_meno_casi_testati']) * 100

# calculate rolling average 7gg
df['rolling_tested'] = df['ratio_cases_tests'].rolling(7).mean()
df['rolling_swabs_tested'] = df['perc_tamponi_meno_testati'].rolling(7).mean()

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df[x_name], y=df['rolling_tested'],
               name='Moving avg (% tested cases)',
               line=dict(color='blue'))
)

fig.add_trace(
    go.Scatter(x=df[x_name], y=df['rolling_swabs_tested'],
               name='Moving avg (% total swabs - total cases)',
               line=dict(color='orange'))
)

fig.add_trace(go.Scatter(x=df[x_name], y=df['ratio_cases_tests'], name='% tested cases',
                         line=dict(color='blue', dash='dot')))

fig.add_trace(go.Scatter(x=df[x_name], y=df['perc_tamponi_meno_testati'], name='% Total Swabs - tested cases',
                         line=dict(color='orange', dash='dot')))

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text='Days')
# set y axis title
fig.update_yaxes(title_text="%")

fig.show()
