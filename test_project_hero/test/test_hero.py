from project_1.hero import Hero

import unittest


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("mario_123", 5, 90.0, 20.0)

    def test_init_hero(self):
        self.assertEqual("mario_123", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(90.0, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_types_attributes(self):
        self.assertTrue(isinstance(self.hero.username, str))
        self.assertTrue(isinstance(self.hero.level, int))
        self.assertTrue(isinstance(self.hero.health, float))
        self.assertTrue(isinstance(self.hero.damage, float))

    def test_battle_method_raises_exception_when_fighting_the_same_username(self):
        enemy_hero = Hero("mario_123", 2, 100.0, 10.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_raises_exception_when_hero_health_is_low(self):
        enemy_hero = Hero("jax_123", 2, 50.0, 10.0)

        self.hero.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_raises_exception_when_enemy_health_is_low(self):
        enemy_hero = Hero("jax_123", 2, -2, 10.0)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight jax_123. He needs to rest", str(ex.exception))

    def test_battle_method_successful(self):
        enemy_hero = Hero("jax_123", 2, 110.0, 10.0)

        self.hero.battle(enemy_hero)

        self.assertEqual(70.0, self.hero.health)
        self.assertEqual(15.0, enemy_hero.health)

    def test_battle_method_when_draw(self):
        enemy_hero = Hero("jax_123", 3, 50.0, 40.0)

        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_battle_method_when_hero_wins(self):
        enemy_hero = Hero("jax_123", 1, 50.0, 10)

        self.assertEqual("You win", self.hero.battle(enemy_hero))

        self.assertEqual(6, self.hero.level)
        self.assertEqual(85.0, self.hero.health)
        self.assertEqual(25.0, self.hero.damage)

    def test_battle_method_when_enemy_wins(self):
        enemy_hero = Hero("jax_123", 4, 120, 30)

        self.assertEqual("You lose", self.hero.battle(enemy_hero))

        self.assertEqual(5, enemy_hero.level)
        self.assertEqual(25.0, enemy_hero.health)
        self.assertEqual(35.0, enemy_hero.damage)

    def test_str_repr_method(self):
        result = "Hero mario_123: 5 lvl\n" \
                 "Health: 90.0\n" \
                 "Damage: 20.0\n"

        self.assertEqual(result, str(self.hero))

if __name__=="__main__":
    unittest.main()






