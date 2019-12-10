import unittest2
from mahjonggscoring import Tile

class TestHanzi(unittest2.TestCase):
	def test_red_dragon(self):
		tile = Tile("中")
		self.assertEqual(tile.name, "red dragon")
	def test_green_dragon(self):
		tile = Tile("發")
		self.assertEqual(tile.name, "green dragon")
	def test_white_dragon(self):
		tile = Tile("白")
		self.assertEqual(tile.name, "white dragon")
	def test_east_wind(self):
		tile = Tile("東")
		self.assertEqual(tile.name, "east wind")
	def test_west_wind(self):
		tile = Tile("西")
		self.assertEqual(tile.name, "west wind")
	def test_south_wind(self):
		tile = Tile("南")
		self.assertEqual(tile.name, "south wind")
	def test_north_wind(self):
		tile = Tile("北")
		self.assertEqual(tile.name, "north wind")

if __name__ == '__main__':
	unittest2.main()