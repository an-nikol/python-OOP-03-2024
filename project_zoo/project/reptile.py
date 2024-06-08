from project_1.animal import Animal


class Reptile(Animal):
    def __init__(self, name: str):
        super().__init__(name)