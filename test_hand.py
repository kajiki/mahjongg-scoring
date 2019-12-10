import unittest2
from mahjonggscoring import Hand

class TestHand(unittest2.TestCase):
	def test_standard_hand_has_5_sets(self):
		hand = Hand([["1/", "2/", "3/"], ["4●", "5●", "6●"], ["7/", "8/", "9/"], ["2●", "2●", "2●"], ["5#", "5#"]])
		all_tilesets = hand.pair + hand.pungs + hand.kongs + hand.chows + hand.knitted
		self.assertEqual(len(all_tilesets), 5)
	
	def test_no_kongs(self):
		hand = Hand([["1/", "2/", "3/"], ["4●", "5●", "6●"], ["7/", "8/", "9/"], ["2●", "2●", "2●"], ["5#", "5#"]])
		self.assertEqual(hand.tilecount, 14)
	
	def test_special_hand(self):
		hand = Hand([["E", "E", "8/", "8/", "4#", "4#", "4●", "4●", "N", "N", "9#", "9#", "B", "B"]])
		regular_tilesets = hand.pair + hand.pungs + hand.kongs + hand.chows + hand.knitted
		self.assertEqual(len(regular_tilesets), 0)
		
	def test_chows_not_in_pung_list(self):
		hand = Hand([["6#", "7#", "8#"], ["6#", "7#", "8#"], ["6#", "7#", "8#"], ["3/", "3/", "3/", "3/"], ["2●", "2●"]])
		self.assertEqual(len(hand.pungs), 0)
	
	def test_pungs_not_in_chow_list(self):
		hand = Hand([["1/", "1/", "1/"], ["2/", "2/", "2/"], ["3/", "3/", "3/"], ["S", "S", "S", "S"], ["C", "C"]])
		self.assertEqual(len(hand.chows), 0)
	
	def test_kong_in_kong_list(self):
		hand = Hand([["6#", "7#", "8#"], ["6#", "7#", "8#"], ["6#", "7#", "8#"], ["3/", "3/", "3/", "3/"], ["2●", "2●"]])
		self.assertEqual(len(hand.kongs), 1)
	
	def test_kong_not_elsewhere(self):
		hand = Hand([["1/", "1/", "1/"], ["2/", "2/", "2/"], ["3/", "3/", "3/"], ["S", "S", "S", "S"], ["C", "C"]])
		not_kongs = hand.pair + hand.pungs + hand.chows + hand.knitted
		self.assertEqual(len(not_kongs), 4)
	
if __name__ == '__main__':
	unittest2.main()