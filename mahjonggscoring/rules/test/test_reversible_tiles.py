import unittest2
from mahjonggscoring.rules import ReversibleTiles
from mahjonggscoring import Hand

class TestReversibleTiles(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "2●", "3●"], ["2●", "3●", "4●"], ["5●", "5●", "5●"], ["5/", "5/", "5/", "5/"], ["B", "B"]]
		hand = Hand(data)
		self.examination = ReversibleTiles(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 8)

class TestNotReversibleTiles(unittest2.TestCase):
	def test_wrong_tiles(self):
		data = [["1●", "2●", "3●"], ["2●", "3●", "4●"], ["3●", "4●", "5●"], ["6●", "6●", "6●"], ["B", "B"]]
		hand = Hand(data)
		self.examination = ReversibleTiles(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
if __name__ == '__main__':
	unittest2.main()