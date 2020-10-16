#!/usr/bin/python3
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'

# read csv for url
df = pandas.read_csv(url)
df = df.loc[df['denominazione_regione'] == 'Lombardia']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app_title = 'Dashboard Lombardia'

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
df['nuovi_positivi_avg'] = df['nuovi_positivi'].rolling(7).mean()
df['nuovi_decessi_avg'] = df['nuovi_decessi'].rolling(7).mean()
df['totale_ospedalizzati_avg'] = df['totale_ospedalizzati'].rolling(7).mean()

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

        html.Div([  # first chart row
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
                            'title': 'Terapia intensiva'
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
                            {'x': df['data'], 'y': df['totale_ospedalizzati'], 'type': 'bar', 'name': 'Ospedalizzazioni'},
                        ],
                        'layout': {
                            'title': 'Totale ospedalizzati'
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
                            'title': 'Decessi giornalieri'
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
        # html.Div([  # second chart row
        #     html.Div([
        #         dcc.Graph(
        #             id='rapporto-positivi-tamponi',
        #             figure={
        #                 'data': [
        #                     {'x': df['data'], 'y': df['nuovi_positivi'], 'type': 'scatter',
        #                      'line': dict(color='orange', dash='dot'),
        #                      'name': 'Nuovi casi'},
        #                     {'x': df['data'], 'y': df['nuovi_decessi'], 'type': 'scatter', 'yaxis': 'y2',
        #                      'line': dict(color='blue', dash='dot'),
        #                      'name': 'Decessi giornalieri'},
        #                     {'x': df['data'], 'y': df['nuovi_positivi_avg'], 'type': 'scatter',
        #                      'line': dict(color='orange'),
        #                      'name': 'Nuovi casi (media 7 giorni)'},
        #                     {'x': df['data'], 'y': df['nuovi_decessi_avg'], 'type': 'scatter', 'yaxis': 'y2',
        #                      'line': dict(color='blue'),
        #                      'name': 'Nuovi decessi (media 7 giorni)'}
        #                 ],
        #                 'layout': {
        #                     'title': 'Media mobile a 7gg: Decessi giornalieri vs. Contagi giornalieri',
        #                     'yaxis': {'rangemode': 'nonnegative'},
        #                     'yaxis2': {
        #                         'side': 'right',
        #                         'overlaying': 'y',  # show both traces,
        #                         'rangemode': 'nonnegative'
        #
        #                     }
        #
        #                 }
        #             },
        #             config=chart_config
        #         )
        #
        #     ], className='six columns'),
        #     html.Div([
        #         dcc.Graph(
        #             id='totale-ospedalizzati',
        #             figure={
        #                 'data': [
        #                     {'x': df['data'], 'y': df['totale_ospedalizzati'], 'type': 'bar',
        #                      'name': 'Totale ospedalizzati',
        #                      'marker': dict(color='DarkCyan')},
        #                     {'x': df['data'], 'y': df['totale_ospedalizzati_avg'], 'type': 'scatter',
        #                      'line': dict(color='blue', dash='dot'),
        #                      'name': 'Media 7 giorni'}
        #                 ],
        #                 'layout': {
        #                     'title': 'Terapia intensiva e casi gravi'
        #                 }
        #             },
        #             config=chart_config
        #         )
        #     ], className='six columns')
        #
        # ], className='row'),
        #
        # html.Div([  # third chart row
        #     html.Div([
        #         dcc.Graph(
        #             id='nuovi-casi-vs-morti',
        #             figure={
        #                 'data': [
        #                     {'x': df['data'], 'y': df['nuovi_decessi'], 'type': 'bar', 'name': 'Nuovi decessi',
        #                      'yaxis': 'y1', 'marker': dict(color='orange')},
        #                     {'x': df['data'], 'y': df['nuovi_positivi'], 'type': 'scatter', 'yaxis': 'y2',
        #                      'line': dict(color='blue'),
        #                      'name': 'Nuovi casi'}
        #                 ],
        #                 'layout': {
        #                     'title': 'Nuovi casi vs decessi',
        #                     'xaxis': dict(
        #                         rangeselector=dict(buttons=slider_button),
        #                         rangeslider=dict(visible=True),
        #                         type='date'
        #                     ),
        #                     'yaxis': {'rangemode': 'nonnegative',
        #                               },
        #                     'yaxis2': {
        #                         'side': 'right',
        #                         'overlaying': 'y',  # show both traces,
        #                         'rangemode': 'tozero'
        #
        #                     }
        #
        #                 }
        #             },
        #             config=chart_config
        #         )
        #
        #     ], className='twelve columns')
        #
        # ], className='row')

    ], className='twelve columns')
)

if __name__ == '__main__':
    app.run_server(debug=True)
