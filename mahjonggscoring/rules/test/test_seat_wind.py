import unittest2
from mahjonggscoring.rules import SeatWind
from mahjonggscoring import Hand

class TestSeatWind(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "7●", "8●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/", "3/"], ["1#", "2#", "3#"]]
		hand = Hand(data, {"seat wind": "W"})
		self.examination = SeatWind(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 2)
		
class TestNotSeatWind(unittest2.TestCase):
	def test_other_seat_wind(self):
		data = [["6●", "7●", "8●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/", "3/"], ["6#", "7#", "8#"]]
		hand = Hand(data, {"seat wind": "N"})
		self.examination = SeatWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_seat_wind_missing(self):
		data = [["6●", "7●", "8●"], ["W", "W", "W"], ["F", "F"], ["3/", "3/", "3/", "3/"], ["6#", "7#", "8#"]]
		hand = Hand(data)
		self.examination = SeatWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_no_wind_pung(self):
		data = [["6●", "7●", "8●"], ["W", "W"], ["F", "F", "F"], ["3/", "3/", "3/", "3/"], ["1#", "2#", "3#"]]
		hand = Hand(data, {"seat wind": "W"})
		self.examination = SeatWind(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()