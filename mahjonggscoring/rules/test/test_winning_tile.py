import unittest2
from mahjonggscoring import Hand
from mahjonggscoring.rules import EdgeWait
from mahjonggscoring.rules import ClosedWait
from mahjonggscoring.rules import SingleWait
from mahjonggscoring.rules import SelfDrawn
from mahjonggscoring.rules import LastTile
from mahjonggscoring.rules import LastTileDraw
from mahjonggscoring.rules import LastTileClaim
from mahjonggscoring.rules import OutWithReplacementTile
from mahjonggscoring.rules import RobbingTheKong

class TestEdgeWait(unittest2.TestCase):
	def test_edge_wait(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1/", "2/", "3/"], ["7/", "8/", "9/"], ["5#", "5#"]]
		hand = Hand(data, {"winning tile": "Edge Wait"})
		self.examination = EdgeWait(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)

class TestClosedWait(unittest2.TestCase):
	def test_closed_wait(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1/", "2/", "3/"], ["7/", "8/", "9/"], ["5#", "5#"]]
		hand = Hand(data, {"winning tile": "Closed Wait"})
		self.examination = ClosedWait(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)
#
class TestSingleWait(unittest2.TestCase):
	def setUp(self):
		data = [["S", "S", "S"], ["E", "E", "E"], ["W", "W", "W"], ["N", "N", "N"], ["3#", "3#"]]
		hand = Hand(data, {"winning tile": "Single Wait"})
		self.examination = SingleWait(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)

class TestSelfDrawn(unittest2.TestCase):
	def test_self_drawn(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "1#", "1●", "9/", "9#", "9●", "1#"]]
		hand = Hand(data, {"winning tile": "Self-Drawn"})
		self.examination = SelfDrawn(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)

class TestLastTile(unittest2.TestCase):
	def test_last_tile(self):
		data = [["S", "S", "S"], ["E", "E", "E"], ["W", "W", "W"], ["N", "N", "N"], ["3#", "3#"]]
		hand = Hand(data, {"winning tile": "Last Tile"})
		self.examination = LastTile(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)
	
class TestLastTileDraw(unittest2.TestCase):
	def test_last_tile_draw(self):
		data = [["C", "C", "C"], ["F", "F", "F"], ["B", "B", "B"], ["5#", "6#", "7#"], ["3#", "3#"]]
		hand = Hand(data, {"winning tile": "Last Tile Draw"})
		self.examination = LastTileDraw(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)

class TestLastTileClaim(unittest2.TestCase):
	def setUp(self):
		data = [["1●", "2●", "3●"], ["4#", "5#", "6#"], ["7/", "8/", "9/"], ["2#", "3#", "4#"], ["1/", "1/"]]
		hand = Hand(data, {"winning tile": "Last Tile Claim"})
		self.examination = LastTileClaim(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)
	
class TestOutWithReplacementTile(unittest2.TestCase):
	def test_out_with_replacement_tile(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"winning tile": "Out with Replacement Tile"})
		self.examination = OutWithReplacementTile(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)

class TestRobbingTheKong(unittest2.TestCase):
	def test_robbing_the_kong(self):
		data = [["1●", "2●", "3●"], ["7●", "8●", "9●"], ["1/", "2/", "3/"], ["7/", "8/", "9/"], ["5#", "5#"]]
		hand = Hand(data, {"winning tile": "Robbing the Kong"})
		self.examination = RobbingTheKong(hand)
		self.passed = self.examination.evaluate()
		self.assertTrue(self.passed)