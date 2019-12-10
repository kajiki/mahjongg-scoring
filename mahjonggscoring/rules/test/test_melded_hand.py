import unittest2
from mahjonggscoring.rules import MeldedHand
from mahjonggscoring import Hand

class TestMeldedHand(unittest2.TestCase):
	def setUp(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data)
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 6)

class TestNotMeldedHand(unittest2.TestCase):
	def test_knitted_straight(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["3/", "3/", "3/"], ["4/", "4/"]]
		hand = Hand(data)
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_thirteen_orphans(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "1#", "1●", "9/", "9#", "9●", "1#"]]
		hand = Hand(data)
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
	def test_concealed_hand(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"concealed": [False, True, True, True, True]})
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_fully_concealed_hand(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data, {"concealed": True})
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_self_drawn(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"winning tile": "Self-Drawn"})
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_out_with_replacement_tile(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"flowers": 3, "winning tile": "Out with Replacement Tile"})
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_last_tile_draw(self):
		data = [["7#", "7#"], ["8#", "8#", "8#"], ["3●", "4●", "5●"], ["1/", "1/", "1/"], ["N", "N", "N"]]
		hand = Hand(data, {"winning tile": "Last Tile Draw"})
		self.examination = MeldedHand(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
	
if __name__ == '__main__':
	unittest2.main()