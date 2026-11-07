from rich.prompt import Prompt
from player import PlayerStats
from player import show_players, get_players

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]
    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = get_players(url)
    stats = PlayerStats(reader)

    while True:
        teams = set(player.team for player in stats.players)
        team = Prompt.ask("Team", choices=teams, default="")

        players = stats.top_scorers_by_team(team)

        show_players(players, season, team)
    #break

if __name__ == "__main__":
    main()
