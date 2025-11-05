from prac_06.guitar import Guitar
from operator import attrgetter


def main():
    guitars = []

    print("My guitars!")

    name = input("Enter guitar name: ")
    while name != "":
        year = int(input("Enter year: "))
        cost =  float(input("Enter cost: $"))
        guitar_add = Guitar(name, year, cost)   # create guitar
        guitars.append(guitar_add)  # add object into guitar
        print(f"{guitar_add} added")
        name = input("Enter guitar name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Fender Stratocruisers", 2014, 765.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort(key=attrgetter("year"))

    if guitars:     # lists, strings and other collections are False
        # In order for sorting to work on Guitar objects,
        # the __lt__ method must be defined in Guitar class
        # guitars.sort()
        print("These are my guitars:")

        for i, guitar in enumerate(guitars, 1): # enumerate()
            # enumerate object
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            # Note the use of the format method and numbered
            print(f"Guitar {i}: {guitar.name:<23} ({guitar.year:<4}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")



main()