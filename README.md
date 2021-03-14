# Dashboard for Covid19-Italy

Development of an online service for the representation of charts about the Covid-19 pandemic.
Thesis project of Alessandro Riva, student at __Università degli studi dell'Insubria__.  
Thesis advisor: Prof. Davide Tosi

## How dashboard works
Dashboards fetch data directly from the CSV file present in the Github repository provided by the Department of Italian Civil Protection.
Dashboards are stateless, i.e. without memory, therefore the data is not stored locally, but taken from the repository at each page load.

## Installation

To run the project is required:

- Pandas    `$ pip install pandas`
- Plotly    `$ pip install plotly==4.12.0`
- Dash      `$ pip install dash==1.17.0`
- Dash Bootstrap Components `$ pip install dash-bootstrap-components`

## Docker images
- [Italy](https://hub.docker.com/r/alex27riva/dash_italy)
- [Lombardy](https://hub.docker.com/r/alex27riva/dashboard_lombardia)
- [Italy regions](https://hub.docker.com/r/alex27riva/dashboard_regioni)

## Data source
Data is taken from the Department of Italian Civil Protection [GitHub](https://github.com/pcm-dpc/COVID-19)

## License
This project is licensed under the terms of the GNU GPLv3 license.
