from textwrap import indent
from tinydb import TinyDB, Query

class Database:

    def __init__(self, db):
        self.db = TinyDB(db, indent=4)
        self.players = self.db.table("players")