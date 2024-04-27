class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest

class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_car_init(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_make_method_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car = Car("", "GT-R", 15, 75)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))


    def test_model_method_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "", 15, 75)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "GT-R", 0, 75)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car = Car("Nissan", "GT-R", 15, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_method_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_method_refuel_adds_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_method_when_fuel_amount_is_more_than_fuel_capacity(self):
        self.car.refuel(80)

        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_with_valid_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(73.5, self.car.fuel_amount)

    def test_drive_car_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))



if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
