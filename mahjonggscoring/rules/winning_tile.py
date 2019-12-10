class EdgeWait:
	name = "Edge Wait"
	points = 1
	excluded = ("ClosedWait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def evaluate(self):
		chow_like = self.hand.chows + self.hand.knitted
		edge_wait = True if getattr(self.hand, "winningtile", "") == "Edge Wait" and len(chow_like) > 0 else False
		return edge_wait

class ClosedWait:
	name = "Closed Wait"
	points = 1
	excluded = ("Edge Wait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def evaluate(self):
		chow_like = self.hand.chows + self.hand.knitted
		closed_wait = True if getattr(self.hand, "winningtile", "") == "Closed Wait" and len(chow_like) > 0 else False
		return closed_wait

class SingleWait:
	name = "Single Wait"
	points = 1
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def evaluate(self):
		single_wait = True if getattr(self.hand, "winningtile", "") == "Single Wait" and len(self.hand.pair) == 1 else False
		return single_wait

class SelfDrawn:
	name = "Self-Drawn"
	points = 1
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def evaluate(self):
		return getattr(self.hand, "winningtile", "") == "Self-Drawn"

class LastTile:
	name = "Last Tile"
	points = 4
	excluded = ("ClosedWait", "Edge Wait", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def evaluate(self):
		return getattr(self.hand, "winningtile", "") == "Last Tile"

class LastTileDraw:
	name = "Last Tile Draw"
	points = 8
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Claim", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def evaluate(self):
		return getattr(self.hand, "winningtile", "") == "Last Tile Draw"
		
class LastTileClaim:
	name = "Last Tile Claim"
	points = 8
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Draw", "Out with Replacement Tile", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def evaluate(self):
		return getattr(self.hand, "winningtile", "") == "Last Tile Claim"

class OutWithReplacementTile:
	name = "Out with Replacement Tile"
	points = 8
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Robbing The Kong", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
	
	def examine_replaced_tile(self):
		replaced_tile = True if (getattr(self.hand, "flowers", 0) > 0) or len(self.hand.kongs) > 0 else False
		return replaced_tile
	
	def examine_status(self):
		return getattr(self.hand, "winningtile", "") == "Out with Replacement Tile"
	
	def evaluate(self):
		replaced_tile = self.examine_replaced_tile()
		status = self.examine_status()
		
		replacement_tile_last = all([replaced_tile, status])
		return replacement_tile_last
	
class RobbingTheKong:
	name = "Robbing The Kong"
	points = 8
	excluded = ("ClosedWait", "Edge Wait", "Last Tile", "Last Tile Claim", "Last Tile Draw", "Out with Replacement Tile", "Self-Drawn", "Single Wait")
	
	def __init__(self, handObj):
		self.hand = handObj
		
	def evaluate(self):
		return getattr(self.hand, "winningtile", "") == "Robbing the Kong"
	