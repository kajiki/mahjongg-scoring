import unittest2
from mahjonggscoring import Tileset

class TestTileset(unittest2.TestCase):
	def test_chow(self):
		tileset = Tileset(["7#", "8#", "9#"])
		self.assertEqual(tileset.type, "chow")
	
	def test_pung_suited(self):
		tileset = Tileset(["7#", "7#", "7#"])
		self.assertEqual(tileset.type, "pung")
		
	def test_pung_honors(self):
		tileset = Tileset(["E", "E", "E"])
		self.assertEqual(tileset.type, "pung")
		
	def test_kong_suited(self):
		tileset = Tileset(["1●", "1●", "1●", "1●"])
		self.assertEqual(tileset.type, "kong")
		
	def test_kong_honors(self):
		tileset = Tileset(["F", "F", "F", "F"])
		self.assertEqual(tileset.type, "kong")
		
	def test_pair_suited(self):
		tileset = Tileset(["6/", "6/"])
		self.assertEqual(tileset.type, "pair")
		
	def test_pair_honors(self):
		tileset = Tileset(["W", "W"])
		self.assertEqual(tileset.type, "pair")
		
	def test_knitted(self):
		tileset = Tileset(["2●", "5●", "8●"])
		self.assertEqual(tileset.type, "knitted")
		
	def test_special_set(self):
		tileset = Tileset(["E", "E", "8/", "8/", "4#", "4#", "4●", "4●", "N", "N", "9#", "9#", "B", "B"])
		self.assertEqual(tileset.type, "special")
		
	def test_wind(self):
		tileset = Tileset(["N", "N", "N", "N"])
		self.assertEqual(tileset.honor, "wind")
	def test_wind_is_honor(self):
		tileset = Tileset(["N", "N", "N", "N"])
		self.assertEqual(tileset.tile_type, "honor")
	
	def test_dragon(self):
		tileset = Tileset(["C", "C", "C", "C"])
		self.assertEqual(tileset.honor, "dragon")
	def test_dragon_is_honor(self):
		tileset = Tileset(["C", "C", "C", "C"])
		self.assertEqual(tileset.tile_type, "honor")
	
	def test_suited_set_is_not_honor(self):
		tileset = Tileset(["6#", "7#", "8#"])
		self.assertRaises(AttributeError, lambda: tileset.honor)
		
	def test_terminal_chow_1(self):
		tileset = Tileset(["1●", "2●", "3●"])
		self.assertEqual(tileset.tile_type, "terminal")
	def test_terminal_chow_9(self):
		tileset = Tileset(["7#", "8#", "9#"])
		self.assertEqual(tileset.tile_type, "terminal")
	
	def test_terminal_pair_1(self):
		tileset = Tileset(["1●", "1●"])
		self.assertEqual(tileset.tile_type, "terminal")
	def test_terminal_pair_9(self):
		tileset = Tileset(["9#", "9#"])
		self.assertEqual(tileset.tile_type, "terminal")
	
	def test_terminal_pung_1(self):
		tileset = Tileset(["1●", "1●", "1●"])
		self.assertEqual(tileset.tile_type, "terminal")
	def test_terminal_pung_9(self):
		tileset = Tileset(["9#", "9#", "9#"])
		self.assertEqual(tileset.tile_type, "terminal")
	
	def test_terminal_kong_1(self):
		tileset = Tileset(["1●", "1●", "1●", "1●"])
		self.assertEqual(tileset.tile_type, "terminal")
	def test_terminal_kong_9(self):
		tileset = Tileset(["9#", "9#", "9#", "9#"])
		self.assertEqual(tileset.tile_type, "terminal")
	
	def test_knitted_is_not_terminal(self):
		tileset = Tileset(["3/", "6/", "9/"])
		self.assertRaises(AttributeError, lambda: tileset.tile_type)
	
	def test_seven_shifted_pairs_has_suit(self):
		tileset = Tileset(["3/", "3/", "4/", "4/", "5/", "5/", "6/", "6/", "7/", "7/", "8/", "8/", "9/", "9/"])
		self.assertEqual(tileset.suit, "bamboo")
	def test_thirteen_orphans_has_no_suit(self):
		tileset = Tileset(["1/", "9/", "E", "C", "1#", "9#", "F", "S", "1●", "9●", "B", "N", "W", "W"])
		self.assertRaises(AttributeError, lambda: tileset.suit)
		
if __name__ == '__main__':
	unittest2.main()