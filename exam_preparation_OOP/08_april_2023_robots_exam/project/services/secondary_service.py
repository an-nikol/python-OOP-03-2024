from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15
    TYPE_ = "SecondaryService"

    def __init__(self, name: str):
        super().__init__(name, capacity=SecondaryService.CAPACITY)

    def details(self):
        if self.robots:
            robots_names = [r.name for r in self.robots]
            return f"{self.name} Secondary Service:\nRobots: {' '.join(robots_names)}"
        else:
            return f"{self.name} Secondary Service:\nRobots: none"

