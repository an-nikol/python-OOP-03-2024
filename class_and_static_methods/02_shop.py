from typing import Dict


class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str: int] = {} # stores the name of the item and its qty

    @classmethod
    def small_shop(cls, name: str, type_shop: str): # from __feature__ import annotations
        return cls(name, type_shop, capacity=10)

    def add_item(self, item_name: str) -> str:
        if sum(self.items.values()) < self.capacity:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if (item_name in self.items) and self.items[item_name] - amount >= 0:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"



