#unittest requires this insanity :(
if __package__.find(".") == -1:
	from constants import Constants
else:
	from mahjonggscoring.constants import Constants

class SeatWind:
	name = "Seat Wind"
	points = 2
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_standard_hand(self):
		return self.hand.standardhand
	
	def examine_important_wind(self):
		important_wind = False
		pungs_and_kongs = self.hand.pungs + self.hand.kongs
		
		try:
			seat_wind = Constants.WINDS[self.hand.seatwind]
			
			for tileset in pungs_and_kongs:
				if getattr(tileset, "honor", None) == "wind" and tileset.tiles[0].name == seat_wind:
					important_wind = True
		except AttributeError: pass
		except KeyError: pass
		
		return important_wind
		
	def evaluate(self):
		standard_hand = self.examine_standard_hand()
		important_wind = self.examine_important_wind()
		
		seat_wind = all([standard_hand, important_wind])
		return seat_wind