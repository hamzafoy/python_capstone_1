from data_wrangler import *
from pprint import pprint

path_to_data = "./data/siege_locations.csv" # Path to the siege_locations.csv file
dataset = generate_siege_data(path_to_data)
#pprint(generate_siege_data(path_to_data))

def count_sieges(data):
    return "There has been " + str(len(data)) + " sieges from year 1600 to 1800"

pprint(count_sieges(dataset))