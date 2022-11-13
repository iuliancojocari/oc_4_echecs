import random

class Match:

    def __init__(self, name, player_1, player_2, player_1_color=None, player_2_color=None, results={}):
        self.name = name
        self.player_1 = player_1
        self.player_1_color = player_1_color
        self.player_2 = player_2
        self.player_1_color = player_2_color
        self.results = results
        self.colors = ["Black", "White"]
        self.player_color = random.choice(self.colors)

        # set the player color
        if self.player_color == "White":
            self.player_1_color = "White"
            self.player_2_color = "Black"
        else:
            self.player_1_color = "Black"
            self.player_2_color = "White"""

    def update_results(self, winner, loser, match_null):
        """
        Update results

        Parameters:
        - winner : player_x.id
        - loser : player_x.id
        - null : {player_1: player_1.id, player_2: player_2.id}
        """
        if match_null:
            self.results[match_null["player_1"]] = 0.5
            self.results[match_null["player_2"]] = 0.5
        else:
            self.results[winner] = 1
            self.results[loser] = 0
        
    def to_dict(self):
        """
        Serialize match
        """
        return {
            "name": self.name,
            "player_1": self.player_1.id, 
            "player_2": self.player_2.id,
            "player_1_color": self.player_1_color,
            "player_2_color": self.player_2_color,
            "results": self.results,            
        }
    
    @classmethod
    def from_dict(cls, store, dict):
        """
        Deserialize match
        """
        return cls(**{
            "name": dict["name"],
            "player_1": store.get_player_by_id(dict["player_1"]),
            "player_2": store.get_player_by_id(dict["player_2"]), # dict[x] = player.id
            "player_1_color": dict["player_1_color"],           
            "player_2_color": dict["player_2_color"], 
            "results" : dict["results"]          
        })