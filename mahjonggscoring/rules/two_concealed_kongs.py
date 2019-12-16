#unittest requires this insanity :(
if __package__.find(".") == -1:
	from tools import Tools
else:
	from mahjonggscoring.tools import Tools

class TwoConcealedKongs:
	name = "Two Concealed Kongs"
	points = 8
	excluded = ("Two Concealed Pungs",)
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
		
	def examine_two_concealed(self):
		two_concealed = False
		limit_value = 2
		
		#some tilesets are concealed
		if type(getattr(self.hand, "concealed", None)) is list:
			separated = Tools.separate_melded_concealed(self.hand.tilesets, self.hand.concealed)
						
			concealed_kong_count = 0
			for tileset in separated["concealed"]:
				if tileset in self.hand.kongs:
					concealed_kong_count += 1

			two_concealed = True if concealed_kong_count == limit_value else False
		
		#the hand is concealed
		elif getattr(self.hand, "concealed", None) == True:
			if len(self.hand.kongs) == limit_value:
				two_concealed = True
			else:
				two_concealed = False
		
		#the hand is melded
		else:
			two_concealed = False
		
		return two_concealed
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		two_concealed = self.examine_two_concealed()
		
		two_concealed_kongs = all([standard_hand, two_concealed])
		return two_concealed_kongs