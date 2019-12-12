import unittest2
from mahjonggscoring.rules import PrevalentWind
from mahjonggscoring import Hand

class TestPrevalentWind(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "6●", "6●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/"], ["2#", "2#", "2#"]]
		hand = Hand(data, {"prevalent wind": "W"})
		self.examination = PrevalentWind(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 2)

class TestNotPrevalentWind(unittest2.TestCase):
	def test_other_prevalent_wind(self):
		data = [["6●", "6●", "6●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/", "3/"], ["2#", "2#", "2#"]]
		hand = Hand(data, {"prevalent wind": "S"})
		self.examination = PrevalentWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_prevalent_wind_missing(self):
		data = [["6●", "6●", "6●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/", "3/"], ["2#", "2#", "2#"]]
		hand = Hand(data)
		self.examination = PrevalentWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_no_wind_pung(self):
		data = [["6●", "6●", "6●"], ["W", "W"], ["F", "F", "F"], ["3/", "3/", "3/"], ["2#", "2#", "2#"]]
		hand = Hand(data, {"prevalent wind": "W"})
		self.examination = PrevalentWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()