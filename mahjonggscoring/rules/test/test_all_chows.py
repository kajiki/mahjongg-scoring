import unittest2
from mahjonggscoring.rules import AllChows
from mahjonggscoring import Hand

#The definition includes that the pair consist of suited tiles.
class TestAllChows(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "2●", "3●"], ["4#", "5#", "6#"], ["7/", "8/", "9/"], ["2#", "3#", "4#"], ["1/", "1/"]]
		hand = Hand(data)
		self.examination = AllChows(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 2)
		
class TestAllChowsKnitted(unittest2.TestCase):
	def setUp(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["2/", "3/", "4/"], ["4/", "4/"]]
		hand = Hand(data)
		self.examination = AllChows(hand)
		self.passed = self.examination.evaluate()

	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 2)

class TestNotAllChows(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["1●", "2●", "3●"], ["4#", "5#", "6#"], ["7/", "8/", "9/"], ["3#", "3#", "3#"], ["1/", "1/"]]
		hand = Hand(data)
		self.examination = AllChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_honors(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["2/", "3/", "4/"], ["B", "B"]]
		hand = Hand(data)
		self.examination = AllChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = AllChows(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()