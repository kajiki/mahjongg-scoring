#unittest requires this insanity :(
if __package__.find(".") == -1:
	from tools import Tools
else:
	from mahjonggscoring.tools import Tools

class MeldedKong:
	name = "Melded Kong"
	points = 1
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
		
	def examine_one_melded(self):
		one_melded = False
		limit_value = 1
		
		#some tilesets are concealed
		if type(getattr(self.hand, "concealed", None)) is list:
			separated = Tools.separate_melded_concealed(self.hand.tilesets, self.hand.concealed)
						
			melded_kong_count = 0
			for tileset in separated["melded"]:
				if tileset in self.hand.kongs:
					melded_kong_count += 1

			one_melded = True if melded_kong_count == limit_value else False
			
		#all tilesets are melded (ignoring the pair)
		elif getattr(self.hand, "concealed", None) == None or getattr(self.hand, "concealed", None) == False:
			if len(self.hand.kongs) == limit_value: one_melded = True
			else: one_melded = False
				
		#the hand is concealed
		else: one_melded = False
		
		return one_melded
			
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		one_melded = self.examine_one_melded()
		
		melded_kong = all([standard_hand, one_melded])
		return melded_kong
			