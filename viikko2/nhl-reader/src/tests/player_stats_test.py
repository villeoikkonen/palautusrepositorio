import unittest

from player import Player, PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "assists": 12,
                "goals": 4,
                "team": "EDM",
                "games": 20,
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "assists": 54,
                "goals": 45,
                "team": "PIT",
                "games": 20,
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "assists": 53,
                "goals": 37,
                "team": "EDM",
                "games": 20,
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "assists": 56,
                "goals": 42,
                "team": "DET",
                "games": 20,
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "assists": 89,
                "goals": 35,
                "team": "EDM",
                "games": 20,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_returns_players_in_point_order(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_top_scorers_by_team_returns_players_in_point_order(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_top_scorers_returns_empty_list_for_unknown_filter(self):
        players = self.stats.top_scorers_by_team("XXX")

        self.assertEqual(players, [])


if __name__ == "__main__":
    unittest.main()
