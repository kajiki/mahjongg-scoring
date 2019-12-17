#unittest requires this insanity :(
if __package__.find(".") == -1:
	from tools import Tools
else:
	from mahjonggscoring.tools import Tools

class ConcealedKong:
	name = "Concealed Kong"
	points = 2
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
		
	def examine_one_concealed(self):
		one_concealed = False
		limit_value = 1
		
		#some tilesets are concealed
		if type(getattr(self.hand, "concealed", None)) is list:
			separated = Tools.separate_melded_concealed(self.hand.tilesets, self.hand.concealed)
						
			concealed_kong_count = 0
			for tileset in separated["concealed"]:
				if tileset in self.hand.kongs:
					concealed_kong_count += 1

			one_concealed = True if concealed_kong_count == limit_value else False
		
		#the hand is concealed
		elif getattr(self.hand, "concealed", None) == True:
			if len(self.hand.kongs) == limit_value:
				one_concealed = True
			else:
				one_concealed = False
		
		#the hand is melded
		else: one_concealed = False
		
		return one_concealed
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		one_concealed = self.examine_one_concealed()
		
		concealed_kong = all([standard_hand, one_concealed])
		return concealed_kong