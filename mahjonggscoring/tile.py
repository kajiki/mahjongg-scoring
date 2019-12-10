#unittest requires this insanity :(
from pathlib import Path
if __name__ == Path(__file__).stem:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

class Tile:
	def __init__(self, tile, going_out=None):
		#self.tile_type can be honor, terminal or neither; there is also self.honor
	
		self.code = tile
		self.name = ""
		self.last_tile = False #Use going_out, a mutable default argument
		
		#self.going_out = "" if going_out is None else going_out
	
		#rank is first character if single digit 1-9
		if tile[:1] and tile[:1].isdigit():
			self.rank = tile[:1]
		#suit is reverse first character if one of the three suits
		if tile[1:] and tile[1:] in Constants.SUITS.keys():
			self.suit = Constants.SUITS[tile[1:]]
		
		if tile in Constants.WINDS.keys():
			self.tile_type = "honor"
			self.honor = "wind"
		elif tile in Constants.DRAGONS.keys():
			self.tile_type = "honor"
			self.honor = "dragon"
		
		try:
			if self.rank == "1" or self.rank == "9":
				self.tile_type = "terminal"
		except AttributeError:
			pass
		
		honor = getattr(self, "honor", "")

		if honor == "wind":
			self.name = Constants.WINDS[tile]
		elif honor == "dragon":
			self.name = Constants.DRAGONS[tile]
		else:
			self.name = self.suit + " " + self.rank