#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

class FullFlush:
	name = "Full Flush"
	points = 24
	excluded = ("No Honor Tiles",)
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def get_tiles(self):
		all_tiles = []
		for tileset in self.hand.tilesets:
			for tile in tileset.tiles:
				all_tiles.append(tile)
		return all_tiles
	
	def examine_single_suit(self):
		all_tiles = self.get_tiles()
		single_suit = False
		try:
			first_tile_suit = all_tiles[0].suit
			single_suit = all(tile.suit == first_tile_suit for tile in all_tiles)
		except AttributeError: pass
		
		return single_suit
		
	def evaluate(self):
		full_flush = self.examine_single_suit()
		
		return full_flush