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
		self.repeated = {}
		self.seatwind = self.hand.seatwind
		self.prevalentwind = self.hand.prevalentwind
		
		#Sort rules by highest point value.
		sorted_rules = sorted(RuleList.RULES, key = RuleList.RULES.get, reverse = True)
		self.rules = sorted_rules
		
		excluded = []
		criteria_objects = {}
		repeated_criteria = {}
		
		for rule in self.rules:
			examination = rule(self.hand)
			passed = examination.evaluate()

			if passed == True or (type(passed is int) and passed > 0):
				#Some rules apply, but don't score, because they're implied by other (usually higher scoring) rules.
				if rule.name not in excluded:
					criteria_objects[examination.name] = examination
					if type(passed) is int and passed > 1:
						repeated_criteria[examination.name] = passed
				try: excluded += examination.excluded
				except AttributeError: pass

				excluded_unique = np.unique(np.array(excluded))
				excluded = excluded_unique.tolist()
		
		self.criteria = {key:rule.points for (key, rule) in criteria_objects.items()}
		self.repeated = repeated_criteria
		
		final_score = 0
		if repeated_criteria:
			occurrence = 0
			for key, value in self.criteria.items():
				if key in repeated_criteria.keys():
					occurrence = repeated_criteria[key]
				else:
					occurrence = 1
				final_score += value * occurrence
		else:
			final_score = sum(self.criteria.values())
		self.score = final_score