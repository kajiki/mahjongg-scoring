import unittest2
from mahjonggscoring.rules import FullyConcealedHand
from mahjonggscoring import Hand

class TestFullyConcealedStandardHand(unittest2.TestCase):
	def setUp(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["3/", "3/", "3/"], ["4/", "4/"]]
		hand = Hand(data, {"concealed": True})
		self.examination = FullyConcealedHand(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 4)

class TestFullyConcealedSpecialHand(unittest2.TestCase):
	def setUp(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data, {"concealed": True})
		self.examination = FullyConcealedHand(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 4)

class TestNotFullyConcealedHand(unittest2.TestCase):
	def test_not_fully_concealed(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"concealed": [False, True, True, True, True]})
		self.examination = FullyConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_melded(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data)
		self.examination = FullyConcealedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()