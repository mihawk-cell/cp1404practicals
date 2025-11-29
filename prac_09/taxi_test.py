
from prac_09.taxi import Taxi


def main():
    """Test Taxi class"""
    my_taxi = Taxi("Pruis 1", 100) # Create a new taxi
    my_taxi.drive(40) # Drive the taxi 40 km
    print(my_taxi) # Print the taxi's details
    print(my_taxi.get_fare()) # Print the taxi the current fare

    print()
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(my_taxi.get_fare())


main()