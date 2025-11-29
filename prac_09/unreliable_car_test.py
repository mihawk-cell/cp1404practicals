
from prac_09.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Audi", 100, 90)

    print(f"{car.name:4} drove {car.drive(150):2}km.")

main()