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

def search_city_among_sieges(data):
    city_list = []
    search_item = input("Enter what city you want to search the data for: ")
    for row in data:
        if row[3] == search_item:
            city_list.append(row[3])
    return city_list, search_item

def search_country_among_sieges(data):
    country_list = []
    search_item = input("Enter what country you want to search the data for: ")
    for row in data:
        if row[4] == search_item:
            country_list.append(row[4])
    return country_list, search_item

def search_sieges_for_city(data):
    search_for_city = search_city_among_sieges(data)
    result = 'is not found'
    if len(search_for_city[0]) >= 1:
        result = 'is found'
    return "The city of " + search_for_city[1] + " " + result + " in the dataset."

def search_sieges_for_country(data):
    search_for_country = search_country_among_sieges(data)
    result = 'is not found'
    if len(search_for_country[0]) >= 1:
        result = 'is found'
    return "The country of " + search_for_country[1] + " " + result + " in the dataset."

def count_sieges(data):
    year_list = find_min_among_sieges(data)
    return "There has been " + str(len(data)) + " sieges from year " + str(min(year_list)) + " to " + str(max(year_list)) + "."

pprint(count_sieges(dataset))
pprint(search_sieges_for_country(dataset))