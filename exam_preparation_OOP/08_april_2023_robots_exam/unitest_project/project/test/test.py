from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Grigor", 30, 100.0)

    def test_init_constructor(self):
        self.assertEqual(self.tennis_player.name, "Grigor")
        self.assertEqual(self.tennis_player.age, 30)
        self.assertEqual(self.tennis_player.points, 100.0)
        self.assertEqual(self.tennis_player.wins, [])

    def test_invalid_name_raise_exception_2_letters(self):

        with self.assertRaises(ValueError) as ex:
            invalid_tennis_player = TennisPlayer("Gr", 30, 100.0)

        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")


    def test_invalid_age_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            invalid_tennis_player = TennisPlayer("Grigor", 17, 100.0)

        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_invalid_adding_win_which_already_exist(self):
        self.tennis_player.wins = ["Wimbledon"]

        invalid_tour_name = "Wimbledon"
        result = self.tennis_player.add_new_win(invalid_tour_name)

        self.assertEqual(result, f"{invalid_tour_name} has been already added to the list of wins!")

    def test_add_win_happy_path(self):
        self.assertEqual(self.tennis_player.wins, [])

        valid_tour_name = "Wimbledon"
        self.tennis_player.add_new_win(valid_tour_name)

        self.assertEqual(self.tennis_player.wins, ["Wimbledon"])

    def test_lt_first_player_has_less_points_than_second_player(self):
        tennis_player_1 = TennisPlayer("Alcaras", 30, 100.0)
        tennis_player_2 = TennisPlayer("Medveded", 30, 120.0)

        result = tennis_player_1 < tennis_player_2

        self.assertEqual(result, f'{tennis_player_2.name} is a top seeded player and he/she is better than {tennis_player_1.name}')


    def test_lt_first_player_has_more_points_than_second_player(self):
        tennis_player_1 = TennisPlayer("Alcaras", 30, 120.0)
        tennis_player_2 = TennisPlayer("Medveded", 30, 100.0)

        result = tennis_player_1 < tennis_player_2
        self.assertEqual(result, f'{tennis_player_1.name} is a better player than {tennis_player_2.name}')

    def test_str_method_no_wins(self):
        result = str(self.tennis_player)

        self.assertEqual(result, f"Tennis Player: {self.tennis_player.name}\n"
                                 f"Age: {self.tennis_player.age}\n"
                                 f"Points: {self.tennis_player.points:.1f}\n"
                                 f"Tournaments won: {', '.join(self.tennis_player.wins)}")

    def test_str_method_one_win(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023')

    def test__str__two_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023', 'FO 2022']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023, FO 2022')

if __name__ == "__main__":
    unittest.main()