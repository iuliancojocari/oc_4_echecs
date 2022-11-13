from chess.controllers.timestamp import get_timestamp
from chess.models.match import Match
from chess.models.round import Round

class Tournament:
    def __init__(self, id, name, location, date, time_control, players=[], description="", nb_rounds=4, rounds=[], scores={}):
        self.id = id
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.scores = scores  # {"1": 2, "2": 4}

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

    def save_players_scores(self, winner, loser, null):
        """
        Save players scores

        Parameters :
        - Winner : player_x.id
        - Equality : {player_1: player_1.id, player_2: player_2.id}
        """

        if null:
            self.scores[null["player_1"]] = self.scores.get(null["player_1"], 0) + 0.5
            self.scores[null["player_2"]] = self.scores.get(null["player_2"], 0) + 0.5
        else : 
            self.scores[str(winner)] = self.scores.get(str(winner), 0) + 1
            self.scores[str(loser)] = self.scores.get(str(loser), 0) + 0


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
            player._score = self.scores.get(str(player.id), 0)

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
        """
        Sort players with the same score
        """
        players = self.get_players_with_same_score()
        self.players = []
        for score, players_list in players.items():
            self.players.extend(
                sorted(players_list, key=lambda x: x.rank, reverse=True)
            )

    def create_round(self, round_number):
        """
        Create new round

        Parameters:
        - round_number : number of the new round to create
        """
        start_date = get_timestamp()
        round = Round("Round " + str(round_number), start_date)
        round.matches = []

        match_number = 1
        if round_number == 1:
            # for the 1st round we sort players by rank
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
            # for the new rounds we sort players by score
            # if multiple players have the same score
            # we sort them by rank
            self.sort_players_by_score()
            print([p.first_name for p in self.players])
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
        
    @classmethod
    def set_round_end_date(cls, round):
        """
        At the end of each round, update the 
        round end_date attribute
        """
        round.end_date = get_timestamp()

    def to_dict(self):
        """
        Serialize tournament object
        """
        return {
            "id" : self.id, 
            "name" : self.name, 
            "location": self.location, 
            "date" : self.date, 
            "time_control": self.time_control, 
            "players": [player.id for player in self.players], 
            "description": self.description, 
            "nb_rounds": self.nb_rounds,
            "rounds": [round.to_dict() for round in self.rounds],
            "scores": self.scores
        }
    @classmethod
    def from_dict(cls, store, dict):
        """
        Deserialize tournament object
        """
        return cls(**{
            "id": dict["id"],
            "name": dict["name"],
            "location": dict["location"],
            "date": dict["date"],
            "time_control": dict["time_control"],
            "players": [store.get_player_by_id(player) for player in dict["players"]],
            "description": dict["description"],
            "nb_rounds": dict["nb_rounds"],
            "rounds": [Round.from_dict(store, round) for round in dict["rounds"]],
            "scores": dict["scores"]
        })

