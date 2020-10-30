#!/usr/bin/python3
from datetime import date

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
from dash.dependencies import Input, Output

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
today = date.today()
REF_TAMP = 9000  # reference value
regions = ['Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna', 'Friuli Venezia Giulia', 'Lazio',
           'Liguria', 'Lombardia', 'Marche', 'Molise', 'P.A. Bolzano', 'P.A. Trento', 'Piemonte', 'Puglia',
           'Sardegna', 'Sicilia', 'Toscana', 'Umbria', "Valle d'Aosta", 'Veneto']

# read csv for url
df = pandas.read_csv(url)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
plotly_js_minified = ['https://cdn.plot.ly/plotly-basic-latest.min.js']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                external_scripts=plotly_js_minified,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'}]
                )
app.title = 'Dashboard Regioni'

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


def calculate_data(dframe):
    # data calculation
    dframe['terapia_intensiva_avg'] = dframe['terapia_intensiva'].rolling(7).mean()
    dframe['nuovi_decessi'] = dframe.deceduti.diff().fillna(dframe.deceduti)

    # percentage swab - cases
    dframe['delta_casi_testati'] = dframe.casi_testati.diff().fillna(dframe.casi_testati)
    dframe['incr_tamponi'] = dframe.tamponi.diff().fillna(dframe.tamponi)
    dframe['perc_positivi_tamponi'] = (dframe['nuovi_positivi'] / dframe['incr_tamponi']) * 100  # AB
    dframe['perc_positivi_test'] = (dframe['nuovi_positivi'] / dframe['delta_casi_testati']) * 100  # AD

    # rolling averages
    dframe['nuovi_positivi_avg'] = dframe['nuovi_positivi'].rolling(7).mean()
    dframe['nuovi_decessi_avg'] = dframe['nuovi_decessi'].rolling(7).mean()
    dframe['totale_ospedalizzati_avg'] = dframe['totale_ospedalizzati'].rolling(7).mean()
    dframe['perc_positivi_tamponi_avg'] = dframe['perc_positivi_tamponi'].rolling(3).mean()
    dframe['perc_positivi_test_avg'] = dframe['perc_positivi_test'].rolling(3).mean()

    # norm cases
    dframe['nuovi_casi_norm'] = dframe['nuovi_positivi'] * REF_TAMP / dframe['incr_tamponi']
    return dframe


def get_lista():
    selections = []
    for reg in regions:
        selections.append(dict(label=reg, value=reg))
    return selections


app.layout = html.Div(  # main div
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(id='region_select',
                             options=get_lista(),
                             placeholder='Seleziona una regione...',
                             persistence=True,
                             persistence_type='session'
                             )

            ], className='four columns offset-by-three')
        ], className='row'),
        html.Div([  # andamento contagi
            html.Div([
                dcc.Graph(
                    id='andamento-contagi',

                    config=chart_config
                )

            ], className='twelve columns')

        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='perc-casi-tamponi',

                    config=chart_config
                )

            ], className='six columns'),
        ], className='row'),

        html.Div([  # second chart row

            html.Div([
                dcc.Graph(
                    id='totale-ospedalizzati',

                    config=chart_config
                )
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='decessi-giornalieri',

                    config={
                        'displaylogo': False,
                        'displayModeBar': False,
                        'responsive': True
                    }
                )
            ], className='six columns'),

        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='terapia-intensiva',
                    config=chart_config
                )
            ], className='twelve columns'),

        ], className='row')

    ], className='ten columns offset-by-one')
)


@app.callback(
    Output('andamento-contagi', 'figure'),
    [Input('region_select', 'value')])
def update_andamento_contagi(regione):
    reg_df = df.loc[df['denominazione_regione'] == regione]
    local_df = calculate_data(reg_df.copy())
    local_df['nuovi_positivi_avg'] = local_df['nuovi_positivi'].rolling(7).mean()
    figure = {
        'data': [
            {'x': local_df['data'], 'y': local_df['nuovi_positivi'], 'type': 'bar', 'name': 'Nuovi Casi'},
            {'x': local_df['data'], 'y': local_df['nuovi_positivi_avg'], 'type': 'scatter',
             'line': dict(color='orange'),
             'name': 'Media 7 giorni'}
        ],
        'layout': {
            'title': 'Andamento dei contagi',
            'xaxis': dict(
                rangeselector=dict(buttons=slider_button),
                rangeslider=dict(visible=False),
                type='date'
            )
        }
    }
    return figure


@app.callback(
    Output('perc-casi-tamponi', 'figure'),
    [Input('region_select', 'value')])
def update_perc_casi_tamponi(regione):
    reg_df = df.loc[df['denominazione_regione'] == regione]
    local_df = calculate_data(reg_df.copy())

    figure = {
        'data': [
            {'x': local_df['data'], 'y': local_df['perc_positivi_test'], 'type': 'scatter',
             'name': 'Nuovi Casi testati', 'line': dict(color='orange')},
            {'x': local_df['data'], 'y': local_df['perc_positivi_tamponi'], 'type': 'scatter',
             'line': dict(color='blue'),
             'name': 'Totale casi testati'},
            {'x': local_df['data'], 'y': local_df['perc_positivi_test_avg'], 'type': 'scatter',
             'name': 'Nuovi Casi (media 3gg)', 'line': dict(color='orange', dash='dot')},
            {'x': local_df['data'], 'y': local_df['perc_positivi_tamponi_avg'], 'type': 'scatter',
             'line': dict(color='blue', dash='dot'),
             'name': 'Totale casi (media 3gg)'}
        ],
        'layout': {
            'title': '% Nuovi Casi / Test tramite tamponi',
            'xaxis': {
                'type': 'date',
                'range': ['2020-04-22', today],
                'rangeselector': dict(buttons=slider_button),
                'rangeslider': dict(visible=False)

            },
            'yaxis': {
                'range': [0, 30],
                'tickprefix': '% '
            }

        }
    }
    return figure


@app.callback(
    Output('totale-ospedalizzati', 'figure'),
    [Input('region_select', 'value')])
def update_perc_casi_tamponi(regione):
    reg_df = df.loc[df['denominazione_regione'] == regione]
    local_df = calculate_data(reg_df.copy())
    figure = {
        'data': [
            {'x': local_df['data'], 'y': local_df['totale_ospedalizzati'], 'type': 'bar',
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
    }
    return figure


@app.callback(
    Output('decessi-giornalieri', 'figure'),
    [Input('region_select', 'value')])
def update_perc_casi_tamponi(regione):
    reg_df = df.loc[df['denominazione_regione'] == regione]
    local_df = calculate_data(reg_df.copy())
    figure = {
        'data': [
            {'x': local_df['data'], 'y': local_df['nuovi_decessi'], 'type': 'bar',
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
    }
    return figure


@app.callback(
    Output('terapia-intensiva', 'figure'),
    [Input('region_select', 'value')])
def update_perc_casi_tamponi(regione):
    reg_df = df.loc[df['denominazione_regione'] == regione]
    local_df = calculate_data(reg_df.copy())
    figure = {
        'data': [
            {'x': local_df['data'], 'y': local_df['terapia_intensiva'], 'type': 'bar', 'name': 'Terapia Intensiva',
             'marker': dict(color='LightSalmon')},
            {'x': local_df['data'], 'y': local_df['terapia_intensiva_avg'], 'type': 'scatter',
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
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
