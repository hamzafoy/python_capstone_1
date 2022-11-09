# Importing csv to work with comma-separated value files.
import csv
import pandas as pd
from pprint import pprint



path_to_data = "./data/siege_locations.csv" # Path to the siege_locations.csv file
def generate_siege_data(path_string):
    list_of_sieges = []
    with open(path_string) as siege_data:
        csv_data = csv.reader(siege_data, delimiter=',')
        for row in csv_data:
            list_of_sieges.append(row)
        list_of_sieges.pop('years')
        del list_of_sieges[0]
        
    return list_of_sieges



#pprint(generate_siege_data(path_to_data))

data = pd.read_csv('./data/siege_locations.csv')
print(data)