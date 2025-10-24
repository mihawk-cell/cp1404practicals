"""
Wimbledon Champions Program
Estimate: 30 minutes
Actual:
"""

import csv

def read_csv(filename):
    """Read CSV file and return data as a list of rows"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            data.append(row)
    return data

def count_champions(data):
    """Count how many times each champion has won"""
    champ_dict = {}
    for row in data:
        name = row["Champion"]
        champ_dict[name] = champ_dict.get(name, 0) + 1
    return champ_dict

def get_countries(data):
    """Return a sorted list of unique champion countries"""
    country_set = set()
    for row in data:
        country_set.add(row["Country"])
    return sorted(country_set)

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    # Count champion wins
    champions_dict = count_champions(data)

    # Get champion countries alphabetically
    countries_sorted = get_countries(data)

    # Print champions and their win counts
    print("Wimbledon Champions: ")
    for name, count in champions_dict.items():
        print(f"{name} {count}")

    # Print countries
    print(f"\nThese {len(countries_sorted)} countries have won Wimbledon: ")
    print(", ".join(countries_sorted))

if __name__ == "__main__":
    main()

