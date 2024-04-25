class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class TestWorker(unittest.TestCase):

    def test_initializer(self):
        # Arrange & Act
        worker = Worker("James", 1000, 50)

        # Assert
        self.assertEqual(worker.name, "James")
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 50)
        self.assertEqual(worker.money, 0)

    def test_work_method_when_money_and_energy_is_increased(self):
        # Arrange
        # state before calling def work
        worker = Worker("James", 1000, 50)
        self.assertEqual(worker.name, "James")
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 50)
        self.assertEqual(worker.money, 0)

        # Act
        # calling the work method
        worker.work()

        # Assert
        # state after calling the work method
        self.assertEqual(worker.money, 1000)
        self.assertEqual(worker.energy, 49)

        # calling the work method again
        worker.work()

        # checking if it is incremented correctly
        self.assertEqual(worker.money, 2000)
        self.assertEqual(worker.energy, 48)

    def test_work_method_when_energy_is_negative(self):
        # Assert
        # state before def work
        worker = Worker("James", 1000, -1)
        self.assertEqual(worker.name, "James")
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, -1)
        self.assertEqual(worker.money, 0)


        # calling the work method
        with self.assertRaises(Exception) as ex:
            # Act
            worker.work()

        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_method_and_adding_energy(self):
        # Arrange
        worker = Worker("James", 1000, 5)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(worker.energy, 6)

    def test_get_info_method(self):
        # Arrange
        worker = Worker("James", 1000, 5)

        # Act and Assert
        self.assertEqual(worker.get_info(), f'James has saved 0 money.')

        worker.work()

        self.assertEqual(worker.get_info(), f'James has saved 1000 money.')

if __name__ == '__main__':
    unittest.main()

