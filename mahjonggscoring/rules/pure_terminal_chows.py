class PureTerminalChows:
	name = "Pure Terminal Chows"
	points = 64
	excluded = ("All Chows", "Full Flush", "Pure Double Chow", "Two Terminal Chows")
	
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
	
	def examine_correct_sum(self):
		correct_sum = True if self.hand.tilecount == 14 else False
		return correct_sum
	
	def examine_single_suit(self):
		try:
			first_suit = self.hand.tilesets[0].suit
			single_suit = all(tileset.suit == first_suit for tileset in self.hand.tilesets)
		except AttributeError: single_suit = False
		
		return single_suit
	
	def examine_correct_pattern(self):
		try:
			terminals = all(tileset.tile_type == "terminal" for tileset in self.hand.chows)
			
			if terminals == True:
				pair_of_fives = all(tile.rank == "5" for tile in self.hand.pair[0].tiles)
				
				terminal_1_count = 0
				terminal_9_count = 0
				terminal_1 = [1,2,3]
				terminal_9 = [7,8,9]
				
				for tileset in self.hand.chows:
					ranks = self.map_ranks(tileset)
					if ranks == terminal_1: terminal_1_count += 1
					elif ranks == terminal_9: terminal_9_count += 1
				
				correct_pattern = True if terminal_1_count == 2 and terminal_9_count == 2 and pair_of_fives == True else False
			else:
				correct_pattern = False
		except IndexError: correct_pattern = False
		except AttributeError: correct_pattern = False
		
		return correct_pattern
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		correct_sum = self.examine_correct_sum()
		single_suit = self.examine_single_suit()
		correct_pattern = self.examine_correct_pattern()
		
		passed = all([standard_hand, correct_sum, single_suit, correct_pattern])
		return passed