import pandas as pd


class Util:
    """This class is used to derive more data from .csv file"""

    def __init__(self, file):
        self.df = pd.read_csv(file)

    def print_colunm_names(self):
        print(self.df.columns)

    def column_list(self):
        return list(self.df.columns)

    def calc_delta(self, col, new_col):
        self.df[new_col] = self.df.col.diff().shift(-1)


test_url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita' \
           '-andamento-nazionale.csv '
u = Util(test_url)
print(u.column_list())
