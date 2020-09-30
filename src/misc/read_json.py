""" This file read italy json data"""
import json

path = '../../dataset/italy.json'
with open(path) as file:
    data = json.load(file)
print(list(data[0].keys()))


def calc_mortality():
    for day in data:
        fatality = day['deceduti'] / day['totale_casi']
        day['mortal_perc'] = round(fatality, 3)
        print(fatality)


calc_mortality()
