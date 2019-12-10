class AllGreen:
	name = "All Green"
	points = 88
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_codes(self, tiles):
		def get_codes(tile): return tile.code
		codes = list(map(get_codes, tiles))
		return codes
	
	def examine_standard_hand(self):
		return self.hand.standardhand
		
	def examine_allowed_tiles(self):
		valid_tiles = ["2/", "3/", "4/", "6/", "8/", "F"]
		
		all_tiles = []
		for tileset in self.hand.tilesets:
			for tile in tileset.tiles:
				all_tiles.append(tile)
		
		allowed_tiles = all(code in valid_tiles for code in self.map_codes(all_tiles))
		return allowed_tiles
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		allowed_tiles = self.examine_allowed_tiles()
		
		all_green = all([standard_hand, allowed_tiles])
		return all_green