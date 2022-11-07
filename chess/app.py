from textwrap import indent
from chess.controllers.home_controller import HomePageController
from chess.controllers.player_controller import PlayerController
from chess.controllers.tournament_controller import TournamentController
from chess.models.player import Player
from chess.models.tournament import Tournament
from chess.models.database import Database
import subprocess as sp
from tinydb import TinyDB



class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "manage_players": PlayerController.list,
        "new_player": PlayerController.create,
        "edit_player": PlayerController.update,
        "delete_player": PlayerController.delete,
        "manage_tournaments": TournamentController.list,
        "new_tournament": TournamentController.create,
        "load_tournament": TournamentController.load,
        "update_tournament": TournamentController.update,
        "delete_tournament": TournamentController.delete,
        "add_players": TournamentController.players,
        "play_tournament": TournamentController.play_tournament,
        "save_scores": TournamentController.save_scores,
        "play_round": TournamentController.play_round
        
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = TinyDB("database.json")
        """self.store = {
            "players": [
                Player(1, "Player_1", "Player_1", "21-09-2022", "H"),
                Player(2, "Player_2", "Player_2", "21-09-2022", "H"),
                Player(3, "Player_3", "Player_3", "21-09-2022", "H"),
                Player(4, "Player_4", "Player_4", "21-09-2022", "H"),
                Player(5, "Player_5", "Player_5", "21-09-2022", "H"),
                Player(6, "Player_6", "Player_6", "21-09-2022", "H"),
                Player(7, "Player_7", "Player_7", "21-09-2022", "H"),
                Player(8, "Player_8", "Player_8", "21-09-2022", "H"),
            ], 
            "tournaments": [
                Tournament(23, "Premier tournament", "Paris", "23/09/2022", "Blitz"),
                Tournament(24, "Deuxième tournament", "Bordeaux", "24/09/2022", "Bullet",[Player(1, "Player_1", "Player_1", "21-09-2022", "H"),Player(2, "Player_2", "Player_2", "21-09-2022", "H"),Player(3, "Player_3", "Player_3", "21-09-2022", "H"),Player(4, "Player_4", "Player_4", "21-09-2022", "H"),Player(5, "Player_5", "Player_5", "21-09-2022", "H"),Player(6, "Player_6", "Player_6", "21-09-2022", "H"),Player(7, "Player_7", "Player_7", "21-09-2022", "H"),Player(8, "Player_8", "Player_8", "21-09-2022", "H")])
            ]
        }"""
        
    def run(self):
        while not self.exit:
            # Clear the shell output
            if self.route == "select_players":
                pass
            else:
                sp.call("cls", shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]
            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True
