#unittest requires this insanity :(
from pathlib import Path
if __name__ == Path(__file__).stem:
	from constants import Constants
	from tile import Tile
	from tools import Tools
else:
	from mahjonggscoring.constants import Constants
	from mahjonggscoring.tile import Tile
	from mahjonggscoring.tools import Tools

class Tileset:
	def __init__(self, tiles, concealed=None):
		#self.type can be pung, kong, chow, knitted, pair, special
		#self.tile_type is determined from tile.tile_type
		#self.honor is determined from tile.honor
		
		self.tiles = []
		self.concealed = False if concealed is None else concealed
		
		for t in tiles:
			self.tiles.append(Tile(t))
		
		#this includes Seven Pairs
		if len(tiles) == 14:
			self.type = "special"
			
		tileset_type = getattr(self, "type", "")
		honor = getattr(self.tiles[0], "honor", "")

		if tileset_type != "special":
			if honor == "dragon":
				self.tile_type = "honor"
				self.honor = "dragon"
			elif honor == "wind":
				self.tile_type = "honor"
				self.honor = "wind"
			try:
				self.suit = self.tiles[0].suit
			except AttributeError:
				pass
		
		is_sequence = False
		is_repeated = False
		is_knitted = False
		first_tile_rank = getattr(self.tiles[0], "rank", "")
		first_tile_suit = getattr(self.tiles[0], "suit", "")
		if tileset_type == "special":
			#There is only one special set which has a suit: Seven Shifted Pairs.
			
			def get_suits(tile):
				suit = getattr(tile, "suit", "")
				return suit
			suits = list(map(get_suits, self.tiles))
			
			if "" not in suits:
				self.suit = self.tiles[0].suit
			
		#suited sets can take many forms
		elif first_tile_rank.isdigit():
			
			def get_ranks(tile):
				rank = int(tile.rank)
				return rank
			ranks = list(map(get_ranks, self.tiles))
			ranks.sort()
			
			is_sequence = Tools.check_sequence(ranks)
			is_repeated = True if ranks == list(reversed(ranks)) else False
				
			for knitted in Constants.KNITTED_SETS:
				if is_sequence == False and tuple(ranks) == knitted: is_knitted = True
			
			type_first = getattr(self.tiles[0], "tile_type", "")
			type_last = getattr(self.tiles[-1], "tile_type", "")
			#chow, pung, kong and pair can be terminal, knitted can not
			if (type_first == "terminal" or type_last == "terminal") and is_knitted == False:
				self.tile_type = "terminal"

		#honor sets lack rank and are thus simpler
		else:
			def get_names(tile): return tile.name		
			names = list(map(get_names, self.tiles))
			names.sort()
			
			is_repeated = True if names == list(reversed(names)) else False

		if is_sequence == True:
			self.type = "chow"
		elif is_knitted == True:
			self.type = "knitted"
			self.concealed = True #knitted sets cannot be melded
		elif is_repeated == True and len(self.tiles) == 2:
			self.type = "pair"
		elif is_repeated == True and len(self.tiles) == 3:
			self.type = "pung"
		elif is_repeated == True and len(self.tiles) == 4:
			self.type = "kong"