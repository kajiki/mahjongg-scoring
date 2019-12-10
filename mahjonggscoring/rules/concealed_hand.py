class ConcealedHand:
	name = "Concealed Hand"
	points = 2
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_four_concealed(self):
		concealed_sets = []
		allowed_sets = ["pung", "kong", "chow", "knitted"]
		
		for tileset in self.hand.tilesets:
			if tileset.type in allowed_sets:
				concealed_sets.append(tileset.concealed)
		
		return all(concealed_sets)
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		four_concealed = self.examine_four_concealed()
		
		concealed_hand = all([standard_hand, four_concealed])
		return concealed_hand