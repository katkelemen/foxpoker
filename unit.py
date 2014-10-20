# -*- coding: utf8 -*-
import unittest
import poker

class TestPoker(unittest.TestCase):

####################################

    def test_hand_length(self):
        self.assertTrue( poker.is_valid_hand(["AS","7S","7H","10C","JD"]) )
        self.assertFalse( poker.is_valid_hand(["AS","7S","7H"]) )

    def test_valid_card(self):
        self.assertTrue( poker.is_valid_card("AS") )
        self.assertFalse( poker.is_valid_card("1S") )
        self.assertFalse( poker.is_valid_card("AK") )

    def test_valid_hand(self):
        self.assertFalse( poker.is_valid_hand(["AS","7M","7H","10C","JD"]))
        self.assertFalse( poker.is_valid_hand(["AS","7S","AS","10C","JD"]))

    def test_bigger_card(self):
        self.assertTrue( poker.is_bigger_card("KC", "QD"))
        self.assertFalse( poker.is_bigger_card("QD", "KC"))

    def test_highcard(self):
        self.assertFalse(poker.is_bigger_hand(
            ["2S","3S","4S","6C","7D"],
            ["2S","3S","4S","6C","KD"]))
        self.assertTrue(poker.is_bigger_hand(
            ["2S","3S","4S","6C","KD"],
            ["2S","3S","4S","6C","7D"]))

    def test_one_pair(self):
        self.assertTrue(poker.get_pair(["2S","3S","3D","6C","7D"]))
        self.assertTrue(poker.is_bigger_hand(
            ["2S","3S","3D","6C","7D"],
            ["2S","3S","4S","6C","KD"]))

    def test_highest_card(self):
        self.assertTrue(poker.get_highest_card(["AS","7M","7H","10C","JD"])=="AS")
        self.assertTrue(poker.get_highest_card(["2S","7M","7H","10C","JD"])=="JD")

    def test_partition(self):
        self.assertEqual(poker.get_highest_card(["AS","AD","AC","10C","10D"]),
            [["AS","AD","AC"],["10C","10D"]])

####################################

if __name__ == '__main__':
    unittest.main()