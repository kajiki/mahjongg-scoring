import unittest2
from mahjonggscoring.rules import FourKongs
from mahjonggscoring import Hand

class TestFourKongs(unittest2.TestCase):
	def setUp(self):
		data = [["W", "W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data)
		self.examination = FourKongs(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)
		
class TestNotFourKongs(unittest2.TestCase):
	def test_not_four_kongs(self):
		data = [["W", "W", "W", "W"], ["8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data)
		self.examination = FourKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)