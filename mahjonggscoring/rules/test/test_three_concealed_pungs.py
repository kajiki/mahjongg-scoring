import unittest2
from mahjonggscoring.rules import ThreeConcealedPungs
from mahjonggscoring import Hand

#Kongs are scored also.
class TestThreeConcealedPungs(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●", "3●"], ["2/", "2/"], ["1#", "2#", "3#"]]
		hand = Hand(data, {"concealed": [True, True, True, False, True]})
		self.examination = ThreeConcealedPungs(hand)
		self.passed = self.examination.evaluate()
		
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 16)
		
class TestThreeConcealedPungsFull(unittest2.TestCase):
	def setUp(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●", "3●"], ["2/", "2/"], ["1#", "2#", "3#"]]
		hand = Hand(data, {"concealed": True})
		self.examination = ThreeConcealedPungs(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 16)

class TestNotThreeConcealedPungs(unittest2.TestCase):
	def test_not_three_pungs(self):
		data = [["6●", "7●", "8●"], ["B", "B", "B"], ["3●", "3●", "3●", "3●"], ["2/", "2/"], ["1#", "2#", "3#"]]
		hand = Hand(data, {"concealed": True})
		self.examination = ThreeConcealedPungs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_not_concealed(self):
		data = [["6●", "6●", "6●"], ["B", "B", "B"], ["3●", "3●", "3●", "3●"], ["2/", "2/"], ["1#", "2#", "3#"]]
		hand = Hand(data)
		self.examination = ThreeConcealedPungs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()