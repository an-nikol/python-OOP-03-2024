from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0  # total income of pastry shop

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_delicacies = {"Gingerbread": Gingerbread, "Stolen": Stolen}

        if self._find_valid_delicacy(name, self.delicacies) is not None:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in valid_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = valid_delicacies[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        valid_booths = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

        if self._find_valid_booth(booth_number, self.booths) is not None:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = valid_booths[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        searched_booth = self._find_the_first_booth_that_is_not_reserved(number_of_people, self.booths)

        if searched_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        searched_booth.reserve(number_of_people)
        return f"Booth {searched_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        searched_booth = self._find_valid_booth(booth_number, self.booths)
        searched_delicacy = self._find_valid_delicacy(delicacy_name, self.delicacies)

        if searched_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if searched_delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        searched_booth.delicacy_orders.append(searched_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        searched_booth = self._find_valid_booth(booth_number, self.booths)

        total_sum_for_all_orders = sum([o.price for o in searched_booth.delicacy_orders])

        booth_bill = searched_booth.price_for_reservation + total_sum_for_all_orders
        self.income += booth_bill

        searched_booth.delicacy_orders.clear()
        searched_booth.is_reserved = False
        searched_booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {booth_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # helper methods
    @staticmethod
    def _find_valid_delicacy(name, collection):
        delicacy = [d for d in collection if d.name == name]
        return delicacy[0] if delicacy else None

    @staticmethod
    def _find_valid_booth(booth_num, collection):
        booth = [b for b in collection if b.booth_number == booth_num]
        return booth[0] if booth else None

    @staticmethod
    def _find_the_first_booth_that_is_not_reserved(num_of_people, collection):
        for b in collection:
            if not b.is_reserved and b.capacity >= num_of_people:
                return b
        else:
            return None
