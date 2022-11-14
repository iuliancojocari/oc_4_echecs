from chess.models.store import Store
from chess.views.reports_view import ReportsView

class ReportsController:

    @classmethod
    def display_menu(cls, route_params=None):

        choice = ReportsView.display_menu()

        if choice == "1":
            next = "display_all_players"
        elif choice == "2":
            next = "display_tournament_players"
        elif choice == "3":
            next = "display_all_tournaments"
        elif choice == "4":
            next = "display_tournament_round"
        elif choice == "5":
            next = "display_tournament_matches"

        return next, None

    @classmethod
    def display_all_players(cls, route_params=None):
        players = Store.get_players()
        
        print("1. By rank")
        print("2. In alphabetical order")
        filter = input("Choose a filter: ")

        if filter == "1":
            players = sorted(players, key=lambda x: x.rank, reverse=True)
        elif filter == "2":
            players = sorted(players, key=lambda x: x.first_name, reverse=False)
        
        choice = ReportsView.display_all_players(players)

        if choice == "1":
            next = "reports"
        elif choice.lower() == "h":
            next = "homepage"
            
        return next, None
    
    @classmethod
    def display_tournament_players(cls, route_params=None):
        tournaments = Store.get_tournaments()

        tournament_id = ReportsView.display_tournaments(tournaments)
        tournament = Store.get_tournament_by_id(tournament_id)

        print("1. By rank")
        print("2. In alphabetical order")
        filter = input("Choose a filter: ")

        if filter == "1":
            tournament.players = sorted(tournament.players, key=lambda x: x.rank, reverse=True)
        elif filter == "2":
            tournament.players = sorted(tournament.players, key=lambda x: x.first_name, reverse=False)

        choice = ReportsView.display_tournament_players(tournament.players)

        if choice == "1":
            next = "reports"
        elif choice.lower() == "h":
            next = "homepage"
            
        return next, None

    @classmethod
    def display_all_tournaments(cls, route_params=None):
        tournaments = Store.get_tournaments()

        choice = ReportsView.display_all_tournaments(tournaments)

        if choice == "1":
            next = "reports"
        elif choice.lower() == "h":
            next = "homepage"
            
        return next, None

    @classmethod
    def display_tournament_rounds(cls, route_params=None):
        tournaments = Store.get_tournaments()

        tournament_id = ReportsView.display_tournaments(tournaments)
        tournament = Store.get_tournament_by_id(tournament_id)

        choice = ReportsView.display_tournament_rounds(tournament)

        if choice == "1":
            next = "reports"
        elif choice.lower() == "h":
            next = "homepage"
            
        return next, None

    @classmethod
    def display_tournament_matches(cls, route_params=None):
        tournaments = Store.get_tournaments()

        tournament_id = ReportsView.display_tournaments(tournaments)
        tournament = Store.get_tournament_by_id(tournament_id)

        choice = ReportsView.display_tournament_matches(tournament)

        if choice == "1":
            next = "reports"
        elif choice.lower() == "h":
            next = "homepage"
            
        return next, None