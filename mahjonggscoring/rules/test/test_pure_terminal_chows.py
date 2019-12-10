import unittest2
from mahjonggscoring.rules import PureTerminalChows
from mahjonggscoring import Hand

#There are only three possible combinations: 123 123 789 789 55 in the respective suit.
class TestPureTerminalChows(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1●", "2●", "3●"], ["7●", "8●", "9●"], ["5●", "5●"]]
		hand = Hand(data)
		self.examination = PureTerminalChows(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 64)
	
class TestNotPureTerminalChows(unittest2.TestCase):
	def test_not_terminal(self):
		data = [["1●", "2●", "3●"], ["4●", "5●", "6●"], ["1●", "2●", "3●"], ["7●", "8●", "9●"], ["5●", "5●"]]
		hand = Hand(data)
		self.examination = PureTerminalChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	def test_not_chows(self):
		data = [["1●", "2●", "3●"], ["1●", "1●", "1●"], ["9●", "9●", "9●"], ["7●", "8●", "9●"], ["5●", "5●"]]
		hand = Hand(data)
		self.examination = PureTerminalChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	def test_not_pure(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1/", "2/", "3/"], ["7/", "8/", "9/"], ["5#", "5#"]]
		hand = Hand(data)
		self.examination = PureTerminalChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	def test_special_set(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "1#", "1●", "9/", "9#", "9●", "1#"]]
		hand = Hand(data)
		self.examination = PureTerminalChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
if __name__ == '__main__':
	unittest2.main()