import unittest2
from mahjonggscoring import Tile

class TestTile(unittest2.TestCase):
	def test_wind(self):
		tile = Tile("S")
		self.assertEqual(tile.honor, "wind")
	def test_wind_is_honor(self):
		tile = Tile("S")
		self.assertEqual(tile.tile_type, "honor")
	def test_dragon(self):
		tile = Tile("F")
		self.assertEqual(tile.honor, "dragon")
	def test_dragon_is_honor(self):
		tile = Tile("F")
		self.assertEqual(tile.tile_type, "honor")
	
	def test_terminal_1(self):
		tile = Tile("1●")
		self.assertEqual(tile.tile_type, "terminal")
	def test_terminal_9(self):
		tile = Tile("9●")
		self.assertEqual(tile.tile_type, "terminal")
	def test_terminal_is_not_honor(self):
		tile = Tile("1#")
		self.assertRaises(AttributeError, lambda: tile.honor)
		
	def test_suit_has_rank(self):
		tile = Tile("5/")
		self.assertEqual(tile.rank, "5")
	def test_rank_has_suit(self):
		tile = Tile("5/")
		self.assertEqual(tile.suit, "bamboo")
	
	def test_honor_has_no_rank(self):
		tile = Tile("B")
		self.assertRaises(AttributeError, lambda: tile.rank)
	def test_honor_has_no_suit(self):
		tile = Tile("B")
		self.assertRaises(AttributeError, lambda: tile.suit)
	def test_suited_tile_is_not_honor(self):
		tile = Tile("3/")
		self.assertRaises(AttributeError, lambda: tile.honor)
		
	def test_name_suited(self):
		tile = Tile("8#")
		self.assertEqual(tile.name, "character 8")
	def test_name_dragon(self):
		tile = Tile("C")
		self.assertEqual(tile.name, "red dragon")
	def test_name_wind(self):
		tile = Tile("E")
		self.assertEqual(tile.name, "east wind")
	
if __name__ == '__main__':
	unittest2.main()