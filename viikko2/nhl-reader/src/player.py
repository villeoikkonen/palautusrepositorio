import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name:20} team {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = filter(
            lambda player: player.nationality == nationality,
            self._players
        )
        sorted_players = sorted(
            players_of_nationality,
            reverse=True,
            key=lambda player: player.goals + player.assists
        )
        return list(sorted_players)

#{'name': 'Cole Schwindt', 'nationality': 'CAN', 'assists': 7, 'goals': 1, 'team': 'VGK', 'games': 42, 'id': 8481655}]