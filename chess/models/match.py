import random
from chess.models.player import Player

class Match:

    def __init__(self, name, player_1, player_2, player_1_color="", player_2_color="",results=[]):
        self.name = name
        self.player_1 = player_1
        self.player_1_color = player_1_color
        self.player_2 = player_2
        self.player_1_color = player_2_color
        self.results = results
        self.colors = ["Black", "White"]
        self.player_color = random.choice(self.colors)

        if self.player_color == "White":
            self.player_1_color = "White"
            self.player_2_color = "Black"
        else:
            self.player_1_color = "Black"
            self.player_2_color = "White"""

    def update_results(self, results=[]):
        self.results = results

        return results

    def to_dict(self):
        return {
            "name": self.name,
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "player_1_color": self.player_1_color,
            "player_2_color": self.player_2_color,
            "results": self.results,            
        }
    
    @classmethod
    def from_dict(cls, dict):
        return cls(**{
            "name": dict["name"],
            "player_1": Player.from_dict(dict["player_1"]),
            "player_2": Player.from_dict(dict["player_2"]),
            "player_1_color": dict["player_1_color"],           
            "player_2_color": dict["player_2_color"], 
            "results" : dict["results"]          
        })