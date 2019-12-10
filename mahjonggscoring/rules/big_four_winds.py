class BigFourWinds:
	name = "Big Four Winds"
	points = 88
	excluded = ("All Pungs", "Big Three Winds", "Prevalent Wind", "Pung of Terminals or Honors", "Seat Wind")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def map_honors(self):
		def get_honors(tile):
			honor = getattr(tile, "honor", "")
			return honor
		honors = list(map(get_honors, self.hand.pungs + self.hand.kongs))
		return honors
	
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_wind_pungs(self):
		winds = [honor for honor in self.map_honors() if honor == "wind"]
		wind_pungs = True if len(winds) == 4 else False
		return wind_pungs
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		wind_pungs = self.examine_wind_pungs()
		
		big_four_winds = all([standard_hand, wind_pungs])
		return big_four_winds