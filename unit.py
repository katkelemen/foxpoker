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
        self.assertTrue( poker.is_bigger("KC", "QD"))
        self.assertFalse( poker.is_bigger("QD", "KC"))

    def test_is_bigger_hand(self):
        self.assertTrue(poker.is_bigger_hand)
####################################

if __name__ == '__main__':
    unittest.main()