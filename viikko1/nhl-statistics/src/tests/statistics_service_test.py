import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertEqual(edm_players[0].name, "Semenko")
        self.assertEqual(edm_players[1].name, "Kurri")
        self.assertEqual(edm_players[2].name, "Gretzky")

    def test_search_returns_correct_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_top_returns_correct_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in top_players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_sorts_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_sorts_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_sorts_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_returns_empty_list_for_one(self):
        top_players = self.stats.top(1)
        self.assertEqual(len(top_players), 1)
