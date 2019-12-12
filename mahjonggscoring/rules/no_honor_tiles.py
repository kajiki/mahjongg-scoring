#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

class NoHonorTiles:
	name = "No Honor Tiles"
	points = 1
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_no_honors(self):
		all_tiles = []
		for tileset in self.hand.tilesets:
			for tile in tileset.tiles:
				all_tiles.append(tile)
	
		no_honors = not any(getattr(tile, "tile_type", None) == "honor" for tile in all_tiles)
		return no_honors
		
	def evaluate(self):
		no_honors = self.examine_no_honors()
		return no_honors