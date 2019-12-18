#unittest requires this insanity :(
if __package__.find(".") == -1:
	from tools import Tools
else:
	from mahjonggscoring.tools import Tools

class ThreeConcealedPungs:
	name = "Three Concealed Pungs"
	points = 16
	excludes = ("Two Concealed Pungs",)

	def __init__(self, handObj):
		self.hand = handObj
		
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_three_concealed(self):
		three_concealed = False
		limit_value = 3
		pungs_and_kongs = self.hand.pungs + self.hand.kongs
		
		#some tilesets are concealed
		if type(getattr(self.hand, "concealed", None)) is list:
			separated = Tools.separate_melded_concealed(self.hand.tilesets, self.hand.concealed)
						
			concealed_count = 0
			for tileset in separated["concealed"]:
				if tileset in pungs_and_kongs:
					concealed_count += 1

			three_concealed = True if concealed_count == limit_value else False
			
		#the hand is concealed
		elif getattr(self.hand, "concealed", None) == True:
			if len(pungs_and_kongs) == limit_value:
				three_concealed = True
			else:
				three_concealed = False
		
		#the hand is melded
		else: three_concealed = False
		
		return three_concealed
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		three_concealed = self.examine_three_concealed()
		
		three_concealed_pungs = all([standard_hand, three_concealed])
		return three_concealed_pungs