from player import Player, PlayerReader, PlayerStats
from rich.prompt import Prompt
from player import show_players

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]
    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationalities = set(player.nationality for player in stats._players)
        nationality = Prompt.ask("Nationality", choices=nationalities, default="")

        players = stats.top_scorers_by_nationality(nationality)

        show_players(players, season, nationality)
    #break

if __name__ == "__main__":
    main()
