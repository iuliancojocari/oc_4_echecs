from textwrap import indent
from tinydb import TinyDB, Query
from chess.utils.constants import DB_PATH
from chess.models.player import Player


class Store:

    db = TinyDB(DB_PATH, indent=4)

    @classmethod
    def save(cls, db_table, item):
        cls.db.table(db_table).insert(item)

    @classmethod
    def get_players(cls):
          
        players = cls.db.table("players").all()

        players_list = []

        for player in players:

            p = Player.from_dict(player)

            players_list.append(p)

        
        return players_list

    
    @classmethod
    def delete_player(cls, player_id):
        pass