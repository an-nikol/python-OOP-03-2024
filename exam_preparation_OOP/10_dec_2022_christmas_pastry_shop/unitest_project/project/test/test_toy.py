from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_innit_constructor(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

        self.assertEqual(ToyStore.__base__.__name__, "object")
        self.assertTrue(isinstance(self.toy_store.toy_shelf, dict))

    def test_add_toy_method_raise_exception_when_shelf_not_there(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "doll")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_method_raise_exception_when_toy_already_on_shelf(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "doll")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_method_raise_exception_when_shelf_taken(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "teddy_bear")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_method_happy_path(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}

        result = self.toy_store.add_toy("B", "teddy_bear")

        self.assertEqual(result, f"Toy:teddy_bear placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": "doll", "B": "teddy_bear"})

    def test_remove_toy_raise_exception_when_no_shelf(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("C", "doll")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": "doll", "B": None})

    def test_remove_toy_raise_exception_when_no_toy(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "teddy_bear")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": "doll", "B": None})

    def test_remove_toy_happy_path(self):
        self.toy_store.toy_shelf = {"A": "doll", "B": None}

        result = self.toy_store.remove_toy("A", "doll")

        self.assertEqual(result, f"Remove toy:doll successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {"A": None, "B": None})

if __name__ == "__main__":
    unittest.main()