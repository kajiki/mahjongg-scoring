import unittest2
from mahjonggscoring.rules import BigThreeDragons
from mahjonggscoring import Hand

class TestBigThreeDragons(unittest2.TestCase):
	def setUp(self):
		data = [["C", "C", "C"], ["F", "F", "F"], ["B", "B", "B", "B"], ["5#", "6#", "7#"], ["3#", "3#"]]
		hand = Hand(data)
		self.examination = BigThreeDragons(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotBigThreeDragons(unittest2.TestCase):
	def test_standard_set(self):
		data = [["C", "C", "C"], ["1#", "2#", "3#"], ["B", "B", "B"], ["3#", "4#", "5#"], ["3/", "3/"]]
		hand = Hand(data)
		self.examination = BigThreeDragons(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_set(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "1#", "1●", "9/", "9#", "9●", "1#"]]
		hand = Hand(data)
		self.examination = BigThreeDragons(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()