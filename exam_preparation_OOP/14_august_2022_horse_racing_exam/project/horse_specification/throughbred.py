from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TYPE_ = "Thoroughbred"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if value > Thoroughbred.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        increased_speed = 3
        if self.speed + increased_speed > Thoroughbred.MAX_SPEED:
            self.speed = Thoroughbred.MAX_SPEED
        else:
            self.speed += increased_speed
