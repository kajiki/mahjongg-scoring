#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants
	
class AllChows:
	name = "All Chows"
	points = 2
	excluded = ("No Honor Tiles",)
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_suited_pair(self):
		suited_pair = False
		suits = list(Constants.SUITS.values())
		try:
			suited_pair = True if self.hand.pair[0].suit in suits else False
		#no suit
		except AttributeError: pass
		#no pair
		except IndexError: pass
		
		return suited_pair
	
	def examine_chow_hand(self):
		chow_like = self.hand.chows + self.hand.knitted
		chow_hand = True if len(chow_like) == 4 else False
		return chow_hand
	
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		chow_hand = self.examine_chow_hand()
		suited_pair = self.examine_suited_pair()
		
		all_chows = all([standard_hand, chow_hand, suited_pair])
		return all_chows
		