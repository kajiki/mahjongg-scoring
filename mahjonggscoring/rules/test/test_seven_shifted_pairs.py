import unittest2
from mahjonggscoring.rules import SevenShiftedPairs
from mahjonggscoring import Hand

#There are only nine possible combinations: 1-7, 2-8, 3-9 in the respective suit.
class TestSevenShiftedPairs(unittest2.TestCase):
	def setUp(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = SevenShiftedPairs(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotSevenShiftedPairs(unittest2.TestCase):
	def test_special_set(self):
		data = [["1/", "1/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = SevenShiftedPairs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
	def test_standard_set(self):
		data = [["6●", "6●", "6●"], ["7●", "7●", "7●"], ["8●", "8●", "8●"], ["9●", "9●", "9●"], ["2●", "2●"]]
		hand = Hand(data)
		self.examination = SevenShiftedPairs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()