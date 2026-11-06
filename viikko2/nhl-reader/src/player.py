import requests
from rich.console import Console
from rich.table import Table
from rich import box

class Player: # pylint: disable=too-few-public-methods
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.games = player_data['games']

    def __str__(self):
        return f"{self.name:20} team {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerStats: # pylint: disable=too-few-public-methods
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = filter(
            lambda player: player.nationality == nationality,
            self.players
        )
        sorted_players = sorted(
            players_of_nationality,
            reverse=True,
            key=lambda player: player.goals + player.assists
        )
        return list(sorted_players)

def get_players(url):
    response = requests.get(url, timeout=2).json()
    players = [Player(player_dict) for player_dict in response]
    return players

def show_players(players, season, nationality):
    table = Table(
        title=f"Season {season} players from {nationality}",
        title_style="italic",
        header_style="bold white",
        box=box.SQUARE,
        padding=(0, 1),
    )

    table.add_column("Player", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", style="green", justify="right")
    table.add_column("assists", style="green", justify="right")
    table.add_column("points", style="green", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )

    console = Console()
    console.print(table)
