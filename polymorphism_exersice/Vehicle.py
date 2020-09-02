'''
Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles that
inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both have
fuel_quantity, fuel_consumption in liters per km and can be driven a given distance: drive(distance) and refueled
with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air conditioners and their fuel
consumption per km when driving is increased by 0.9 liters for the car and with 1.6 liters for the truck. Also, the
Truck has a tiny hole in its tank and when it's refueled it keeps only 95% of the given fuel. The car has no problems
and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.
'''

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        result = (self.fuel_consumption + 0.9) * distance
        if result < self.fuel_quantity:
            self.fuel_quantity -= result

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        result = (self.fuel_consumption + 1.6) * distance
        if result < self.fuel_quantity:
            self.fuel_quantity -= result

    def refuel(self, fuel):
        fuel *= 0.95
        self.fuel_quantity += fuel


if __name__ == '__main__':
    car = Car(20, 5)
    car.drive(3)
    print(car.fuel_quantity)
    car.refuel(10)
    print(car.fuel_quantity)
    print('-'*20)
    truck = Truck(100, 15)
    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)
    print('-'*20)

    car_one = Car(150, 6)
    car_two = Car(150, 6)
    car_one.drive(15)
    car_two.drive(50)
    print(car_one.fuel_quantity)
    print(car_two.fuel_quantity)