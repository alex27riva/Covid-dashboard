#!/usr/bin/python3
from datetime import date

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas
from dash.dependencies import Input, Output

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
rows = []

# read csv for url
df = pandas.read_csv(url)
# get a list off all regions
regions = df['denominazione_regione'].drop_duplicates().tolist()
print(regions)

plotly_js_minified = ['https://cdn.plot.ly/plotly-basic-latest.min.js']

app = dash.Dash(__name__, external_scripts=plotly_js_minified,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'}]
                )
app.title = 'Dashboard Regioni'

server = app.server


def generate_card(region_name):
    card = dbc.Card(
        [
            dbc.CardImg(src="/assets/img/" + region_name + ".png", top=True),
            dbc.CardBody(
                [
                    html.H4(region_name, className="card-title"),
                    dbc.Button("Go to dashboard", color="primary"),
                ]
            ),
        ],
        style={"width": "12rem"},
    )
    return card


def generate_card_row(left, right):
    return dbc.Row([
        dbc.Col(left,
                width=6
                ),
        dbc.Col(
            right,
            width=6
        )

    ])


# regions_iter = iter(regions)
#
# while regions > 0:
#     rows.append(generate_card_row(generate_card(regions[i]), generate_card(regions[i + 1])))

for i in range(0, 20):
    rows.append(generate_card_row(generate_card(regions[i]), generate_card(regions[i + 1])))

app.layout = html.Div(  # main div
    dbc.Container(
        rows
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
