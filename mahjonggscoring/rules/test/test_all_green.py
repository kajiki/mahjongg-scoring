import unittest2
from mahjonggscoring.rules import AllGreen
from mahjonggscoring import Hand

#Standard hand, but only 6 kinds of tiles are valid: bamboo 2, 3, 4, 6, 8 and green dragon.
class TestAllGreen(unittest2.TestCase):
	def setUp(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = AllGreen(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotAllGreen(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["2/", "3/", "4/"], ["3/", "4/", "5/"], ["4/", "5/", "6/"], ["5/", "6/", "7/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = AllGreen(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = AllGreen(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()