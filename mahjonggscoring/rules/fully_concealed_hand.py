class FullyConcealedHand:
	name = "Fully Concealed Hand"
	points = 4
	excluded = ("Concealed Hand", "Self-Drawn")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def evaluate(self):
		if getattr(self.hand, "concealed", None) is not None and type(self.hand.concealed) is not list and self.hand.concealed == True:
			fully_concealed = True
		else:
			fully_concealed = False
		return fully_concealed