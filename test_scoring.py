import unittest2
from mahjonggscoring import Hand
from mahjonggscoring import Scoring

#Tests 1-3 use examples from Mahjong Wiki, sourced 2019-12-09.
#http://mahjong.wikidot.com/rules:chinese-official-scoring
#Under Creative Commons Attribution-NoDerivs
#https://creativecommons.org/licenses/by-nd/3.0/

class TestScoringHand1(unittest2.TestCase):
	def setUp(self):
		data = [["B", "B"], ["3#", "4#", "5#"], ["6#", "7#", "8#"], ["6#", "7#", "8#"], ["W", "W", "W", "W"]]
		hand = Hand(data, {"concealed": [False, True, False, False, False], "prevalent wind": "E", "seat wind": "S"})
		self.examination = Scoring(hand)
	
	def test_score(self):
		self.assertEqual(self.examination.score, 11)
	
	def test_rules(self):
		rule_names = list(self.examination.criteria)
		rule_names.sort()
		self.assertListEqual(rule_names,["Half Flush", "Melded Kong", "Pung of Terminals or Honors", "Pure Double Chow", "Short Straight"])

class TestScoringHand2(unittest2.TestCase):
	def setUp(self):
		data = [["4/", "5/", "6/"], ["8●", "8●", "8●", "8●"], ["9●", "9●", "9●"], ["3●", "4●", "5●"], ["6/", "6/"]]
		hand = Hand(data, {"winning tile": "Self-Drawn", "prevalent wind": "E", "seat wind": "E"})
		self.examination = Scoring(hand)
		
	def test_score(self):
		self.assertEqual(self.examination.score, 12)
	
	def test_rules(self):
		rule_names = list(self.examination.criteria)
		rule_names.sort()
		self.assertListEqual(rule_names,["Melded Kong", "No Honor Tiles", "Pung of Terminals or Honors", "Reversible Tiles", "Self-Drawn"])

class TestScoringHand3(unittest2.TestCase):
	def setUp(self):
		data = [["2/", "5/", "8/"], ["1#", "4#", "7#"], ["3●", "6●", "9●"], ["1/", "2/", "3/"], ["4/", "4/"]]
		hand = Hand(data,{"winning tile": "Self-Drawn", "prevalent wind": "E", "seat wind": "E"})
		self.examination = Scoring(hand)
		
	def test_score(self):
		self.assertEqual(self.examination.score, 15)
	
	def test_rules(self):
		rule_names = list(self.examination.criteria)
		rule_names.sort()
		self.assertListEqual(rule_names,["All Chows", "Knitted Straight", "Self-Drawn"])

class TestScoringHand4(unittest2.TestCase):
	def setUp(self):
		data = [["8/", "8/", "3/", "3/", "4/", "4/", "9/", "9/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = Scoring(hand)
		
	def test_score(self):
		self.assertEqual(self.examination.score, 88)
	
	def test_rules(self):
		rule_names = list(self.examination.criteria)
		rule_names.sort()
		self.assertListEqual(rule_names, ["Seven Shifted Pairs"])

if __name__ == '__main__':
	unittest2.main()
	
