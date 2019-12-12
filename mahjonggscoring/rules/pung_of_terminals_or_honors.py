#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

class PungOfTerminalsOrHonors:
	name = "Pung of Terminals or Honors"
	points = 1
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_tile_types(self, tilesets):
		def get_tile_types(tile):
			tile_type = getattr(tile, "tile_type", "")
			return tile_type
		tile_types = list(map(get_tile_types, tilesets))
		return tile_types
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_honor_terminal(self):
		terminal_or_honor = False
		pungs_and_kongs = self.hand.pungs + self.hand.kongs
		tile_types = list(self.map_tile_types(pungs_and_kongs))
		
		important_winds = []

		try: important_winds.append(Constants.WINDS[self.hand.prevalentwind])
		except AttributeError: pass
		except KeyError: pass
		
		try: important_winds.append(Constants.WINDS[self.hand.seatwind])
		except AttributeError: pass
		except KeyError: pass
		
		tileset_count = 0
		for tileset in pungs_and_kongs:
			if (getattr(tileset, "honor", None) == "wind" and tileset.tiles[0].name not in important_winds) or getattr(tileset, "tile_type", "") == "terminal":
				tileset_count += 1
		
		terminal_or_honor = tileset_count if tileset_count > 0 else False
		return terminal_or_honor
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		honor_terminal = self.examine_honor_terminal()
		
		pung_of_terminals_or_honors = honor_terminal if all([standard_hand, honor_terminal]) else False
		return pung_of_terminals_or_honors
	