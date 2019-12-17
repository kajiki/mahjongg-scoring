#unittest requires this insanity :(
if __package__.find(".") == -1:
	from rules.all_chows import AllChows
	from rules.all_green import AllGreen
	from rules.big_four_winds import BigFourWinds
	from rules.big_three_dragons import BigThreeDragons
	from rules.concealed_hand import ConcealedHand
	from rules.concealed_kong import ConcealedKong
	from rules.four_kongs import FourKongs
	from rules.full_flush import FullFlush
	from rules.fully_concealed_hand import FullyConcealedHand
	from rules.knitted_straight import KnittedStraight
	from rules.melded_hand import MeldedHand
	from rules.melded_kong import MeldedKong
	from rules.nine_gates import NineGates
	from rules.no_honor_tiles import NoHonorTiles
	from rules.prevalent_wind import PrevalentWind
	from rules.pung_of_terminals_or_honors import PungOfTerminalsOrHonors
	from rules.pure_terminal_chows import PureTerminalChows
	from rules.reversible_tiles import ReversibleTiles
	from rules.seat_wind import SeatWind
	from rules.seven_shifted_pairs import SevenShiftedPairs
	from rules.thirteen_orphans import ThirteenOrphans
	from rules.three_kongs import ThreeKongs
	from rules.two_concealed_kongs import TwoConcealedKongs
	from rules.two_kongs import TwoKongs
	from rules.winning_tile import EdgeWait
	from rules.winning_tile import ClosedWait
	from rules.winning_tile import SingleWait
	from rules.winning_tile import SelfDrawn
	from rules.winning_tile import LastTile
	from rules.winning_tile import LastTileDraw
	from rules.winning_tile import LastTileClaim
	from rules.winning_tile import OutWithReplacementTile
	from rules.winning_tile import RobbingTheKong
else:
	from mahjonggscoring.rules.all_chows import AllChows
	from mahjonggscoring.rules.all_green import AllGreen
	from mahjonggscoring.rules.big_four_winds import BigFourWinds
	from mahjonggscoring.rules.big_three_dragons import BigThreeDragons
	from mahjonggscoring.rules.concealed_hand import ConcealedHand
	from mahjonggscoring.rules.concealed_kong import ConcealedKong
	from mahjonggscoring.rules.four_kongs import FourKongs
	from mahjonggscoring.rules.full_flush import FullFlush
	from mahjonggscoring.rules.fully_concealed_hand import FullyConcealedHand
	from mahjonggscoring.rules.knitted_straight import KnittedStraight
	from mahjonggscoring.rules.melded_hand import MeldedHand
	from mahjonggscoring.rules.melded_kong import MeldedKong
	from mahjonggscoring.rules.nine_gates import NineGates
	from mahjonggscoring.rules.no_honor_tiles import NoHonorTiles
	from mahjonggscoring.rules.prevalent_wind import PrevalentWind
	from mahjonggscoring.rules.pung_of_terminals_or_honors import PungOfTerminalsOrHonors
	from mahjonggscoring.rules.pure_terminal_chows import PureTerminalChows
	from mahjonggscoring.rules.reversible_tiles import ReversibleTiles
	from mahjonggscoring.rules.seat_wind import SeatWind
	from mahjonggscoring.rules.seven_shifted_pairs import SevenShiftedPairs
	from mahjonggscoring.rules.thirteen_orphans import ThirteenOrphans
	from mahjonggscoring.rules.three_kongs import ThreeKongs
	from mahjonggscoring.rules.two_concealed_kongs import TwoConcealedKongs
	from mahjonggscoring.rules.two_kongs import TwoKongs
	from mahjonggscoring.rules.winning_tile import EdgeWait
	from mahjonggscoring.rules.winning_tile import ClosedWait
	from mahjonggscoring.rules.winning_tile import SingleWait
	from mahjonggscoring.rules.winning_tile import SelfDrawn
	from mahjonggscoring.rules.winning_tile import LastTile
	from mahjonggscoring.rules.winning_tile import LastTileDraw
	from mahjonggscoring.rules.winning_tile import LastTileClaim
	from mahjonggscoring.rules.winning_tile import OutWithReplacementTile
	from mahjonggscoring.rules.winning_tile import RobbingTheKong

class RuleList:
	RULES = {\
		AllChows: AllChows.points,\
		#AllFives: AllFives.points,\
		AllGreen: AllGreen.points,\
		#AllPungs: AllPungs.points,\
		#AllEvenPungs: AllEvenPungs.points,\
		#AllHonors: AllHonors.points,\
		#AllSimples: AllSimples.points,\
		#AllTerminals: AllTerminals.points,\
		#AllTerminalsAndHonors: AllTerminalsAndHonors.points,\
		#AllTypes: AllTypes.points,\
		BigFourWinds: BigFourWinds.points,\
		BigThreeDragons: BigThreeDragons.points,\
		#BigThreeWinds: BigThreeWinds.points,\
		#ChickenHand: ChickenHand.points,\
		ClosedWait: ClosedWait.points,\
		ConcealedHand: ConcealedHand.points,\
		ConcealedKong: ConcealedKong.points,\
		#DoublePung: DoublePung.points,\
		#DragonPung: DragonPung.points,\
		EdgeWait: EdgeWait.points,\
		FourKongs: FourKongs.points,\
		#FourPureShiftedPungs: FourPureShiftedPungs.points,\
		#FourConcealedPungs: FourConcealedPungs.points,\
		#FourShiftedChows: FourShiftedChows.points,\
		FullFlush: FullFlush.points,\
		FullyConcealedHand: FullyConcealedHand.points,\
		#GreaterHonorsAndKnittedTiles: GreaterHonorsAndKnittedTiles.points,\
		#HalfFlush: HalfFlush.points,\
		KnittedStraight: KnittedStraight.points,\
		LastTile: LastTile.points,\
		LastTileClaim: LastTileClaim.points,\
		LastTileDraw: LastTileDraw.points,\
		#LesserHonorsAndKnittedTiles: LesserHonorsAndKnittedTiles.points,\
		#LittleFourWinds: LittleFourWinds.points,\
		#LittleThreeDragons: LittleThreeDragons.points,\
		#LowerFour: LowerFour.points,\
		#LowerTiles: LowerTiles.points,\
		MeldedHand: MeldedHand.points,\
		MeldedKong: MeldedKong.points,\
		#MiddleTiles: MiddleTiles.points,\
		#MixedDoubleChow: MixedDoubleChow.points,\
		#MixedShiftedChows: MixedShiftedChows.points,\
		#MixedShiftedPungs: MixedShiftedPungs.points,\
		#MixedStraight: MixedStraight.points,\
		#MixedTripleChow: MixedTripleChow.points,\
		NineGates: NineGates.points,\
		NoHonorTiles: NoHonorTiles.points,\
		#OneVoidedSuit: OneVoidedSuit.points,\
		#OutsideHand: OutsideHand.points,\
		OutWithReplacementTile: OutWithReplacementTile.points,\
		PrevalentWind: PrevalentWind.points,\
		PungOfTerminalsOrHonors: PungOfTerminalsOrHonors.points,\
		#PureDoubleChow: PureDoubleChow.points\
		#PureShiftedChows: PureShiftedChows.points,\
		#PureShiftedPungs: PureShiftedPungs.points,\
		#PureStraight: PureStraight.points,\
		PureTerminalChows: PureTerminalChows.points,\
		#PureTripleChow: PureTripleChow.points,\
		#QuadrupleChow: QuadrupleChow.points,\
		ReversibleTiles: ReversibleTiles.points,\
		RobbingTheKong: RobbingTheKong.points,\
		SeatWind: SeatWind.points,\
		SelfDrawn: SelfDrawn.points,\
		#SevenPairs: SevenPairs.points,\
		SevenShiftedPairs: SevenShiftedPairs.points,\
		#ShortStraight: ShortStraight.points,\
		SingleWait: SingleWait.points,\
		ThirteenOrphans: ThirteenOrphans.points,\
		#ThreeConcealedPungs: ThreeConcealedPungs.points,\
		#TileHog: TileHog.points,\
		ThreeKongs: ThreeKongs.points,\
		#TriplePung: TriplePung.points,\
		#ThreeSuitedTerminalChows: ThreeSuitedTerminalChows.points,\
		#TwoConcealedPungs: TwoConcealedPungs.points,\
		TwoConcealedKongs: TwoConcealedKongs.points,\
		#TwoDragonPungs: TwoDragonPungs.points,\
		TwoKongs: TwoKongs.points,\
		#TwoTerminalChows: TwoTerminalChows.points,\
		#UpperFour: UpperFour.points,\
		#UpperTiles: UpperTiles.points\
	}