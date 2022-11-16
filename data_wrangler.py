# Importing csv to work with comma-separated value files.
import csv
import pandas as pd
from pprint import pprint

#def clean_multi_year_siege(year_data):

def clean_space(string_data):
    return string_data.rstrip(" ")

def generate_siege_data(path_string):
    list_of_sieges = []
    with open(path_string) as siege_data:
        csv_data = csv.reader(siege_data, delimiter=',')
        for row in csv_data:
            # row[1].replace(u"\uFFFD", "?").encode("utf-8")
            # row[3].replace(u"\uFFFD", "?").encode("utf-8")
            for item in row:
                if isinstance(item, str):
                    row[row.index(item)] = clean_space(item)
            list_of_sieges.append(row)
        del list_of_sieges[0]
    return list_of_sieges





#data = pd.read_csv('./data/siege_locations.csv')
#print(data)