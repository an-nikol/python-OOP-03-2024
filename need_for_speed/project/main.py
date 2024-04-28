from project_1.car import Car
from project_1.cross_motorcycle import CrossMotorcycle
from project_1.family_car import FamilyCar
from project_1.motorcycle import Motorcycle
from project_1.race_motorcycle import RaceMotorcycle
from project_1.sport_car import SportCar
from project_1.vehicle import Vehicle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
