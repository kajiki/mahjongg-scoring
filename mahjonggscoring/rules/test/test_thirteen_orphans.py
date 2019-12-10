import unittest2
from mahjonggscoring.rules import ThirteenOrphans
from mahjonggscoring import Hand

class TestThirteenOrphans(unittest2.TestCase):
	def setUp(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "1#", "1●", "9/", "9#", "9●", "1#"]]
		hand = Hand(data)
		self.examination = ThirteenOrphans(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 88)

class TestNotThirteenOrphans(unittest2.TestCase):
	def test_other_special_set(self):
		data = [["N", "S", "E", "W", "C", "F", "B", "1/", "3●", "4/", "5#", "6●", "7#", "8#"]]
		hand = Hand(data)
		self.examination = ThirteenOrphans(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_standard_set(self):
		data = [["W", "W", "W"], ["E", "E", "E"], ["N", "N", "N"], ["1#", "2#", "3#"], ["C", "C"]]
		hand = Hand(data)
		self.examination = ThirteenOrphans(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
if __name__ == '__main__':
	unittest2.main()