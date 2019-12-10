#unittest requires this insanity :(
from pathlib import Path
if __name__ == Path(__file__).stem:
	from tileset import Tileset
else:
	from mahjonggscoring.tileset import Tileset
	
class Hand:
	def __init__(self, tilesets, optional=None):
		self.tilesets = []
		self.pair = []
		self.pungs = []
		self.kongs = []
		self.chows = []
		self.knitted = []
		self.special = []
		self.tilecount = 0
		self.standardhand = False
		self.prevalentwind = ""
		self.seatwind = ""
		
		if optional is not None:
			#self.concealed is True if the hand is fully concealed, otherwise it's a list corresponding to the tilesets
			self.concealed = False if optional.get("concealed", None) is None else optional["concealed"]
			self.winningtile = False if optional.get("winning tile", None) is None else optional["winning tile"]
			self.flowers = 0 if optional.get("flowers", None) is None else optional["flowers"]
			self.prevalentwind = "E" if optional.get("prevalent wind", None) is None else optional["prevalent wind"]
			self.seatwind = "" if optional.get("seat wind", None) is None else optional["seat wind"]
			
		flat_list = []
		for sublist in tilesets:
			for item in sublist:
				flat_list.append(item)
		self.tilecount = len(flat_list)
	
		for i, tileset in enumerate(tilesets):
			if optional is not None and type(self.concealed) is list:
				self.tilesets.append(Tileset(tileset, self.concealed[i]))
			else:
				self.tilesets.append(Tileset(tileset))
			
		for tileset in self.tilesets:
			if tileset.type == "pair": self.pair.append(tileset)
			elif tileset.type == "pung": self.pungs.append(tileset)
			elif tileset.type == "kong": self.kongs.append(tileset)
			elif tileset.type == "chow": self.chows.append(tileset)
			elif tileset.type == "knitted": self.knitted.append(tileset)
			elif tileset.type == "special": self.special.append(tileset)
		
		#for arr in [self.tilesets, self.pair, self.pungs, self.kongs, self.chows, self.knitted, self.special]:
		#	arr = tuple(arr)
		
		standard_sets = self.kongs + self.pungs + self.chows + self.knitted
		self.standardhand = True if len(standard_sets) == 4 and len(self.pair) == 1 and len(self.special) == 0 else False