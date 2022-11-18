from data_wrangler import *
from pprint import pprint

path_to_data = "./data/siege_locations.csv" # Path to the siege_locations.csv file
dataset = generate_siege_data(path_to_data)
#pprint(generate_siege_data(path_to_data))

def find_min_among_sieges(data):
    year_list = []
    for row in data:
        year_list.append(row[2])
    return year_list
    # pprint(year_list)

def count_sieges(data):
    year_list = find_min_among_sieges(data)
    return "There has been " + str(len(data)) + " sieges from year " + str(min(year_list)) + " to " + str(max(year_list)) + "."

pprint(count_sieges(dataset))