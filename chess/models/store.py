from tinydb import TinyDB
from chess.models.tournament import Tournament
from chess.utils.constants import DB_PATH
from chess.models.player import Player


class Store:

    db = TinyDB(DB_PATH, indent=4)

    @classmethod
    def save(cls, table, item):
        cls.db.table(table).insert(item)
    
    @classmethod
    def edit(cls, id, dict, table):
        return cls.db.table(table).update(dict, doc_ids=[id])

    @classmethod
    def delete(cls, id, table):
        return cls.db.table(table).remove(doc_ids=[id])

    @classmethod
    def get_players(cls):
        players = cls.db.table("players").all()

        if len(players) == 0:
            return []
        else:
            players_list = []

            for player in players:

                p = Player.from_dict(player)

                players_list.append(p)

            
            return players_list

    @classmethod
    def get_tournaments(cls):
        tournaments = cls.db.table("tournaments").all()

        if len(tournaments) == 0:
            return []
        else: 
            tournaments_list = []

            for tournament in tournaments:
                t = Tournament.from_dict(tournament)

                tournaments_list.append(t)

            return tournaments_list

    @classmethod
    def load_tournament(cls, id):
        tournament_data = cls.db.table("tournaments").get(doc_id=id)

        """tournament = Tournament(
            id = tournament_data["id"],
            name = tournament_data["name"],
            location = tournament_data["location"],
            date = tournament_data["date"],
            time_control = tournament_data["time_control"],
            players = tournament_data["players"],
            description = tournament_data["description"],
            nb_rounds = tournament_data["nb_rounds"],
            rounds = tournament_data["rounds"],
            scores = tournament_data["scores"]
        )"""

        tournament = {
            "id": tournament_data["id"],
            "name": tournament_data["name"],
            "location": tournament_data["location"],
            "date": tournament_data["date"],
            "time_control": tournament_data["time_control"],
            "players": tournament_data["players"],
            "description": tournament_data["description"],
            "nb_rounds": tournament_data["nb_rounds"],
            "rounds": tournament_data["rounds"],
            "scores": tournament_data["scores"]
        }


        return Tournament.from_dict(tournament)
    
    

    
         