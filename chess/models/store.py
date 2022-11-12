from tinydb import TinyDB, Query
from tinydb.operations import add
from chess.models.tournament import Tournament
from chess.utils.constants import DB_PATH
from chess.models.player import Player


class Store:

    db = TinyDB(DB_PATH, indent=4)

    @classmethod
    def save(cls, table, item):
        cls.db.table(table).insert(item)

    @classmethod
    def update_tournament_info(cls, id, table, dict):
        cls.db.table(table).upsert(dict, Query().id == id)
    
    @classmethod
    def edit(cls, id, dict, table):
        Object = Query()
        return cls.db.table(table).upsert(dict, Object.id == id)

    @classmethod
    def add_players(cls, id, dict, table):
        Object = Query()
        
        return cls.db.table(table).update(add("players", [dict]), Object.id == id)

    @classmethod
    def save_round(cls, id, dict, table):
        Object = Query()

        return cls.db.table(table).update(add("rounds", [dict]), Object.id == id)

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
    def get_player_by_id(cls, id):
        player = cls.db.table("players").get(Query().id == id)
        return Player.from_dict(player)

    @classmethod
    def get_tournaments(cls):
        tournaments = cls.db.table("tournaments").all()

        if len(tournaments) == 0:
            return []
        else: 
            tournaments_list = []

            for tournament in tournaments:
                t = Tournament.from_dict(store=cls, dict=tournament)

                tournaments_list.append(t)

            return tournaments_list

    @classmethod
    def load_tournament(cls, id):
        Object = Query()
        tournament = cls.db.table("tournaments").get(Object.id == id)

        return Tournament.from_dict(store=cls, dict=tournament)
        
        
    @classmethod
    def save_winner_score(cls, id, table, dict):
        Object = Query()
        return cls.db.table(table).upsert({"scores": dict}, Object.id == id)
        

    @classmethod
    def save_results(cls, id, name, table, dict):
        Object = Query()

        return cls.db.table(table).upsert({"results": dict}, ((Object.id == id) and (Object.name == name)))
         