from nose.tools import *
from pyquiz.quiz2 import *

class TestQuiz2(object):
    def test_should_raise_WrongNumberOfPlayersError_when_not_two_players(self):
        game = [ ["Armando", "P"], ["Dave", "S"], ["Bob", "R"] ]
        assert_raises(WrongNumberOfPlayersError, rps_game_winner, game)

    def test_should_raise_NoSuchStrategyError_when_illegal_strategy_given(self):
        illegal_games = ([ ["Armando", "F"], ["Dave", "S"] ],
                            [ ["Armando", "sf"], ["Dave", "S"] ],
                            [ ["Armando", "s"], ["Dave", "fS"] ],
                            [ ["Armando", "s"], ["Dave", "Ss"] ]
        )

        for game in illegal_games:
            assert_raises(NoSuchStrategyError, rps_game_winner, game)

    def test_should_return_correct_winner_when_not_tie(self):
        actual = rps_game_winner([ ["Armando", "p"], ["Dave", "S"] ])

        assert_equal(actual, ["Dave", "S"])

    def test_should_return_first_player_when_tie(self):
        actual = rps_game_winner([ ["Armando", "P"], ["Dave", "P"] ])

        assert_equal(actual, ["Armando", "P"])

#rps_tournament_winner

    def test_should_return_winner_when_tournament_is_just_one_game(self):
        actual = rps_tournament_winner([ ["Armando", "P"], ["Dave", "P"] ])

        assert_equal(actual, ["Armando", "P"])

    def test_should_return_winner_when_tournament_is_8_players(self):
        tournament = [
                        [
                            [ ["Armando", "P"], ["Dave", "S"] ],
                            [ ["Richard", "R"],  ["Michael", "S"] ],
                        ],
                        [
                            [ ["Allen", "s"], ["Omer", "p"] ],
                            [ ["David E.", "R"], ["Richard X.", "P"] ]
                        ]
                    ]
        actual = rps_tournament_winner(tournament)

        assert_equal(actual, ["Richard", "R"])
