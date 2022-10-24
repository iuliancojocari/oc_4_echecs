from chess.controllers.timestamp import get_timestamp
from chess.models.match import Match
from chess.models.round import Round

# from match import Match
# from round import Round
# from timestamp import get_timestamp
# from player import Player


class Tournament:
    def __init__(self, id, name, location, date, time_control, players=[], description=""):
        self.id = id
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.players = players
        self.nb_rounds = 4
        self.rounds = []
        self.scores = {}  # {"1": 2, "2": 4}

    def has_played(self, player_1, player_2):
        """
        Check if player_1 has played with player_2

        Parameters:
        - player_1 : current match player_1 (player object)
        - player_2 : current match player_2 (player object)

        Returns :
        - bool : True or False
        """
        for round in self.rounds:
            for match in round.matches:
                if (player_1 == match.player_1 and player_2 == match.player_2) or (
                    player_1 == match.player_2 and player_2 == match.player_1
                ):
                    return True

    def save_players_scores(self, winner, equality={}):
        """
        Save players scores

        Parameters :
        - Winner : player_x.id
        - Equality : {player_1: player_1.id, player_2: player_2.id}
        """
        if winner:
            self.scores[winner] = self.scores.get(winner, 0) + 1
        else:
            self.scores[equality["player_1"]] = self.scores.get(winner, 0) + 0.5
            self.scores[equality["player_2"]] = self.scores.get(winner, 0) + 0.5

    def sort_by_rank(self):
        """
        Sort players by rank
        """
        self.players.sort(key=lambda x: x.rank, reverse=True)

    def sort_players_by_score(self):
        """
        Sort players by score
        """
        for player in self.players:
            player._score = self.scores.get(player.id, 0)

        self.players.sort(key=lambda p: p._score, reverse=True)

    def get_players_with_same_score(self):
        """
        Get all players with the same score

        Returns:
        - dict : {_score: [players_list]}
        """
        players = {}
        for player in self.players:
            players.setdefault(getattr(player, "_score"), []).append(player)
        # return dict {_score : [players_list]}
        # exemple :
        # {2.5: [player_1, player_2], 1: [player_3, player_4]} etc etc
        return players

    def sort_by_rank_players_with_same_score(self):
        players = self.get_players_with_same_score()
        self.players = []
        for score, players_list in players.items():
            self.players.extend(
                sorted(players_list, key=lambda x: x.rank, reverse=True)
            )

    def create_round(self, round_number):
        start_date = get_timestamp()
        round = Round("Round " + str(round_number), start_date)

        match_number = 1
        if round_number == 1:
            self.sort_by_rank()

            # split list in 2
            top_players_list = self.players[: len(self.players) // 2]
            lower_players_list = self.players[len(self.players) // 2 :]

            for i, player in enumerate(top_players_list):
                player_1 = player
                player_2 = lower_players_list[i]

                match = Match(f"Match {match_number}", player_1, player_2)
                round.matches.append(match)
                match_number += 1
        else:
            self.sort_players_by_score()
            self.sort_by_rank_players_with_same_score()

            available_players = [p for p in self.players]

            while available_players:
                current_player = available_players.pop(0)
                for i, player in enumerate(available_players):
                    if not self.has_played(current_player, player):
                        match = Match(f"Match {match_number}", current_player, player)
                        round.matches.append(match)
                        available_players.pop(i)
                        match_number += 1
                        break
                else:
                    next_player = available_players.pop(0)
                    match = Match(f"Match {match_number}", current_player, next_player)
                    round.matches.append(match)
                    match_number += 1

        self.rounds.append(round)


"""
tournament = Tournament("1", "Premier", "Paris", "01-01-2022", "Bullet")
tournament.players = [
                Player(1, "Player_1", "Player_1", "21-09-2022", "H", rank=1),
                Player(2, "Player_2", "Player_2", "21-09-2022", "H", rank=2),
                Player(3, "Player_3", "Player_3", "21-09-2022", "H", rank=4),
                Player(4, "Player_4", "Player_4", "21-09-2022", "H", rank=7),
                Player(5, "Player_5", "Player_5", "21-09-2022", "H", rank=1),
                Player(6, "Player_6", "Player_6", "21-09-2022", "H", rank=5),
                Player(7, "Player_7", "Player_7", "21-09-2022", "H", rank=3),
                Player(8, "Player_8", "Player_8", "21-09-2022", "H", rank=2),
]
tournament.create_round(round_number=1)
print("Round 1")
print(f"{tournament.rounds[0].matches[0].player_1.first_name} - color : {tournament.rounds[0].matches[0].player_1._color}")
print(f"{tournament.rounds[0].matches[0].player_2.first_name} - color : {tournament.rounds[0].matches[0].player_2._color}")
print()
print(tournament.rounds[0].matches[1].player_1.first_name)
print(tournament.rounds[0].matches[1].player_2.first_name)
print()
print(tournament.rounds[0].matches[2].player_1.first_name)
print(tournament.rounds[0].matches[2].player_2.first_name)
print()
print(tournament.rounds[0].matches[3].player_1.first_name)
print(tournament.rounds[0].matches[3].player_2.first_name)

print()

tournament.save_players_scores(None, {"player_1": tournament.rounds[0].matches[0].player_1.id, "player_2": tournament.rounds[0].matches[0].player_2.id})
tournament.save_players_scores(None, {"player_1": tournament.rounds[0].matches[1].player_1.id, "player_2": tournament.rounds[0].matches[1].player_2.id})
tournament.save_players_scores(None, {"player_1": tournament.rounds[0].matches[2].player_1.id, "player_2": tournament.rounds[0].matches[2].player_2.id})
tournament.save_players_scores(None, {"player_1": tournament.rounds[0].matches[3].player_1.id, "player_2": tournament.rounds[0].matches[3].player_2.id})


tournament.create_round(round_number=2)
#print("Round 2")
#print(tournament.rounds[1].matches[0].player_1.__dict__)
#print(tournament.rounds[1].matches[0].player_2.__dict__)
#print()
#print(tournament.rounds[1].matches[1].player_1.__dict__)
#print(tournament.rounds[1].matches[1].player_2.__dict__)
#print()
#print(tournament.rounds[1].matches[2].player_1.__dict__)
#print(tournament.rounds[1].matches[2].player_2.__dict__)
#print()
#print(tournament.rounds[1].matches[3].player_1.__dict__)
#print(tournament.rounds[1].matches[3].player_2.__dict__)
#print()
tournament.save_players_scores(tournament.rounds[1].matches[0].player_1.id)
tournament.save_players_scores(tournament.rounds[1].matches[1].player_2.id)
tournament.save_players_scores(tournament.rounds[1].matches[2].player_1.id)
tournament.save_players_scores(tournament.rounds[1].matches[3].player_2.id)
#print()
tournament.create_round(round_number=3)
#print("Round 3")
#print(tournament.rounds[2].matches[0].player_1.__dict__)
#print(tournament.rounds[2].matches[0].player_2.__dict__)
#print()
#print(tournament.rounds[2].matches[1].player_1.__dict__)
#print(tournament.rounds[2].matches[1].player_2.__dict__)
#print()
#print(tournament.rounds[2].matches[2].player_1.__dict__)
#print(tournament.rounds[2].matches[2].player_2.__dict__)
#print()
#print(tournament.rounds[2].matches[3].player_1.__dict__)
#print(tournament.rounds[2].matches[3].player_2.__dict__)
tournament.save_players_scores(tournament.rounds[2].matches[0].player_1.id)
tournament.save_players_scores(tournament.rounds[2].matches[1].player_2.id)
tournament.save_players_scores(tournament.rounds[2].matches[2].player_1.id)
tournament.save_players_scores(tournament.rounds[2].matches[3].player_2.id)
#print()
tournament.create_round(round_number=3)
#print("Round 4")
#print(tournament.rounds[3].matches[0].player_1.__dict__)
#print(tournament.rounds[3].matches[0].player_2.__dict__)
#print()
#print(tournament.rounds[3].matches[1].player_1.__dict__)
#print(tournament.rounds[3].matches[1].player_2.__dict__)
#print()
#print(tournament.rounds[3].matches[2].player_1.__dict__)
#print(tournament.rounds[3].matches[2].player_2.__dict__)
#print()
#print(tournament.rounds[3].matches[3].player_1.__dict__)
#print(tournament.rounds[3].matches[3].player_2.__dict__)
tournament.save_players_scores(tournament.rounds[3].matches[0].player_1.id)
tournament.save_players_scores(tournament.rounds[3].matches[1].player_2.id)
tournament.save_players_scores(tournament.rounds[3].matches[2].player_1.id)
tournament.save_players_scores(tournament.rounds[3].matches[3].player_2.id)
"""
