import unittest2
from mahjonggscoring.rules import TwoKongs
from mahjonggscoring import Hand

#Both kongs are melded.
class TestTwoKongs(unittest2.TestCase):
	def setUp(self):
		data = [["W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data)
		self.examination = TwoKongs(hand)
		self.passed = self.examination.evaluate()

	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 4)

class TestNotTwoKongs(unittest2.TestCase):
	def test_not_kong(self):
		data = [["6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = TwoKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_not_melded(self):
		data = [["W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data, {"concealed": [False, True, True, False, False]})
		self.examination = TwoKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
	def test_one_melded(self):
		data = [["W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data, {"concealed": [False, False, True, False, False]})
		self.examination = TwoKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["5/", "5/", "3/", "3/", "4/", "4/", "8/", "8/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = TwoKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()