class FourConcealedPungs:
	name = "Four Concealed Pungs"
	points = 64
	excluded = ("All Pungs", "Concealed Hand", "Three Concealed Pungs", "Two Concealed Pungs")

	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_no_chows(self):
		pungs_and_kongs = self.hand.pungs + self.hand.kongs
		not_pair = self.hand.pungs + self.hand.kongs + self.hand.knitted + self.hand.chows
		
		no_chows = True if len(pungs_and_kongs) == len(not_pair) else False
		return no_chows
		
	def examine_four_concealed(self):
		four_concealed = False
		concealed_sets = []
		limit_value = 4
		pungs_and_kongs = self.hand.pungs + self.hand.kongs
		
		#some tilesets are concealed
		if type(getattr(self.hand, "concealed", None)) is list:
			for tileset in pungs_and_kongs:
				concealed_sets.append(tileset.concealed)
		
			four_concealed = all(concealed_sets)

		#the hand is concealed
		elif getattr(self.hand, "concealed", None) == True:
			four_concealed = True if len(pungs_and_kongs) == limit_value else False

		#the hand is melded
		else: four_concealed = False
		
		return four_concealed
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		no_chows = self.examine_no_chows()
		four_concealed = self.examine_four_concealed()
		
		four_concealed_pungs = all([standard_hand, no_chows, four_concealed])
		return four_concealed_pungs