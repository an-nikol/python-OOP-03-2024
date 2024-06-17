from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, time_to_catch=DeepSeaFish.TIME_TO_CATCH)

    def fish_details(self):
        return f"{__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {DeepSeaFish.TIME_TO_CATCH} seconds]"
