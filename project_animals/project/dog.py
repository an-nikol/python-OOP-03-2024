from project_1.animal import Animal


class Dog(Animal):

    @staticmethod
    def make_sound():
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}"