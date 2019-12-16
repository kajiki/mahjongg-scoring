class ThreeKongs:
	name = "Three Kongs"
	points = 32
	excluded = ("Concealed Kong", "Melded Kong", "Two Concealed Kongs", "Two Kongs")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_correct_sum(self):
		correct_sum = True if self.hand.tilecount == 17 else False
		return correct_sum
	
	def examine_kong_hand(self):
		limit_value = 3
		kong_hand = True if len(self.hand.kongs) == 3 else False
		
		return kong_hand
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		correct_sum = self.examine_correct_sum()
		kong_hand = self.examine_kong_hand()
		
		three_kongs = all([standard_hand, correct_sum, kong_hand])
		return three_kongs