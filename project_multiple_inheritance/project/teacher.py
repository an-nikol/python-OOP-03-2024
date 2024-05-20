from project_1.employee import Employee
from project_1.person import Person


class Teacher(Person, Employee):

    def teach(self) -> str:
        return "teaching..."