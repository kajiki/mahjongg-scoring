import unittest2
from mahjonggscoring.rules import MeldedKong
from mahjonggscoring import Hand

class TestMeldedKongPartial(unittest2.TestCase):
	def setUp(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [False, True, False, False, False]})
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)

class TestMeldedKongExplicit(unittest2.TestCase):
	def setUp(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": False})
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)

class TestMeldedKongImplicit(unittest2.TestCase):
	def setUp(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
	
	def test_passed(self):
		self.assertTrue(self.passed)
	
	def test_points(self):
		self.assertEqual(self.examination.points, 1)

class TestNotMeldedKong(unittest2.TestCase):
	def test_not_kong(self):
		data = [["6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data)
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_not_melded(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [True, False, False, False, False]})
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_two_melded(self):
		data = [["6/", "6/", "6/", "6/"], ["2/", "3/", "4/"], ["F", "F", "F", "F"], ["2/", "3/", "4/"], ["8/", "8/"]]
		hand = Hand(data, {"concealed": [False, True, False, True, False]})
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)
	
	def test_special_hand(self):
		data = [["5/", "5/", "3/", "3/", "4/", "4/", "8/", "8/", "6/", "6/", "7/", "7/", "5/", "5/"]]
		hand = Hand(data)
		self.examination = MeldedKong(hand)
		self.passed = self.examination.evaluate()
		self.assertFalse(self.passed)

if __name__ == '__main__':
	unittest2.main()