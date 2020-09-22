#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/lombardia.csv'

df = pd.read_csv(dataset, index_col=[], usecols=['data', 'new_cases_test_percentage', 'positive_swabs_percentage'])
df = df[65:]

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

# Add title
fig.update_layout(
    title_text="% New Cases / Swab Tests in Regione Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
# fig.update_yaxes(title_text="Normalized dayly cases")

fig.show()
