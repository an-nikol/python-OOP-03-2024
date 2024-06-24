from project.truck_driver import TruckDriver

import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Bob", 20.0)

    def test_init_constructor(self):
        self.assertEqual(self.truck_driver.name, "Bob")
        self.assertEqual(self.truck_driver.money_per_mile, 20.0)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0.0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.truck_driver.earned_money = -1

        self.assertEqual(str(ex.exception), f"{self.truck_driver.name} went bankrupt.")

    def test_add_cargo_method_when_location_already_in_available_cargos(self):
        self.truck_driver.available_cargos = {"Serbia": 100}

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Serbia", 100)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_method_successful(self):
        self.assertEqual(self.truck_driver.available_cargos, {})

        result = self.truck_driver.add_cargo_offer("Serbia", 100)

        self.assertEqual(result, "Cargo for 100 to Serbia was added as an offer.")
        self.assertEqual(self.truck_driver.available_cargos, {"Serbia": 100})

    def test_drive_best_cargo_offer_successful(self):
        self.truck_driver.available_cargos = {"Serbia": 250, "Macedonia": 50}

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.truck_driver.name} is driving 250 to Serbia.")
        self.assertEqual(self.truck_driver.earned_money, 4980)
        self.assertEqual(self.truck_driver.miles, 250)


    def test_drive_best_cargo_offer_returns_msg_when_value_error(self):
        self.assertEqual(self.truck_driver.available_cargos, {})

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, "There are no offers available.")

    def test_check_for_activities_eating_method(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.check_for_activities(250)
        self.assertEqual(self.truck_driver.earned_money, 1980)

    def test_check_for_activities_sleeping_method(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.check_for_activities(1000)
        self.assertEqual(self.truck_driver.earned_money, 1875)

    def test_check_for_activities_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.check_for_activities(1500)
        self.assertEqual(self.truck_driver.earned_money, 1335)

    def test_check_for_repair_truck(self):
        self.truck_driver.earned_money = 100_000

        self.truck_driver.check_for_activities(10_000)
        self.assertEqual(self.truck_driver.earned_money, 88_250)

    def test_repr_method(self):
        result = repr(self.truck_driver)

        self.assertEqual(result, f"{self.truck_driver.name} has {self.truck_driver.miles} miles behind his back.")

if __name__ == "__main__":
    unittest.main()