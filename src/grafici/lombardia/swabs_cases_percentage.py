#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/lombardia.csv'

df = pd.read_csv(dataset, index_col=[], usecols=['data', 'new_cases_test_percentage', 'positive_swabs_percentage'])
df = df[65:]

# rolling average 3gg
df['new_cases_rolling'] = df['new_cases_test_percentage'].rolling(3).mean()
df['total_cases_rolling'] = df['positive_swabs_percentage'].rolling(3).mean()

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df['data'], y=df['new_cases_test_percentage'],
               name='New cases tested',
               line=dict(color='orange', width=4))
)

fig.add_trace(
    go.Scatter(x=df['data'], y=df['positive_swabs_percentage'],
               name='Total cases tested',
               line=dict(color='blue', width=4))
)

fig.add_trace(go.Scatter(x=df['data'], y=df['new_cases_rolling'], name='New cases (3 day average)',
                         line=dict(color='orange', width=4, dash='dot')))

fig.add_trace(go.Scatter(x=df['data'], y=df['total_cases_rolling'], name='New cases (3 day average)',
                         line=dict(color='blue', width=4, dash='dot')))

# Add title
fig.update_layout(
    title_text="% New Cases / Swab Tests in Regione Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
# fig.update_yaxes(title_text="Normalized dayly cases")

fig.show()
