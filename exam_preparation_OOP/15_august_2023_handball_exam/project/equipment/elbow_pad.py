from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0
    PRICE_INCREASING = 0.10
    TYPE_ = "ElbowPad"

    def __init__(self):
        super().__init__(protection=ElbowPad.PROTECTION, price=ElbowPad.PRICE)

    def increase_price(self):
        self.price += self.price * ElbowPad.PRICE_INCREASING