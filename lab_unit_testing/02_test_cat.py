class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False



import unittest


class TestCat(unittest.TestCase):

    def setUp(self) -> None:
        # Arrange
        self.cat = Cat("Trisha")

    def test_cat_initializer(self):
        self.assertEqual(self.cat.name, "Trisha")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_cat_eating(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

        # Act
        self.cat.eat()

        # Assert
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, 1)

    def test_cat_eating_when_already_fed(self):

        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_sleeping_when_fed(self):
        # feed the cat
        self.cat.eat()

        # cat goes to sleep
        self.cat.sleep()

        # cat successfully is asleep
        self.assertFalse(self.cat.sleepy)

    def test_cat_not_sleeping_when_not_fed(self):

        # cat goes to sleep without being fed
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

if __name__ == "__main__":
    unittest.main()


