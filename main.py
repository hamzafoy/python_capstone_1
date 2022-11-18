from data_wrangler import *
from data_analyser import *
from pprint import pprint

path_to_data = "./data/siege_locations.csv" # Path to the siege_locations.csv file
dataset = generate_siege_data(path_to_data)

def main(data):
    num_of_sieges = count_sieges(data)
    search_for_city = search_sieges_for_city(data)
    search_for_country = search_sieges_for_country(data)
    pprint(num_of_sieges)
    pprint(search_for_city)
    pprint(search_for_country)

main(dataset)