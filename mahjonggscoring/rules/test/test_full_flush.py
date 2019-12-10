import unittest2
from mahjonggscoring.rules import FullFlush
from mahjonggscoring import Hand

class TestFullFlushStandardHand(unittest2.TestCase):
	def setUp(self):
		data = [["4#", "5#", "6#"], ["6#", "7#", "8#"], ["3#", "3#", "3#"], ["2#", "2#", "2#"], ["9#", "9#"]]
		hand = Hand(data)
		self.examination = FullFlush(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 24)

class TestFullFlushSpecialHand(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "1●", "3●", "3●", "8●", "8●", "4●", "4●", "5●", "5●", "6●", "6●", "7●", "7●"]]
		hand = Hand(data)
		self.examination = FullFlush(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 24)

class TestNotFullFlush(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["4#", "5#", "6#"], ["6#", "7#", "8#"], ["2#", "3#", "4#"], ["2#", "2#", "2#"], ["9/", "9/"]]
		hand = Hand(data)
		self.examination = FullFlush(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["1●", "1●", "3●", "3●", "8●", "8●", "4●", "4●", "5/", "5/", "6●", "6●", "7●", "7●"]]
		hand = Hand(data)
		self.examination = FullFlush(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)