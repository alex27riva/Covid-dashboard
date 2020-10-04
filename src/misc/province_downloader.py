import datetime
import os

import requests
from progress.bar import Bar

url_province = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-'
start_date = datetime.datetime(2020, 2, 24)  # '20200224'

download_folder = '/tmp/province/'

date_list = []

today = datetime.datetime.now()
current_date = start_date
while current_date < today:
    date_list.append(current_date.strftime("%Y%m%d"))
    current_date += datetime.timedelta(days=1)


def download_file(file_date):
    url = url_province + file_date + '.csv'
    r = requests.get(url, allow_redirects=False)
    if r.status_code != 404:
        with open("province/province-" + file_date + '.csv', 'wb') as f:
            f.write(r.content)
            return True
    else:
        return False


def download_all_files():
    bar = Bar('Downloading', max=len(date_list))
    for date in date_list:
        download_file(date)
        bar.next()
    bar.finish()


def check_files():
    downloaded = 0
    for date in date_list:
        if not os.path.isfile('province/province-' + date + '.csv'):
            if download_file(date):
                print(date)
                downloaded += 1
    print("scaricati:, ", downloaded, "file")


download_all_files()
