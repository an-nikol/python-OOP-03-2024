from project_1.animals.animal import Mammal
from project_1.food import Food


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Vegetable" and not food.__class__.__name__ == "Fruit":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Mouse.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"



class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Vegetable" and not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Cat.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

