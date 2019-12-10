#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
	from tools import Tools
else:
	from mahjonggscoring.constants import Constants
	from mahjonggscoring.tools import Tools

import numpy as np

class SevenShiftedPairs:
	name = "Seven Shifted Pairs"
	points = 88
	excluded = ("Concealed Hand", "Full Flush", "Seven Pairs", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def map_codes(self):
		def get_codes(tile): return tile.code
		codes = list(map(get_codes, self.hand.special[0].tiles))
		return codes
	
	def map_ranks(self):
		def get_ranks(tile):
			rank = int(tile.rank)
			return rank
		ranks = list(map(get_ranks, self.hand.special[0].tiles))
		ranks.sort()
		return ranks
		
	def examine_correct_sum(self):
		correct_sum = True if self.hand.tilecount == 14 else False
		return correct_sum
		
	def examine_all_pairs(self):
		try:
			list_length = len(np.unique(np.array(self.map_codes())))
			all_pairs = True if list_length == self.hand.tilecount/2 else False
		except IndexError:
			all_pairs = False
		return all_pairs
		
	def examine_suit_sequence(self):
		try:
			first_suit = self.hand.special[0].tiles[0].suit
			same_suit = all(tile.suit == first_suit for tile in self.hand.special[0].tiles)
			
			if same_suit == True:
				ranks = np.unique(np.array(self.map_ranks()))
				suit_sequence = Tools.check_sequence(ranks)
			else:
				suit_sequence = False
		except AttributeError: #means tile.suit isn't set
			suit_sequence = False
		except IndexError: #means hand.special is empty
			suit_sequence = False
			
		return suit_sequence
	
	def evaluate(self):
		correct_sum = self.examine_correct_sum()
		all_pairs = self.examine_all_pairs()
		suit_sequence = self.examine_suit_sequence()
		
		passed = all([correct_sum, all_pairs, suit_sequence])
		return passed