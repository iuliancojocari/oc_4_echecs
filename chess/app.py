from textwrap import indent
from chess.controllers.home_controller import HomePageController
from chess.controllers.player_controller import PlayerController
from chess.controllers.tournament_controller import TournamentController
from chess.controllers.reports_controller import ReportsController
# from chess.models.player import Player
# from chess.models.tournament import Tournament
from chess.models.store import Store
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
        "add_tournament_players": TournamentController.add_tournament_players,
        "play_tournament": TournamentController.play_tournament,
        "save_scores_and_results": TournamentController.save_scores_and_results,
        "play_round": TournamentController.play_round,
        "update_player_ranking": PlayerController.update_player_ranking,
        "reports": ReportsController.display_menu,
        "display_all_players": ReportsController.display_all_players,
        "display_tournament_players": ReportsController.display_tournament_players,
        "display_all_tournaments": ReportsController.display_all_tournaments,
        "display_tournament_round": ReportsController.display_tournament_rounds,
        "display_tournament_matches": ReportsController.display_tournament_matches
        
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        
        
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
            next_route, next_params = controller_method(self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True
