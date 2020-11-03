#!/usr/bin/python3

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
rows = []

# read csv for url
df = pandas.read_csv(url)
# get a list off all regions
regions = df['denominazione_regione'].drop_duplicates().tolist()
regions.reverse()

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
        style={"width": "10rem"},
    )
    return card


def generate_card_row(left, right):
    if right is not None:
        return dbc.Row([
            dbc.Col(generate_card(left),
                    width=6
                    ),
            dbc.Col(
                generate_card(right),
                width=6
            )

        ])
    else:
        return dbc.Row(
            dbc.Col(generate_card(left),
                    width=6
                    )
        )


while len(regions) > 1:
    l = regions.pop()
    if len(regions) == 1:
        r = None
    else:
        r = regions.pop()
    rows.append(generate_card_row(l, r))

app.layout = html.Div(
    dbc.Container(
        rows
    )
    , className='mt-5')

if __name__ == '__main__':
    app.run_server(debug=True)
