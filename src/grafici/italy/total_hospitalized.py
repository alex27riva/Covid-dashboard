#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

dataset = '../../../dataset/dpc-covid19-ita-andamento-nazionale.csv'

# column names
x_name = 'data'
y_name = 'totale_ospedalizzati'
y_moving_7gg = '7_day_moving_average'

df = pd.read_csv(dataset, index_col=[], usecols=[x_name, y_name])

# rolling average 7gg
df[y_moving_7gg] = df[y_name].rolling(7).mean()

fig = go.Figure(
    go.Bar(x=df[x_name], y=df[y_name],
           name='Total hospitalized')
)

fig.add_trace(
    go.Scatter(x=df[x_name],
               y=df[y_moving_7gg],
               name='7 day average',
               line=dict(color='blue',
                         dash='dot'))
)
# Add title
fig.update_layout(
    title_text="ICU + severe disease"
)
# set x axis name
fig.update_xaxes(title_text="Days")
# set y axis title
# fig.update_yaxes(title_text="Normalized daily cases")

fig.show()
