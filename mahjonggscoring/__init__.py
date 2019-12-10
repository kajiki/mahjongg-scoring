#unittest requires this insanity, sorry
if __name__ == '__main__':
	from tile import Tile
	from tileset import Tileset
	from hand import Hand
	from scoring import Scoring
	import rules
else:
	from mahjonggscoring.tile import Tile
	from mahjonggscoring.tileset import Tileset
	from mahjonggscoring.hand import Hand
	from mahjonggscoring.scoring import Scoring
	import mahjonggscoring.rules