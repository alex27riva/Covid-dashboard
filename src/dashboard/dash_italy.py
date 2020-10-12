import dash
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_html_components as html
import pandas

# data URL
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento' \
      '-nazionale.csv'

df = pandas.read_csv(url)

app = dash.Dash()

app.title = 'Dashboard Italy'


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


# chart n°11
def cumulative_icu():
    y_moving_7gg = 'moving_avg'
    df[y_moving_7gg] = df['terapia_intensiva'].rolling(7).mean()
    fig = go.Figure(
        go.Bar(x=df['data'], y=df['terapia_intensiva'],
               name='ICU patients',
               marker_color='orange')

    )

    fig.add_trace(
        go.Scatter(x=df['data'],
                   y=df[y_moving_7gg],
                   name='7 day average',
                   line=dict(color='blue',
                             dash='dot'))
    )
    # Add title
    fig.update_layout(
        title_text='ICU Cumulative'
    )
    # set x axis name
    fig.update_xaxes(title_text="Days")
    return fig


# ---

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


app.layout = html.Div(
    html.Div([
        html.H1(children='Dashboard Italy'),

        html.Div(children='Covid19 dashboard for Italy'),

        dcc.Graph(id='cumulative-icu',
                  figure=cumulative_icu()
                  ),
        dcc.Graph(id='isolamento-domiciliare',
                  figure=home_isolation()),
        dcc.Graph(id='daily-deaths',
                  figure=deaths_curve())

    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)
