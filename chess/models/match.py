import random

class Match:

    def __init__(self, name, player_1, player_2):
        self.name = name
        self.player_1 = player_1
        self.player_2 = player_2
        self.results = []
        self.colors = ["Black", "White"]
        self.player_color = random.choice(self.colors)

        if self.player_color == "White":
            self.player_1._color = "White"
            self.player_2._color = "Black"
        else:
            self.player_1._color = "Black"
            self.player_2._color = "White"
        

    def update_results(self, results=[]):
        self.results = results