import unittest2
from mahjonggscoring.rules import NineGates
from mahjonggscoring import Hand

class TestNineGatesConcealed(unittest2.TestCase):
	def setUp(self):
		data = [["1/", "1/"], ["1/", "2/", "3/"], ["4/", "5/", "6/"], ["7/", "8/", "9/"], ["9/", "9/", "9/"]]
		hand = Hand(data, {"concealed": [False, True, True, True, True]})
		self.examination = NineGates(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNineGatesFullyConcealed(unittest2.TestCase):
	def setUp(self):
		data = [["1#", "1#", "1#"], ["2#", "3#", "4#"], ["4#", "5#", "6#"], ["7#", "8#", "9#"], ["9#", "9#"]]
		hand = Hand(data, {"concealed": True})
		self.examination = NineGates(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotNineGates(unittest2.TestCase):
	def test_not_concealed_hand(self):
		data = [["1/", "1/"], ["1/", "2/", "3/"], ["4/", "5/", "6/"], ["7/", "8/", "9/"], ["9/", "9/", "9/"]]
		hand = Hand(data, {"concealed": [False, True, False, False, True]})
		self.examination = NineGates(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_not_nine_gates(self):
		data = [["1#", "1#", "1#"], ["3#", "4#", "5#"], ["5#", "6#", "7#"], ["7#", "8#", "9#"], ["9#", "9#"]]
		hand = Hand(data)
		self.examination = NineGates(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
	def test_includes_kong(self):
		data = [["1/", "1/", "1/", "1/"], ["2/", "2/"], ["3/", "4/", "5/"], ["6/", "7/", "8/"], ["9/", "9/", "9/"]]
		hand = Hand(data, {"concealed": [True, False, True, True, True]})
		self.examination = NineGates(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()