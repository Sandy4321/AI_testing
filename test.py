from source import *
import unittest

class Test_source(unittest.TestCase):

    def test_remind_Rock_Hyrax(self):
        self.assertFalse(remind_Rock_Hyrax(43, 35, 6, 9, 67))
    def test_end_Toucan(self):
        self.assertFalse(end_Toucan(1))
    def test_post_Chinchilla(self):
        self.assertTrue(post_Chinchilla(28, 63, 71, 50, 66))
    def test_apologise_Cross_River_Gorilla(self):
        self.assertFalse(apologise_Cross_River_Gorilla(27, 98))
    def test_worry_Appenzeller_Dog(self):
        self.assertTrue(worry_Appenzeller_Dog(37))
    def test_rescue_Akbash(self):
        self.assertEqual(rescue_Akbash(55, 17), 58)
    def test_flash_Woodpecker(self):
        self.assertTrue(flash_Woodpecker(16, 5, 63, 79, 15))
    def test_risk_Eastern_Lowland_Gorilla(self):
        self.assertFalse(risk_Eastern_Lowland_Gorilla(76, 57, 54, 90, 62))
    def test_scribble_Pike(self):
        self.assertTrue(scribble_Pike(61, 23))
    def test_rule_Scorpion(self):
        self.assertTrue(rule_Scorpion(55, 54, 97, 68, 9))
    def test_raise_Aardvark(self):
        self.assertFalse(raise_Aardvark(57, 56, 26))
    def test_kill_Stoat(self):
        self.assertTrue(kill_Stoat(3, 57))
    def test_rule_Magpie(self):
        self.assertFalse(rule_Magpie(62, 71))
    def test_accept_Squirrel_Monkey(self):
        self.assertFalse(accept_Squirrel_Monkey(99, 85, 37, 89, 91))
    def test_protect_Bloodhound(self):
        self.assertFalse(protect_Bloodhound(8, 93))
    def test_perform_Akbash(self):
        self.assertFalse(perform_Akbash(78, 64))
    def test_bore_Giraffe(self):
        self.assertTrue(bore_Giraffe(99, 59, 54))
    def test_mine_Wolf(self):
        self.assertTrue(mine_Wolf(97))
    def test_start_Gharial(self):
        self.assertTrue(start_Gharial(19, 52, 59))
    def test_cycle_Grouse(self):
        self.assertEqual(cycle_Grouse(48), 3)
if __name__=="__main__":
    unittest.main()