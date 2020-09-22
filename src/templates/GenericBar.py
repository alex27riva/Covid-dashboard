#!/usr/bin/python3
import pandas as pd
import plotly.graph_objects as go

# define column names
x_name = 'data'
y_name = 'delta_cases'
y_moving_7gg = 'new_cases_average'


class NewDailyCases:
    """This class show a graph that contains scatter and Bar"""

    def __init__(self, data):
        global fig
        df = pd.read_csv(data, index_col=[], usecols=[x_name, y_name])
        fig = go.Figure()  # create figure object

    def add_bar(self, x, y, name):
        fig.add_trace(
            go.Bar(x=x, y=y,
                   name=name)
        )


# Add title
fig.update_layout(
    title_text="Andamento dei contagi Lombardia"
)
# set x axis name
fig.update_xaxes(title_text="Giorni")
# set y axis title
fig.update_yaxes(title_text="Contagi totali")
fig.update_yaxes(title_text="Contagi giornalieri")

fig.show()
