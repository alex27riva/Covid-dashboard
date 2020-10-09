#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

"""
Chart n°: 2
Title: New Daily Cases - Estimate of the Phase2 and Phase2bis Impact - ITA
Description: Estimation of the Phase2 and Phase2bis Impact in Italy
"""

dataset = '../../../dataset/italy.csv'

# chart title
chart_title = 'New Daily Cases - Estimate of the Phase2 and Phase2bis Impact - ITA'

# column names
x_name = 'date'
y_name = 'new_daily_cases'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])
df_phase2 = df[33:92]
df_phase2_bis = df[92:217]

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df_phase2[x_name],
               y=df_phase2[y_name],
               name='Phase 2 Impact',
               mode='markers',
               marker=dict(
                   size=10,
                   symbol='square'
               ),
               line=dict(color='DeepSkyBlue'))
)

fig.add_trace(
    go.Scatter(x=df_phase2_bis[x_name],
               y=df_phase2_bis[y_name],
               name='Phase2Bis Potential Impact',
               mode='markers',
               marker=dict(
                   size=10,
                   symbol='square'
               ),
               line=dict(color='yellow'))
)


# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
