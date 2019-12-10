class MeldedHand:
	name = "Melded Hand"
	points = 6
	excluded = ("Single Wait",)
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_nothing_concealed(self):
		concealed_sets = []
		allowed_sets = ["pung", "kong", "chow", "knitted"]
		
		for tileset in self.hand.tilesets:
			if tileset.type in allowed_sets:
				concealed_sets.append(tileset.concealed)
		
		nothing_concealed = False
		
		drawn_winning_tile = ["Self-Drawn", "Out with Replacement Tile", "Last Tile Draw"]
		
		if getattr(self.hand, "winningtile", None) in drawn_winning_tile:
			nothing_concealed = False
		elif any(concealed_sets):
			nothing_concealed = False
		else:
			if getattr(self.hand, "concealed", None) is not None and type(self.hand.concealed) is not list and self.hand.concealed == False:
				nothing_concealed = True
			elif getattr(self.hand, "concealed", None) is None:
				nothing_concealed = True
			else:
				nothing_concealed = False
				
		return nothing_concealed
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		nothing_concealed = self.examine_nothing_concealed()
		
		melded_hand = all([standard_hand, nothing_concealed])
		return melded_hand
		
