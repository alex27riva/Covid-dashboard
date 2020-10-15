#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go
import numpy as np

"""
Chart n°: 2
Title: New Daily Cases - Estimate of the Phase2 and Phase2bis Impact - ITA
Description: Estimation of the Phase2 and Phase2bis Impact in Italy
Polynomial fit: https://plotly.com/python/v3/polynomial-fits/
"""
# todo: add polynomial line

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# chart title
chart_title = 'New Daily Cases - Estimate of the Phase2 and Phase2bis Impact - ITA'

# column names
x_name = 'data'
y_name = 'nuovi_positivi'

df = pd.read_csv(url, usecols=[x_name, y_name])
df_phase2 = df[33:92]
df_phase2_bis = df[92:217]

array = df.to_numpy()

# points
x_list = array[:, 0]
y_list = array[:, 1]

# calculate polynomial
# z = np.polyfit(x_list, y_list, 3)
# f = np.poly1d(z)

# calculate new x's and y's
# x_new = np.linspace(x_list[0], x_list[-1], 50)
# y_new = f(x_new)

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

# fig.add_trace(
#     go.Scatter(x=x_new,
#                y=y_new,
#                name='Polynomial line',
#                )
# )

# Add title
fig.update_layout(
    title_text=chart_title
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
# fig.update_yaxes(title_text='')

fig.show()
