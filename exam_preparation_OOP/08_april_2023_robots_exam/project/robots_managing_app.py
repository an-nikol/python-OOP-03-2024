from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @staticmethod
    def _find_robot(name, collection):
        robot = [r for r in collection if r.name == name]
        return robot[0]

    @staticmethod
    def _find_service(name, collection):
        service = [s for s in collection if s.name == name]
        return service[0]

    def add_service(self, service_type: str, name: str):
        valid_services = {"MainService": MainService, "SecondaryService": SecondaryService }

        if service_type not in valid_services:
            raise Exception("Invalid service type!")

        new_service = valid_services[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robots = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

        if robot_type not in valid_robots:
            raise Exception("Invalid robot type!")

        new_robot = valid_robots[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        curr_robot = self._find_robot(robot_name, self.robots)
        curr_service = self._find_service(service_name, self.services)

        if len(curr_service.robots) >= curr_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        if curr_robot.SUITABLE_SERVICE != curr_service.TYPE_:
            return f"Unsuitable service."

        curr_service.robots.append(curr_robot)
        self.robots.remove(curr_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        curr_service = self._find_service(service_name, self.services)

        for r in curr_service.robots:
            if r.name == robot_name:
                self.robots.append(r)
                curr_service.robots.remove(r)
                return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        curr_service = self._find_service(service_name, self.services)
        [r.eating() for r in curr_service.robots]

        return f"Robots fed: {len(curr_service.robots)}."

    def service_price(self, service_name: str):
        curr_service = self._find_service(service_name, self.services)
        total_sum = sum([r.price for r in curr_service.robots])

        return f"The value of service {service_name} is {total_sum:.2f}."

    def __str__(self):
        output = []

        for s in self.services:
            output.append(s.details())

        return '\n'.join(output)
