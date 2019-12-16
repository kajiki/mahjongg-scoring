import unittest2
from mahjonggscoring.rules import TwoConcealedKongs
from mahjonggscoring import Hand

class TestTwoConcealedKongsPartial(unittest2.TestCase):
	def setUp(self):
		data = [["W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data, {"concealed": [False, True, True, True, False]})
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()

	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 8)
		
class TestTwoConcealedKongsAll(unittest2.TestCase):
	def setUp(self):
		data = [["W", "W", "W"], ["8#", "8#", "8#", "8#"], ["3#", "3#", "3#", "3#"], ["2/", "2/", "2/"], ["3●", "3●"]]
		hand = Hand(data, {"concealed": True})
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()

	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 8)
		
class TestNotTwoConcealedKongs(unittest2.TestCase):
	def test_not_kong(self):
		data = [["6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [False, True, True, True, False]})
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_none_concealed(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()
	
	def test_no_concealed_kongs(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [False, True, False, True, False]})
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_one_concealed(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [True, True, False, True, False]})
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["5/", "5/", "3/", "3/", "7/", "7/", "8/", "8/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = TwoConcealedKongs(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	