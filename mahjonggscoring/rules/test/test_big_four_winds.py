import unittest2
from mahjonggscoring.rules import BigFourWinds
from mahjonggscoring import Hand

class TestBigFourWinds(unittest2.TestCase):
	def setUp(self):
		data = [["S", "S", "S"], ["E", "E", "E", "E"], ["W", "W", "W"], ["N", "N", "N"], ["3#", "3#"]]
		hand = Hand(data)
		self.examination = BigFourWinds(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotBigFourWinds(unittest2.TestCase):
	def test_standard_set(self):
		data = [["4#", "4#", "4#"], ["E", "E", "E"], ["W", "W", "W"], ["N", "N", "N"], ["3#", "3#"]]
		hand = Hand(data)
		self.examination = BigFourWinds(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_set(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "3●", "4/", "5#", "6●", "7#", "8#"]]
		hand = Hand(data)
		self.examination = BigFourWinds(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()