"""
CP1404/CP5602 Practical - Suggested Solution
Taxi simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi
from prac_09.car import Car


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Write a taxi simulator program that uses your Taxi and Silver
    classes. Each time, until they quit:
    The user should be presented with a list of available taxis and
    choose one. Then they should say how far they want to drive.
    At the end of each trip, show them the price and add it to the
    """
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = ""
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif menu_choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    """Drive a taxi option"""
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def choose_taxi(current_taxi, taxis):
    """Select a taxi option"""
    print("Taxis available: ")
    display_taxis(taxis)
    # no error-checking
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Display numbered list of taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i+1} - {taxi}")


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)

main()


