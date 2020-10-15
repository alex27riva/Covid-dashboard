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

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

# app = dash.Dash()
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Dashboard Italia'

# data calculation
df['terapia_intensiva_avg'] = df['terapia_intensiva'].rolling(7).mean()


# deaths curve
def deaths_curve():
    df['deceduti_giorn'] = df.deceduti.diff().shift(-1)
    df['moving_avg'] = df['deceduti_giorn'].rolling(7).mean()
    fig = go.Figure(
        go.Bar(x=df['data'], y=df['deceduti_giorn'],
               name='Deaths',
               marker_color='orange')

    )
    fig.add_trace(
        go.Scatter(x=df['data'], y=df['moving_avg'],
                   name='7 day avg'

                   ))

    fig.update_layout(
        title_text='Daily deaths'
    )
    fig.update_xaxes(title_text="Days")
    return fig


# chart 13
def home_isolation():
    fig = go.Figure(
        go.Bar(x=df['data'], y=df['isolamento_domiciliare'],
               name='Home Isolation',
               marker_color='SlateGray')

    )

    fig.update_layout(
        title_text='Home isolation'
    )
    fig.update_xaxes(title_text="Days")
    return fig


def normalized_new_cases():
    MIN_DELTA_TAMP = 964  # =MIN(Q$7:Q$119)    Q = delta_tamp
    REF_TAMP = 48000  # reference value

    # column names
    x_name = 'data'
    y_moving_7gg = 'delta_cases_average'
    df_loc = df.copy()
    df_loc = df_loc[77:]
    df_loc['delta_tamponi'] = df_loc.tamponi.diff().fillna(df_loc.tamponi)
    df_loc['tamp_norm'] = MIN_DELTA_TAMP / df_loc['delta_tamponi'] * df_loc['nuovi_positivi']
    df_loc['nuovi_casi_norm'] = df_loc['nuovi_positivi'] * REF_TAMP / df_loc['delta_tamponi']

    # rolling average 7gg
    df_loc[y_moving_7gg] = df_loc['nuovi_casi_norm'].rolling(7).mean()

    fig = go.Figure(
        go.Bar(x=df_loc[x_name], y=df_loc['nuovi_casi_norm'].astype(int),  # convert to int
               name='New cases')
    )

    fig.add_trace(
        go.Scatter(x=df_loc[x_name],
                   y=df_loc[y_moving_7gg],
                   name='7 day average')
    )

    fig.update_layout(
        title_text='Normalized new daily cases in Italy (+ 7 day avg)'
    )
    fig.update_xaxes(title_text="Days")
    fig.update_yaxes(title_text="Normalized daily cases")
    return fig


# Bootstrap CSS
# app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(  # main div
    html.Div([
        html.Div([
            html.Img(
                src='https://www.uninsubria.it/sites/all/themes/uninsubria/logo.png',
                className='three columns',
                style={
                    'height': '9%',
                    'width': '9%',
                    'float': 'right',
                    'position': 'relative',
                },
            ),
            html.H1(children='Dashboard Italy',
                    className='nine columns'),

            html.Div(children='Covid19 dashboard for Italy',
                     className='nine columns')

        ], className='row'),

        html.Div([  # div for charts
            html.Div([
                dcc.Graph(
                    id='cumulative-icu',
                    figure={
                        'data': [
                            {'x': df['data'], 'y': df['terapia_intensiva'], 'type': 'bar', 'name': 'Terapia Intensiva'},
                            {'x': df['data'], 'y': df['terapia_intensiva_avg'], 'type': 'scatter',
                             'name': '7 day moving avg'}
                        ],
                        'layout': {
                            'title': 'Terapia intensiva'
                        }
                    },
                    config={
                        'displaylogo': False,
                        'displayModeBar': False
                    },
                    style={
                        'margin-top': 20
                    }
                )
            ], className='six columns')
        ], className='row')
    ], className='ten columns offset-by-one')
)

if __name__ == '__main__':
    app.run_server(debug=True)
