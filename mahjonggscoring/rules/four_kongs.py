class FourKongs:
	name = "Four Kongs"
	points = 88
	excluded = ("All Pungs", "Concealed Kong", "Melded Kong", "Single Wait", "Three Kongs", "Two Concealed Kongs", "Two Kongs")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_correct_sum(self):
		correct_sum = True if self.hand.tilecount == 18 else False
		return correct_sum
	
	def examine_kong_hand(self):
		limit_value = 4
		not_pair = self.hand.pungs + self.hand.kongs + self.hand.knitted + self.hand.chows
		kong_hand = True if len(self.hand.kongs) == limit_value and len(not_pair) == limit_value else False
		
		return kong_hand
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		correct_sum = self.examine_correct_sum()
		kong_hand = self.examine_kong_hand()
		
		four_kongs = all([standard_hand, correct_sum, kong_hand])
		return four_kongs