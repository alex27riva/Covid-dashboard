""" This file read italy json data and calculate some other values"""
import json

path = '../../dataset/italy.json'

# list of dict for output data
timestamp_list = []

# open input file
with open(path) as file:
    italy_data = json.load(file)


# list dat keys
# print(list(italy_data[0].keys()))

# function to delete a key pair
def remove_key(key):
    for x in italy_data:
        del x[key]


def calc_mortality():
    for day in italy_data:
        fatality = day['deceduti'] / day['totale_casi']
        day['calculated_mortal_perc'] = round(fatality, 3)


def calc_new_cases():
    for i, day in enumerate(italy_data):
        if i > 0:
            day['calculated_daily_new_cases'] = day['totale_casi'] - italy_data[i - 1]['totale_casi']


def calc_growth_index():
    for i, day in enumerate(italy_data):
        if i > 0:
            growth_index = day['calculated_daily_new_cases'] / italy_data[i - 1]['totale_casi']
            italy_data[i]['calculated_growth_index'] = round(growth_index, 3)


def calc_daily_death():
    for i, day in enumerate(italy_data):
        if i == 0:
            day['calculated_daily_deaths'] = day['deceduti']
        else:
            day['calculated_daily_deaths'] = day['deceduti'] - italy_data[i - 1]['deceduti']


calc_mortality()
calc_new_cases()
calc_growth_index()
calc_daily_death()

with open('out.json', 'w') as out:
    json.dump(italy_data, out, indent=4)
