from project_1.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Male")

    @staticmethod
    def make_sound():
        return "Hiss"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}"

