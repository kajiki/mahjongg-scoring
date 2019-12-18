import unittest2
from mahjonggscoring.rules import FourConcealedPungs
from mahjonggscoring import Hand

#Kongs are scored also.
class TestFourConcealedPungs(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●", "3●"], ["2/", "2/"], ["1#", "1#", "1#"]]
		hand = Hand(data, {"concealed": [True, True, True, False, True]})
		self.examination = FourConcealedPungs(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 64)

class TestFourConcealedPungsFull(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●"], ["2/", "2/"], ["1#", "1#", "1#"]]
		hand = Hand(data, {"concealed": True})
		self.examination = FourConcealedPungs(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 64)

class TestNotFourConcealedPungs(unittest2.TestCase):
	def test_not_four_pungs(self):
		data = [["3#", "4#", "5#"], ["C", "C"], ["6●", "6●", "6●"], ["7#", "7#", "7#"], ["8/", "8/", "8/", "8/"]]
		hand = Hand(data, {"concealed": True})
		self.examination = FourConcealedPungs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_not_concealed(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●"], ["2/", "2/"], ["1#", "1#", "1#", "1#"]]
		hand = Hand(data)
		self.examination = FourConcealedPungs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
		
if __name__ == '__main__':
	unittest2.main()