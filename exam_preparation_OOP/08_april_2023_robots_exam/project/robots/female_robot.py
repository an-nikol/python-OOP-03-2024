from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7
    KILOGRAMS_INCREASING = 1
    SUITABLE_SERVICE = "SecondaryService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=FemaleRobot.INITIAL_WEIGHT)

    def eating(self):
        self.weight += FemaleRobot.KILOGRAMS_INCREASING

