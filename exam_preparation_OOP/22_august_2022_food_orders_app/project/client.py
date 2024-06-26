from typing import List
from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []  # added by the client
        self.bill: float = 0.0  # total amount of money for all means that the client had added to the shopping cart
        self.ordered_meals = {} #?


    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not value[0] == "0" or not len(value) == 10 or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value



