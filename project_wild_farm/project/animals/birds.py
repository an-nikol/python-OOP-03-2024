from project_1.animals.animal import Bird
from project_1.food import Food


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

