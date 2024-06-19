from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return

    @speed.setter
    def speed(self, value: int):
        pass

    @abstractmethod
    def train(self):
        pass