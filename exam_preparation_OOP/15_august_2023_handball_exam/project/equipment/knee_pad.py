from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0
    PRICE_INCREASING = 0.20
    TYPE_ = "KneePad"

    def __init__(self):
        super().__init__(protection=KneePad.PROTECTION, price=KneePad.PRICE)

    def increase_price(self):
        self.price += self.price * KneePad.PRICE_INCREASING

