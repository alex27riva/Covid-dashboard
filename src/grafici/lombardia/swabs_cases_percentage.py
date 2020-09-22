#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

line_width = 2
dataset = '../../../dataset/lombardia.csv'

# column names
x_name = 'data'
y_new_cases = 'new_cases_test_percentage'
y_total_cases = 'positive_swabs_percentage'


# moving average
new_cases_rolling = 'new_cases_rolling'
total_cases_rolling = 'total_cases_rolling'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_new_cases, y_total_cases])
df = df[65:]

# calculate rolling average 3gg
df[new_cases_rolling] = df[y_new_cases].rolling(3).mean()
df[total_cases_rolling] = df[y_total_cases].rolling(3).mean()

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df[x_name], y=df[y_new_cases],
               name='New cases tested',
               line=dict(color='orange', width=line_width))
)

fig.add_trace(
    go.Scatter(x=df[x_name], y=df[y_total_cases],
               name='Total cases tested',
               line=dict(color='blue', width=line_width))
)

fig.add_trace(go.Scatter(x=df[x_name], y=df[new_cases_rolling], name='New cases (3 day average)',
                         line=dict(color='orange', width=line_width, dash='dot')))

fig.add_trace(go.Scatter(x=df[x_name], y=df[total_cases_rolling], name='Total cases (3 day average)',
                         line=dict(color='blue', width=line_width, dash='dot')))

# Add title
fig.update_layout(
    title_text="% New Cases / Swab Tests in Regione Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Percentage %")

fig.show()
