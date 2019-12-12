#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
	from tools import Tools
else:
	from mahjonggscoring.constants import Constants
	from mahjonggscoring.tools import Tools

class KnittedStraight:
	name = "Knitted Straight"
	points = 12
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def map_ranks(self, tileset):
		def get_ranks(tile):
			rank = int(tile.rank)
			return rank
		ranks = list(map(get_ranks, tileset.tiles))
		ranks.sort()
		return ranks
	
	def examine_standard_hand(self):
		return self.hand.standardhand
		
	def examine_knitted_sets(self):
		return len(self.hand.knitted) == 3
	
	def examine_mixed_straight(self):
		knitted = []
		for tileset in self.hand.knitted:
			ranks = self.map_ranks(tileset)
			knitted.append(tuple(ranks))
		knitted_sorted = tuple(sorted(knitted, key=lambda tileset: tileset[0]))
		
		return knitted_sorted == Constants.KNITTED_SETS
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		knitted_sets = self.examine_knitted_sets()
		mixed_straight = self.examine_mixed_straight()
		
		knitted_straight = all([standard_hand, knitted_sets, mixed_straight])
		return knitted_straight
	
	
		