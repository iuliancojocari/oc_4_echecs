from tinydb import TinyDB, Query, where
from tinydb.operations import add
from chess.models.tournament import Tournament
from chess.models.player import Player


class Store:

    # initiate the database
    db_path = "chess\\data\\database.json"

    db = TinyDB(db_path, indent=4)

    @classmethod
    def save(cls, dict, table):
        """
        Save item in the database

        Parameters:
        - table : database table - players or tournaments
        - dict: dictionnary to save into the database
        """
        return cls.db.table(table).insert(dict)

    @classmethod
    def update_tournament_info(cls, id, table, dict):
        """
        Update tournament info into the database

        Parameters:
        - id : tournament id
        - table : tournaments database table
        - dict : dictionnary to save into the database
        """
        return cls.db.table(table).upsert(dict, Query().id == id)

    @classmethod
    def edit(cls, id, dict, table):
        """
        Edit record into the database

        Parameters:
        - id : object id to edit
        - dict : the new edited dict to add into the database
        - table : database table
        """
        return cls.db.table(table).upsert(dict, Query().id == id)

    @classmethod
    def delete(cls, id, table):
        """
        Delete record from the database

        Parameters:
        - id : record id
        - table : database table - tournaments or players
        """
        return cls.db.table(table).remove(where("id") == id)

    @classmethod
    def get_players(cls):
        """
        Get all players
        """
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
        """
        Get player by id

        Parameters:
        - id : player id
        """
        player = cls.db.table("players").get(Query().id == id)
        return Player.from_dict(player)

    @classmethod
    def update_ranking(cls, id, rank):
        return cls.db.table("players").update(add("rank", rank), Query().id == id)

    @classmethod
    def get_tournaments(cls):
        """
        Get tournaments list
        """
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
    def get_tournament_by_id(cls, id):
        """
        Get tournament by id

        Parameters:
        - id : tournament id
        """
        tournament = cls.db.table("tournaments").get(Query().id == id)

        return Tournament.from_dict(store=cls, dict=tournament)
