from source import *
import unittest

class Test_source(unittest.TestCase):

    def test_crawl_Butterfly_Fish(self):
        self.assertFalse(crawl_Butterfly_Fish(63, 19, 20))
    def test_unlock_Common_Toad(self):
        self.assertFalse(unlock_Common_Toad(96, 61, 67))
    def test_fill_Airedale_Terrier(self):
        self.assertFalse(fill_Airedale_Terrier(62, 55, 82, 9))
    def test_invite_Banded_Palm_Civet(self):
        self.assertFalse(invite_Banded_Palm_Civet(55, 74))
    def test_strengthen_Okapi(self):
        self.assertFalse(strengthen_Okapi(35))
    def test_protect_Gar(self):
        self.assertNotEqual(protect_Gar(4, 29, 78, 56, 33), 0)
    def test_expect_Gecko(self):
        self.assertFalse(expect_Gecko(64, 78, 30, 60, 98))
    def test_expand_Snowy_Owl(self):
        self.assertEqual(expand_Snowy_Owl(82, 81), 51)
    def test_love_Wallaby(self):
        self.assertEqual(love_Wallaby(91), 86)
    def test_serve_Wrasse(self):
        self.assertTrue(serve_Wrasse(37, 60, 39, 77, 9))
    def test_slap_Okapi(self):
        self.assertFalse(slap_Okapi(40, 90))
    def test_shave_Turkish_Angora(self):
        self.assertTrue(shave_Turkish_Angora(62, 35, 12, 100, 59))
    def test_list_Spadefoot_Toad(self):
        self.assertNotEqual(list_Spadefoot_Toad(49, 50), 0)
    def test_bounce_Sea_Lion(self):
        self.assertNotEqual(bounce_Sea_Lion(100, 72), 0)
    def test_prefer_Goose(self):
        self.assertFalse(prefer_Goose(26))
    def test_rob_Sea_Lion(self):
        self.assertFalse(rob_Sea_Lion(8))
    def test_introduce_Okapi(self):
        self.assertNotEqual(introduce_Okapi(70), 0)
    def test_trouble_Eastern_Lowland_Gorilla(self):
        self.assertTrue(trouble_Eastern_Lowland_Gorilla(59, 24, 17, 43, 27))
    def test_harass_Moorhen(self):
        self.assertTrue(harass_Moorhen(94, 0))
    def test_beam_French_Bulldog(self):
        self.assertFalse(beam_French_Bulldog(83, 70, 6))
if __name__=="__main__":
    unittest.main()