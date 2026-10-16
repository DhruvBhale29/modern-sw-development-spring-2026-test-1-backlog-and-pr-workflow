
import unittest
import boss_mini


class TestBossCombat(unittest.TestCase):

    def test_attack_reduces_boss_hp(self):
        boss_mini.b_hp = 50
        boss_mini.attack()
        self.assertEqual(boss_mini.b_hp, 40)

    def test_attack_cannot_make_hp_negative(self):
        boss_mini.b_hp = 5
        boss_mini.attack()
        self.assertEqual(boss_mini.b_hp, 0)


if __name__ == "__main__":
    unittest.main()
