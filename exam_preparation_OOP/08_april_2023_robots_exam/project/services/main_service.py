from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30
    TYPE_ = "MainService"

    def __init__(self, name: str):
        super().__init__(name, capacity=MainService.CAPACITY)

    def details(self):

        if self.robots:
            robots_names = [r.name for r in self.robots]
            return f"{self.name} Main Service:\nRobots: {' '.join(robots_names)}"
        else:
            return f"{self.name} Main Service:\nRobots: none"
