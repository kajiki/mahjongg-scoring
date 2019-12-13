class NineGates:
	name = "Nine Gates"
	points = 88
	excluded = ("Full Flush", "Pung of Terminals or Honors")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_ranks(self, tiles):
		def get_ranks(tile):
			rank = int(tile.rank)
			return rank
		ranks = list(map(get_ranks, tiles))
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
	
	def examine_concealed(self):
		concealed_sets = []
		allowed_sets = ["pung", "kong", "chow", "knitted"]
		
		for tileset in self.hand.tilesets:
			if tileset.type in allowed_sets:
				concealed_sets.append(tileset.concealed)
		concealed_hand = all(concealed_sets)
		
		if getattr(self.hand, "concealed", None) is not None and type(self.hand.concealed) is not list and self.hand.concealed == True:
			fully_concealed_hand = True
		else:
			fully_concealed_hand = False
		
		concealed = any([concealed_hand, fully_concealed_hand])
		return concealed
	
	def examine_correct_pattern(self):
		correct_pattern = False
		allowed_pattern = (1,1,1,2,3,4,5,6,7,8,9,9,9)
		
		all_tiles = []
		for tileset in self.hand.tilesets:
			for item in tileset.tiles:
				all_tiles.append(item)
		
		try:
			ranks = self.map_ranks(all_tiles)
			ranks.sort()
			
			#the hand can go out in one of 9 ways, look for that tile
			for n in range(1, 10):
				pattern_test = list(allowed_pattern)
				pattern_test.append(n)
				pattern_test.sort()
				if ranks == pattern_test: correct_pattern = True
		except AttributeError: pass
		
		return correct_pattern
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		correct_sum = self.examine_correct_sum()
		single_suit = self.examine_single_suit()
		concealed = self.examine_concealed()
		correct_pattern = self.examine_correct_pattern()
		
		nine_gates = all([standard_hand, correct_sum, single_suit, concealed, correct_pattern])
		return nine_gates
