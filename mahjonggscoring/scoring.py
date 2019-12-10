#unittest requires this insanity :(
from pathlib import Path
if __name__ == Path(__file__).stem:
	from rules import RuleList
else:
	from mahjonggscoring.rules import RuleList

import numpy as np
	
class Scoring:
	def __init__(self, handObj):
		self.hand = handObj
		self.score = 0
		self.criteria = {}
		
		#Sort rules by highest point value.
		sorted_rules = sorted(RuleList.RULES, key = RuleList.RULES.get, reverse = True)
		self.rules = sorted_rules
		
		excluded = []
		criteria_objects = {}
		
		for rule in self.rules:
			examination = rule(self.hand)
			passed = examination.evaluate()

			if passed == True:
				#Some rules apply, but don't score, because they're implied by other (usually higher scoring) rules.
				if rule.name not in excluded:
					criteria_objects[examination.name] = examination
				try: excluded += examination.excluded
				except AttributeError: pass

				excluded_unique = np.unique(np.array(excluded))
				excluded = excluded_unique.tolist()
		
		self.criteria = {key:rule.points for (key, rule) in criteria_objects.items()}
		self.score = sum(self.criteria.values())