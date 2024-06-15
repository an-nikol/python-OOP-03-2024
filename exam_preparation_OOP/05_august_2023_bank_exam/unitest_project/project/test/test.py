from project.second_hand_car import SecondHandCar

import unittest

class TestSecondHandCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("BMW", "X-5", 1000, 5000.00)

    def test_structure(self):
        self.assertEqual(SecondHandCar.__base__.__name__, "object")
        self.assertTrue(hasattr(SecondHandCar, "set_promotional_price"))
        self.assertTrue(hasattr(SecondHandCar, "need_repair"))
        self.assertTrue(hasattr(SecondHandCar, "__gt__"))
        self.assertTrue(hasattr(SecondHandCar, "__str__"))

    def test_init_types(self):
        self.assertTrue(isinstance(self.car.model, str))
        self.assertTrue(isinstance(self.car.car_type, str))
        self.assertTrue(isinstance(self.car.mileage, int))
        self.assertTrue(isinstance(self.car.price, float))
        self.assertTrue(isinstance(self.car.repairs, list))

    def test_init_constructor(self):
        self.assertEqual(self.car.model, "BMW")
        self.assertEqual(self.car.car_type, "X-5")
        self.assertEqual(self.car.mileage, 1000)
        self.assertEqual(self.car.price, 5000.00)
        self.assertEqual(self.car.repairs, [])

    def test_price_raises_exception_less_than_0(self):

        with self.assertRaises(ValueError) as ex:
            self.car.price = -2.00

        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_price_raises_exception_equal_to_1(self):

        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.00

        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_mileage_raises_exception_less_than_100(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 99

        self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_mileage_raises_exception_equal_to_100(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100

        self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_method_set_promotional_price_raise_exception_when_new_price_more_than_current_price(self):
        invalid_price = 5500.00

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(invalid_price)

        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_method_set_promotional_price_raise_exception_when_new_price_equal_to_current_price(self):
        invalid_price = 5000.00

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(invalid_price)

        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_method_set_promotional_price_happy_path(self):
        self.assertEqual(self.car.price, 5000.00)

        valid_price = 4500.00

        returned_msg = self.car.set_promotional_price(valid_price)

        self.assertEqual(returned_msg, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 4500.00)

    def test_method_need_repair_when_repair_price_is_excessive(self):

        invalid_repair_price = 3000.00
        repair_description = "Engine repair"

        returned_msg = self.car.need_repair(invalid_repair_price, repair_description)

        self.assertEqual('Repair is impossible!', returned_msg)

    def test_method_need_repair_less_than_half_price(self):
        self.assertEqual(self.car.price, 5000.00)
        self.assertEqual(len(self.car.repairs), 0)
        self.assertEqual(self.car.repairs, [])

        valid_repair_price = 1500.00
        repair_description = "Engine repair"

        returned_msg = self.car.need_repair(valid_repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", returned_msg)

        self.assertEqual(self.car.price, 6500.00)
        self.assertEqual(self.car.repairs, ["Engine repair"])
        self.assertEqual(len(self.car.repairs), 1)

    def test_need_repair_happy_case__two_repairs_less_half_priced(self):
        self.assertEqual(self.car.price, 5000.00)
        self.assertEqual(self.car.repairs, [])

        valid_repair_price = 1500.00
        repair_description = "Engine repair"

        returned_msg = self.car.need_repair(valid_repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", returned_msg)

        self.assertEqual(self.car.price, 6500.00)
        self.assertEqual(self.car.repairs, ["Engine repair"])
        self.assertEqual(len(self.car.repairs), 1)

        valid_repair_price = 1000.00
        repair_description = "Oil change"

        returned_msg = self.car.need_repair(valid_repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", returned_msg)

        self.assertEqual(self.car.price, 7500.00)
        self.assertEqual(self.car.repairs, ["Engine repair", "Oil change"])

    def test_method_need_repair_equal_to_half_price(self):
        self.assertEqual(self.car.price, 5000.00)
        self.assertEqual(len(self.car.repairs), 0)
        self.assertEqual(self.car.repairs, [])

        valid_repair_price = 2500.00
        repair_description = "Engine repair"

        returned_msg = self.car.need_repair(valid_repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", returned_msg)

        self.assertEqual(self.car.price, 7500.00)
        self.assertEqual(self.car.repairs, ["Engine repair"])
        self.assertEqual(len(self.car.repairs), 1)

    def test__gt__happy_case(self):
        self.car1 = SecondHandCar('test model', 'test type', 101, 2)
        self.car2 = SecondHandCar('test model2', 'test type', 101, 3)

        self.assertFalse(self.car1 > self.car2)
        self.assertTrue(self.car2 > self.car1)

    def test__gt__type_mismatch(self):
        self.car1 = SecondHandCar('test model', 'test type1', 101, 2)
        self.car2 = SecondHandCar('test model2', 'test type2', 101, 3)

        self.assertEqual(self.car1 > self.car2, "Cars cannot be compared. Type mismatch!")

    def test_str_method(self):
        self.assertEqual(
            str(self.car), f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        )

if __name__ == "__main__":
    unittest.main()