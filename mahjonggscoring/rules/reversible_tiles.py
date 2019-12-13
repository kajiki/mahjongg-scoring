class ReversibleTiles:
	name = "Reversible Tiles"
	points = 8
	excluded = ("One Voided Suit",)
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_codes(self, tiles):
		def get_codes(tile): return tile.code
		codes = list(map(get_codes, tiles))
		return codes
	
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_allowed_tiles(self):
		valid_tiles = ["1●", "2●", "3●", "4●", "5●", "8●", "9●", "2/", "4/", "5/", "6/", "8/", "9/", "B"]
		
		all_tiles = []
		for tileset in self.hand.tilesets:
			for tile in tileset.tiles:
				all_tiles.append(tile)
		
		allowed_tiles = all(code in valid_tiles for code in self.map_codes(all_tiles))
		return allowed_tiles
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		allowed_tiles = self.examine_allowed_tiles()
		
		reversible_tiles = all([standard_hand, allowed_tiles])
		return reversible_tiles