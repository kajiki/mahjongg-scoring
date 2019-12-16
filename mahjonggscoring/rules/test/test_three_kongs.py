import unittest2
from mahjonggscoring.rules import ThreeKongs
from mahjonggscoring import Hand

class TestThreeKongs(unittest2.TestCase):
	def setUp(self):
		data = [["W", "W", "W", "W"], ["8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data)
		self.examination = ThreeKongs(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 32)
		
class TestNotThreeKongs(unittest2.TestCase):
	def test_not_three_kongs(self):
		data = [["1#", "2#", "3#"], ["1#", "2#", "3#"], ["1#", "2#", "3#"], ["1#", "2#", "3#"], ["3●", "3●"]]
		hand = Hand(data)
		self.examination = ThreeKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)