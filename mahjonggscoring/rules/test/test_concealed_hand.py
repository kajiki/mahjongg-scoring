import unittest2
from mahjonggscoring.rules import ConcealedHand
from mahjonggscoring import Hand

class TestConcealedHand(unittest2.TestCase):
	def setUp(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"concealed": [False, True, True, True, True]})
		self.examination = ConcealedHand(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 2)

class TestNotConcealedHand(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"concealed": [False, True, False, True, True]})
		self.examination = ConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_bad_input(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data, {"concealed": [True]})
		self.examination = ConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_full_concealment(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"concealed": True})
		self.examination = ConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_melded(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data)
		self.examination = ConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()