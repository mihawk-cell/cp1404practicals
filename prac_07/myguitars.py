from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of programming language details and display."""
    guitars = read_file(FILENAME)
    # Loop through and display all guitar (using their str method
    for guitar in guitars:
        guitars.sort()
        print(guitar)

    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    price = float(input("Enter price: "))
    write_to_file(name, price, year)


def read_file(filename):
    """Get data from external file."""
    guitars = []
    in_file = open(filename, 'r')
    # File format is like: Guitar, name, year, price
    # 'Consume' the first line (header) - we don't need its cont
    # in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line)) # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts) # debugging
        # Construct a Guitar object using the elements
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the guitar we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    return guitars


def write_to_file(name, price, year):
    """Add date to the external file"""
    with open(FILENAME, 'a') as f:
        f.write(f"{name},{price},{year}\n")

if __name__ == "__main__":
    main()

