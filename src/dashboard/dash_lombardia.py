#!/usr/bin/python3
from datetime import date

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
today = date.today()

# read csv for url
df = pandas.read_csv(url)
df = df.loc[df['denominazione_regione'] == 'Lombardia']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Dashboard Lombardia'

# chart config
chart_config = {'displaylogo': False,
                'displayModeBar': False,
                'responsive': True
                }

# slider buttons
slider_button = list([
    dict(count=1,
         label="1m",
         step="month",
         stepmode="backward"),
    dict(count=3,
         label="3m",
         step="month",
         stepmode="backward"),
    dict(count=6,
         label="6m",
         step="month",
         stepmode="backward"),
    dict(step="all")
])

# data calculation
df['terapia_intensiva_avg'] = df['terapia_intensiva'].rolling(7).mean()
df['nuovi_decessi'] = df.deceduti.diff().fillna(df.deceduti)

# percentage swab - cases
df['delta_casi_testati'] = df.casi_testati.diff().fillna(df.casi_testati)
df['incr_tamponi'] = df.tamponi.diff().fillna(df.tamponi)
df['perc_positivi_tamponi'] = (df['nuovi_positivi'] / df['incr_tamponi']) * 100  # AB
df['perc_positivi_test'] = (df['nuovi_positivi'] / df['delta_casi_testati']) * 100  # AD

# rolling averages
df['nuovi_positivi_avg'] = df['nuovi_positivi'].rolling(7).mean()
df['nuovi_decessi_avg'] = df['nuovi_decessi'].rolling(7).mean()
df['totale_ospedalizzati_avg'] = df['totale_ospedalizzati'].rolling(7).mean()
df['perc_positivi_tamponi_avg'] = df['perc_positivi_tamponi'].rolling(3).mean()
df['perc_positivi_test_avg'] = df['perc_positivi_test'].rolling(3).mean()

app.layout = html.Div(  # main div
    html.Div([
        html.Div([
            html.Img(
                src='https://leformedelgusto.it/wp-content/uploads/2017/06/Logo-regione-lombardia-patrocinio-le-forme'
                    '-del-gusto.png',
                className='three columns',
                style={
                    'height': '15%',
                    'width': '15%',
                    'float': 'right',
                    'position': 'relative',
                },
            ),
            html.H1(children='Dashboard Lombardia',
                    className='nine columns'),

            html.Div(children='Situazione Covid-19 in Lombardia',
                     className='nine columns')

        ], className='row'),

        html.Div([  # andamento contagi, % casi tamponi
            html.Div([
                dcc.Graph(
                    id='andamento-contagi',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['nuovi_positivi'], 'type': 'bar', 'name': 'Nuovi Casi',
                             # 'marker': dict(color='LightSalmon')
                             },
                            {'x': df['data'], 'y': df['nuovi_positivi_avg'], 'type': 'scatter',
                             'line': dict(color='orange'),
                             'name': 'Media 7 giorni'}
                        ],
                        'layout': {
                            'title': 'Andamento dei contagi Lombardia',
                            'xaxis': dict(
                                rangeselector=dict(buttons=slider_button),
                                rangeslider=dict(visible=False),
                                type='date'
                            )
                        }
                    },
                    config=chart_config
                )

            ], className='twelve columns')

        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='perc-casi-tamponi',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['perc_positivi_test'], 'type': 'scatter',
                             'name': 'Nuovi Casi testati', 'line': dict(color='orange')},
                            {'x': df['data'], 'y': df['perc_positivi_tamponi'], 'type': 'scatter',
                             'line': dict(color='blue'),
                             'name': 'Totale casi testati'},
                            {'x': df['data'], 'y': df['perc_positivi_test_avg'], 'type': 'scatter',
                             'name': 'Nuovi Casi (media 3gg)', 'line': dict(color='orange', dash='dot')},
                            {'x': df['data'], 'y': df['perc_positivi_tamponi_avg'], 'type': 'scatter',
                             'line': dict(color='blue', dash='dot'),
                             'name': 'Totale casi (media 3gg)'}
                        ],
                        'layout': {
                            'title': '% Nuovi Casi / Test con tamponi in Regione Lombardia',
                            'xaxis': {
                                'type': 'date',
                                'range': ['2020-04-22', today]
                            },
                            'yaxis': {
                                'range': [0, 30],
                                'tickprefix': '% '
                            }

                        }
                    },
                    config=chart_config
                )

            ], className='six columns')

        ], className='row'),

        html.Div([  # second chart row
            html.Div([
                dcc.Graph(
                    id='Terapia-intensiva',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['terapia_intensiva'], 'type': 'bar', 'name': 'Terapia Intensiva',
                             'marker': dict(color='LightSalmon')},
                            {'x': df['data'], 'y': df['terapia_intensiva_avg'], 'type': 'scatter',
                             'line': dict(color='blue'),
                             'name': 'Media 7 giorni'}
                        ],
                        'layout': {
                            'title': 'Terapia intensiva',
                            'xaxis': dict(
                                rangeselector=dict(buttons=slider_button),
                                rangeslider=dict(visible=False),
                                type='date'
                            )
                        }
                    },
                    config=chart_config
                )
            ], className='four columns'),
            html.Div([
                dcc.Graph(
                    id='totale-ospedalizzati',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['totale_ospedalizzati'], 'type': 'bar',
                             'name': 'Ospedalizzazioni'},
                        ],
                        'layout': {
                            'title': 'Totale ospedalizzati',
                            'xaxis': dict(
                                rangeselector=dict(buttons=slider_button),
                                rangeslider=dict(visible=False),
                                type='date'
                            )
                        }
                    },
                    config=chart_config
                )
            ], className='four columns'),
            html.Div([
                dcc.Graph(
                    id='decessi-giornalieri',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['nuovi_decessi'], 'type': 'bar',
                             'marker': dict(color='grey')},
                        ],
                        'layout': {
                            'title': 'Decessi giornalieri',
                            'xaxis': dict(
                                rangeselector=dict(buttons=slider_button),
                                rangeslider=dict(visible=False),
                                type='date'
                            )
                        }
                    },
                    config={
                        'displaylogo': False,
                        'displayModeBar': False,
                        'responsive': True
                    }
                )
            ], className='four columns'),

        ], className='row'),

        html.Div([  # credits
            html.Footer(children='© 2020 D. Tosi, A. Riva, A. Schiavone, Università Insubria. All rights reserved.',
                        style=dict(font="14.0px 'Helvetica Light'"),
                        className='six columns')
        ], className='row')

    ], className='ten columns offset-by-one')  # twelve columns
)

if __name__ == '__main__':
    app.run_server(debug=True)
