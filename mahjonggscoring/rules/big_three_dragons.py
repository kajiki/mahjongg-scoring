class BigThreeDragons:
	name = "Big Three Dragons"
	points = 88
	excluded = ("Dragon Pung", "Two Dragon Pungs")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def map_honors(self):
		def get_honors(tile):
			honor = getattr(tile, "honor", "")
			return honor
		honors = list(map(get_honors, self.hand.pungs))
		return honors
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_dragon_pungs(self):
		dragons = [honor for honor in self.map_honors() if honor == "dragon"]
		dragon_pungs = True if len(dragons) == 3 else False
		return dragon_pungs
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		dragon_pungs = self.examine_dragon_pungs()
		
		big_three_dragons = all([standard_hand, dragon_pungs])
		return big_three_dragons