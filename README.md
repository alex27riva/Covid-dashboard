# Dashboard for Covid19-Italy

Development of an online service for the representation of charts on the Coronavirus Covid-19 pandemic.
Thesis project of Alessandro Riva, student at Università dell'Insubria.  
Thesis advisor: Prof. Davide Tosi

## How the dashboard works
The dashboard is made using Dash, a productive Python framework for building web analytic applications.

## Installation

To run the project is required:

- Pandas    `$ pip install pandas`
- Plotly    `$ pip install plotly==4.12.0`
- Dash      `$  pip install dash==1.17.0`
- Dash Bootstrap Components `$ pip install dash-bootstrap-components`

## Docker images
- [Italy](https://hub.docker.com/r/alex27riva/dash_italy)
- [Lombardy](https://hub.docker.com/r/alex27riva/dashboard_lombardia)
- [Italy regions](https://hub.docker.com/r/alex27riva/dashboard_regioni)

## Data source
Data is taken from the Department of Italian Civil Protection [GitHub](https://github.com/pcm-dpc/COVID-19)
