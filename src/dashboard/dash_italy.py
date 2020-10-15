import dash
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_html_components as html
import pandas

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

# read csv for url
df = pandas.read_csv(url)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app_title = 'Dashboard Italia'

# data calculation
df['terapia_intensiva_avg'] = df['terapia_intensiva'].rolling(7).mean()
df['nuovi_decessi'] = df.deceduti.diff().fillna(df.deceduti)

app.layout = html.Div(  # main div
    html.Div([
        html.Div([
            html.Img(
                src='https://www.uninsubria.it/sites/all/themes/uninsubria/logo.png',
                className='three columns',
                style={
                    'height': '8%',
                    'width': '8%',
                    'float': 'right',
                    'position': 'relative',
                },
            ),
            html.H1(children='Dashboard Italia',
                    className='nine columns'),

            html.Div(children='Situazione Covid-19 in Italia',
                     className='nine columns')

        ], className='row'),

        html.Div([  # first chart row
            html.Div([
                dcc.Graph(
                    id='Terapia-intensiva',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['terapia_intensiva'], 'type': 'bar', 'name': 'Terapia Intensiva',
                             'marker': dict(color='DodgerBlue')},
                            {'x': df['data'], 'y': df['terapia_intensiva_avg'], 'type': 'scatter',
                             'line': dict(color='blue'),
                             'name': '7 day moving avg'}
                        ],
                        'layout': {
                            'title': 'Terapia intensiva'
                        }
                    },
                    config={
                        'displaylogo': False,
                        'displayModeBar': False
                    }
                )
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='Casi-totali',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['totale_casi'], 'type': 'bar', 'name': 'Casi totali'},
                        ],
                        'layout': {
                            'title': 'Casi totali'
                        }
                    },
                    config={
                        'displaylogo': False,
                        'displayModeBar': False
                    }
                )
            ], className='six columns')
        ], className='row'),

        html.Div([  # second chart row
            html.Div([
                dcc.Graph(
                    id='nuovi-casi-vs-morti',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['nuovi_decessi'], 'type': 'bar', 'name': 'Morti giornalieri',
                             'marker': dict(color='DimGrey')},
                            {'x': df['data'], 'y': df['nuovi_positivi'], 'type': 'scatter', 'xaxis': 'x2',
                             'yaxis': 'y2',
                             'line': dict(color='blue'),
                             'name': 'Nuovi casi'}
                        ],
                        'layout': {
                            'yaxis': {
                                'title': 'Nuovi casi vs morti giornalieri',
                                'secondary_y': False
                            },
                            'yaxis2': {
                                'title': 'Nuovi casi vs morti giornalieri',
                                'secondary_y': True
                            }

                        }
                    },
                    config={
                        'displaylogo': False,
                        'displayModeBar': False
                    }
                )

            ], className='twelve columns')

        ], className='row')
    ], className='ten columns offset-by-one')
)

if __name__ == '__main__':
    app.run_server(debug=True)
