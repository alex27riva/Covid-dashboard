#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""
Chart n°: 10
Title: 7 day average: daily deaths vs daily cases
Description: This chart shows new cases and daily deaths with respective 7 day moving average
"""
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = "7 day average: daily deaths vs daily cases"

# column names
x_name = 'data'
y_new_cases = 'nuovi_positivi'

# moving average
new_cases_rolling = 'new_cases_rolling'
new_deaths_rolling = 'new_deaths_rolling'

df = pd.read_csv(url, usecols=[x_name, y_new_cases, 'deceduti'])
# df = df[105:]
df['daily_deaths'] = df.deceduti.diff().fillna(df.deceduti)

# calculate rolling average 7gg
df[new_cases_rolling] = df[y_new_cases].rolling(7).mean()
df[new_deaths_rolling] = df['daily_deaths'].rolling(7).mean()

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=df[x_name], y=df[new_cases_rolling],
               name='New daily cases (7 day average)',
               line=dict(color='orange'))
)

fig.add_trace(
    go.Scatter(x=df[x_name], y=df[new_deaths_rolling],
               name='Daily deaths (7 day average)',
               line=dict(color='blue')),
    secondary_y=True
)

fig.add_trace(go.Scatter(x=df[x_name], y=df[y_new_cases], name='New cases',
                         line=dict(color='orange', dash='dot')))

fig.add_trace(go.Scatter(x=df[x_name], y=df['daily_deaths'], name='New deaths',
                         line=dict(color='blue', dash='dot')),
              secondary_y=True)

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text='Days')
# set y axis title
fig.update_yaxes(title_text="Cases", secondary_y=False)
fig.update_yaxes(title_text="Deaths", secondary_y=True)

fig.show()
