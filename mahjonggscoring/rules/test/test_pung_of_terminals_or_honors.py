import unittest2
from mahjonggscoring.rules import PungOfTerminalsOrHonors
from mahjonggscoring import Hand

#Concerns pungs/kongs of terminals as well as honors of wind type, specifically NOT prevalent or seat wind.
class TestPungOfTerminalsOrHonors(unittest2.TestCase):
	def setUp(self):
		data = [["S", "S", "S", "S"], ["E", "E", "E"], ["W", "W", "W"], ["1#", "1#", "1#"], ["3#", "3#"]]
		hand = Hand(data, {"prevalent wind": "E", "seat wind": "W"})
		self.examination = PungOfTerminalsOrHonors(hand)
		self.passed = self.examination.evaluate()

	def test_passed(self):
		self.assertEqual(self.passed, 2)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)

class TestNotPungOfTerminalsOrHonors(unittest2.TestCase):
	def test_dragons(self):
		data = [["C", "C", "C"], ["F", "F", "F"], ["B", "B", "B", "B"], ["5#", "6#", "7#"], ["3#", "3#"]]
		hand = Hand(data)
		self.examination = PungOfTerminalsOrHonors(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()