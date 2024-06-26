from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TYPE_ = "Appaloosa"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if value > Appaloosa.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        increased_speed = 2
        if self.speed + increased_speed > Appaloosa.MAX_SPEED:
            self.speed = Appaloosa.MAX_SPEED
        else:
            self.speed += increased_speed