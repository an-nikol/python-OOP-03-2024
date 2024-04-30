from project_1.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Maria", "Chimpanzee", "uga-uga")

    def test_init_mammal(self):
        self.assertEqual("Maria", self.mammal.name)
        self.assertEqual("Chimpanzee", self.mammal.type)
        self.assertEqual("uga-uga", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_method(self):
        exp_result = "Maria makes uga-uga"

        self.assertEqual(exp_result, self.mammal.make_sound())

    def test_info_method(self):
        exp_result = "Maria is of type Chimpanzee"

        self.assertEqual(exp_result, self.mammal.info())

if __name__ == "__main__":
    unittest.main()