from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity # per km
        self.fuel_consumption = fuel_consumption # per km

    def drive(self, distance: int):
        consumption = (Car.FUEL_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        consumption = (Truck.FUEL_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
