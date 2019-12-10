import unittest2
from mahjonggscoring.rules import NoHonorTiles
from mahjonggscoring import Hand

class TestNoHonorTilesStandardHand(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "2●", "3●"], ["4#", "5#", "6#"], ["7/", "8/", "9/"], ["2#", "3#", "4#"], ["1/", "1/"]]
		hand = Hand(data)
		self.examination = NoHonorTiles(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)
	
class TestNoHonorTilesSpecialHand(unittest2.TestCase):
	def setUp(self):
		data = [["7●", "7●", "4●", "4●", "4#", "4#", "9/", "9/", "6/", "6/", "7/", "7/", "8●", "8●"]]
		hand = Hand(data)
		self.examination = NoHonorTiles(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)
		
class TestNotNoHonorTiles(unittest2.TestCase):
	def test_standard_hand(self):
		data = [["1●", "2●", "3●"], ["4#", "5#", "6#"], ["7/", "8/", "9/"], ["2#", "3#", "4#"], ["F", "F"]]
		hand = Hand(data)
		self.examination = NoHonorTiles(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["7●", "7●", "4●", "4●", "4#", "4#", "9/", "9/", "6/", "6/", "E", "E", "8●", "8●"]]
		hand = Hand(data)
		self.examination = NoHonorTiles(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)