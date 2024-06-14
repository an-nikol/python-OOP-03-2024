from project_1.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(20.00, 55.00)

    def test_init_vehicle(self):
        self.assertEqual(20.00, self.vehicle.fuel)
        self.assertEqual(20.00, self.vehicle.capacity)
        self.assertEqual(55.00, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attribute_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))

    def test_drive_successful(self):
        self.vehicle.drive(5)
        self.assertEqual(13.75, self.vehicle.fuel)

    def test_drive_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(25)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_method_successful(self):
        self.vehicle.fuel = 1

        self.vehicle.refuel(5)

        self.assertEqual(6, self.vehicle.fuel)

    def test_refuel_method_exception_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_repr_method(self):
        result = "The vehicle has 55.0 horse power with 20.0 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, str(self.vehicle))