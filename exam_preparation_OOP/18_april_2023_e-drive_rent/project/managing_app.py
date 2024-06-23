from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    @staticmethod
    def _find_user(exp_driving_num, collection):
        user = [u for u in collection if u.driving_license_number == exp_driving_num]
        return user

    @staticmethod
    def _find_vehicle(exp_plate_num, collection):
        vehicle = [v for v in collection if v.license_plate_number == exp_plate_num]
        return vehicle

    @staticmethod
    def _find_route(exp_start, exp_end, exp_length, collection):
        for r in collection:
            if r.start_point == exp_start and r.end_point == exp_end and r.length == exp_length:
                return r

    @staticmethod
    def _find_shorter_route(exp_start, exp_end, exp_length, collection):
        for r in collection:
            if r.start_point == exp_start and r.end_point == exp_end and r.length < exp_length:
                return r

    @staticmethod
    def _find_longer_route(exp_start, exp_end, exp_length, collection):
        for r in collection:
            if r.start_point == exp_start and r.end_point == exp_end and r.length > exp_length:
                return r

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._find_user(driving_license_number, self.users):
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

        if vehicle_type not in valid_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._find_vehicle(license_plate_number, self.vehicles):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = valid_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        if self._find_route(start_point, end_point, length, self.routes):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if self._find_shorter_route(start_point, end_point, length, self.routes):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        longer_route = self._find_longer_route(start_point, end_point, length, self.routes)
        if longer_route:
            longer_route.is_locked = True

        created_route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, created_route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        curr_user = self._find_user(driving_license_number, self.users)[0]
        curr_vehicle = self._find_vehicle(license_plate_number, self.vehicles)[0]
        curr_route = [r for r in self.routes if r.route_id == route_id][0]

        if curr_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if curr_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if curr_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        if is_accident_happened:
            curr_vehicle.is_damaged = True
            curr_user.decrease_rating()
        else:
            curr_user.increase_rating()

        curr_vehicle.drive(curr_route.length)

        return str(curr_vehicle)

    def repair_vehicles(self, count: int):
        all_damaged_vehicles = [v for v in self.vehicles if v.is_damaged]

        sorted_vehicles = sorted(all_damaged_vehicles, key=lambda v: (v.brand, v.model))

        if len(all_damaged_vehicles) > count:
            counted_vehicles = sorted_vehicles[:count]
            for v in counted_vehicles:
                v.is_damaged = False
                v.recharge()
            return f"{len(counted_vehicles)} vehicles were successfully repaired!"

        else:
            for v in all_damaged_vehicles:
                v.is_damaged = False
                v.recharge()
            return f"{len(all_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        output = ["*** E-Drive-Rent ***"]

        for user in sorted_users:
            output.append(str(user))

        return '\n'.join(output)