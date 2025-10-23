from operator import itemgetter
from os.path import split


def MAIN():
    DYNAMIC_NEAT_OUTPUT()
    DICTIONARY()
    READ_DATA()

"""
How do we het this dynamic neat output?

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

Desired output from any similar list of [name, score] pairs:

Derek       =   7
Xavier      =  80
Bob         = 612
Chantanelle =   9
"""
def DYNAMIC_NEAT_OUTPUT():
    print()

"""
Now, what if this were a dictionary?

{'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

Desired output from any similar dictionary:

Bob         = 612
Xavier      =  80
Chantanelle =   9
Derek       =   7
"""
def DICTIONARY():
    name_to_age = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

    name_width = max((len(name) for name in name_to_age.keys()))
    age_width = max((len(str(age)) for age in name_to_age.values()))

    print(name_width)
    print(age_width)

    for name, age in sorted(name_to_age.items(), key=itemgetter(1), reverse=True):
        print(f"{name:{name_width}} = {age:{age_width}}")

"""
Write a function that takes a list of strings and returns a dictionary of pairs:

string: length of string
"""

def LIST_TO_DICTIONARY():
    names = ["Cliff", "Lea", "Gynn"]
    #
    # name_to_length = {}
    #
    # for name in names:
    #     name_to_length[name] = len(name)

    print({name : len(name) for name in names})

    # print(name_to_length)

"""
"""
def READ_DATA():
    import csv

    FILENAME = "countries.csv"

    def main():
        country_to_data = read_data(FILENAME)
        (country_to_data)

    def read_data(filename):
        country_to_data = {}
        with open(filename) as in_file:
            reader = csv.reader(in_file)
            next(reader)
            for record in reader:
                record[2] = int(record[2].replace(",", ""))
                record[3] = float(record[3][:-1])
                country_to_data[record[0]] = record[1:-1]
        return country_to_data

    def print_details(country_to_data):
        country_names = sorted(country_to_data.keys())

    main()




