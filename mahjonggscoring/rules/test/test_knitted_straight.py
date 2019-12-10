import unittest2
from mahjonggscoring.rules import KnittedStraight
from mahjonggscoring import Hand

class TestKnittedStraight(unittest2.TestCase):
	def setUp(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["3/", "3/", "3/"], ["4/", "4/"]]
		hand = Hand(data)
		self.examination = KnittedStraight(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 12)
		
class TestNotKnittedStraight(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1●", "2●", "3●"], ["7●", "8●", "9●"], ["5●", "5●"]]
		hand = Hand(data)
		self.examination = KnittedStraight(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["1/", "4/", "W", "C", "3#", "6#", "9#", "N", "S", "2●", "5●", "8●", "F", "E"]]
		hand = Hand(data)
		self.examination = KnittedStraight(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()