#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

import numpy as np

class ThirteenOrphans:
	name = "Thirteen Orphans"
	points = 88
	excluded = ("All Types", "Concealed Hand", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_codes(self):
		def get_codes(tile): return tile.code
		codes = list(map(get_codes, self.hand.special[0].tiles))
		return codes
	
	def examine_correct_sum(self):
		correct_sum = True if self.hand.tilecount == 14 else False
		return correct_sum
	
	def examine_unique_tiles(self):
		try:
			list_length = len(np.unique(np.array(self.map_codes())))
			unique_tiles = True if list_length == 13 else False
		except IndexError:
			unique_tiles = False
			
		return unique_tiles
		
	def examine_honors_terminals(self):
		honors_terminals = list(Constants.WINDS) + list(Constants.DRAGONS) + ["1/", "9/", "1#", "9#", "1●", "9●"]
		
		try:
			codes = self.map_codes()
		
			no_simples = False
			for c in codes:
				if c not in honors_terminals:
					no_simples = False
					break
				else:
					no_simples = True
		except IndexError: #means hand.special is empty
			no_simples = False
		
		return no_simples
			
	def evaluate(self):
		correct_sum = self.examine_correct_sum()
		unique_tiles = self.examine_unique_tiles()
		honors_terminals = self.examine_honors_terminals()
		
		passed = all([correct_sum, unique_tiles, honors_terminals])
		return passed