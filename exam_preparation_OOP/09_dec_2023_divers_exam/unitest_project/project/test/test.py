from collections import deque

from project.railway_station import RailwayStation
import unittest


class TestRailwayStation(unittest.TestCase):
    pass

    def setUp(self) -> None:
        self.station = RailwayStation("Sofia Station")

    def test_station_structure(self):
        self.assertEqual(RailwayStation.__base__.__name__, "object")
        self.assertTrue(hasattr(RailwayStation, "new_arrival_on_board"))
        self.assertTrue(hasattr(RailwayStation, "train_has_arrived"))
        self.assertTrue(hasattr(RailwayStation, "train_has_left"))

    def test_station_init(self):
        self.station.arrival_trains = deque(["Burgas", "Varna"])
        self.station.departure_trains = deque(["Sofia", "Plovdiv"])

        # check the name attribute
        self.assertEqual("Sofia Station", self.station.name)

        # check the type of of the arrival_trains and departure_trains attributes
        self.assertTrue(isinstance(self.station.arrival_trains, deque))
        self.assertTrue(isinstance(self.station.departure_trains, deque))

        # check if the values are the same
        self.assertEqual(deque(["Burgas", "Varna"]), self.station.arrival_trains)
        self.assertEqual(deque(["Sofia", "Plovdiv"]), self.station.departure_trains)

    def test_station_name_setter_raises_exception_one_char_name(self):
        invalid_name = "S"

        with self.assertRaises(ValueError) as ex:
            self.station.name = invalid_name

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_station_name_setter_raises_exception_empty_string(self):
        invalid_name = ""

        with self.assertRaises(ValueError) as ex:
            self.station.name = invalid_name

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_station_name_setter_raises_exception_edge(self):
        invalid_name = "Kik"

        with self.assertRaises(ValueError) as ex:
            self.station.name = invalid_name

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_station_name_setter_successful(self):
        valid_name = "Varna Station"

        self.station.name = valid_name

        self.assertEqual("Varna Station", self.station.name)

    def test_station_name_setter_with_exact_chars(self):
        valid_name = "Kika"

        self.station.name = valid_name

        self.assertEqual("Kika", self.station.name)

    def test_method_new_arrival_on_board(self):
        self.station.arrival_trains = deque(["Burgas"])

        train_info = "Karlovo"
        self.assertTrue(isinstance(train_info, str))

        self.station.new_arrival_on_board(train_info)

        self.assertEqual(deque(["Burgas", "Karlovo"]), self.station.arrival_trains)

    def test_method_train_has_arrived(self):
        self.station.arrival_trains = deque(["Burgas"])

        train_info = "Karlovo"
        self.assertTrue(isinstance(train_info, str))

        expected_return_msg = self.station.train_has_arrived(train_info)
        self.assertEqual(expected_return_msg, f"There are other trains to arrive before {train_info}.")

    def test_method_train_has_arrived_trains_on_platform_one_train(self):
        self.station.arrival_trains = deque(["Burgas"])
        self.station.departure_trains = deque([])

        train_info = "Burgas"
        self.assertTrue(isinstance(train_info, str))

        expected_return_msg = self.station.train_has_arrived(train_info)

        self.assertEqual(expected_return_msg, f"{train_info} is on the platform and will leave in 5 minutes.")

        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque(["Burgas"]), self.station.departure_trains)

    def test_method_train_has_arrived_trains_on_platform_multiple_trains(self):
        self.station.arrival_trains = deque(["Burgas", "Varna"])
        self.station.departure_trains = deque([])

        train_info = "Burgas"
        self.assertTrue(isinstance(train_info, str))

        expected_return_msg = self.station.train_has_arrived(train_info)

        self.assertEqual(expected_return_msg, f"{train_info} is on the platform and will leave in 5 minutes.")

        self.assertEqual(deque(["Varna"]), self.station.arrival_trains)
        self.assertEqual(deque(["Burgas"]), self.station.departure_trains)

    def test_train_has_left_return_true(self):
        self.station.departure_trains = deque(["Blagoevgrad"])

        train_info = "Blagoevgrad"
        self.assertTrue(isinstance(train_info, str))

        self.assertTrue(self.station.train_has_left(train_info))

        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_har_left_true_multiple_trains(self):
        self.station.departure_trains = deque(["Blagoevgrad", "Simitli"])

        train_info = "Blagoevgrad"
        self.assertTrue(isinstance(train_info, str))

        self.assertTrue(self.station.train_has_left(train_info))

        self.assertEqual(deque(["Simitli"]), self.station.departure_trains)

    def test_train_has_left_returns_false(self):
        self.station.departure_trains = deque(["Blagoevgrad", "Simitli"])

        train_info = "Karlovo"
        self.assertTrue(isinstance(train_info, str))

        self.assertFalse(self.station.train_has_left(train_info))

        self.assertEqual(deque(["Blagoevgrad", "Simitli"]), self.station.departure_trains)


if __name__ == "__main__":
    unittest.main()