from multiprocessing.resource_tracker import ResourceTracker
from chess.models.player import Player
from chess.models.tournament import Tournament
from chess.views.tournament_view import TournamentView

class TournamentController:

    @classmethod
    def get_tournament(cls, store, tournament_id):
        return next(t for t in store["tournaments"] if t.id == tournament_id)
    
    @classmethod
    def list(cls, store, route_params=None):
        """
        The method display the tournaments list

        Parameters : 
            store: tournaments list
            route_params: None

        Returns: 
            Returns the next route
        """

        choice, tournament_id = TournamentView.display_list(store.get_tournaments())

        if choice == "1":
            return "new_tournament", None
        elif choice == "2":
            return "load_tournament", tournament_id
        elif choice == "3":
            return "update_tournament", tournament_id
        elif choice == "4":
            return "delete_tournament", tournament_id
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit"
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        """
        The method create a new tournament

        Parameters: 
            store: tournaments list
            route_params: None

        Returns: 
            Return the next route -> manage_tournaments
        """
        data = TournamentView.create_tournament()

        store.save(table="tournaments", item=Tournament(**data).to_dict())

        return "manage_tournaments", None

    
    @classmethod
    def load(cls, store, route_params):
        tournament = store.load_tournament(route_params)
        
        choice = TournamentView.load_tournament(tournament)


        if choice == "1":
            if len(tournament.players) == 8:
                return "play_tournament", tournament.id
            else: 
                return "add_players", tournament.id
        elif choice == "2":
            return "manage_tournaments", None
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def players(cls, store, route_params):
        # route_params = tournament.id
        tournament = store.load_tournament(route_params)
        total_players = len(tournament.players)

        print(f"Tournament players -> {total_players}\n")

        if total_players < 8:
            players_to_add = 8 - total_players
        
        print(f"Add {players_to_add} players\n")

        nb_player = 1
        while total_players < 8:
            player_id = TournamentView.add_players(store.get_players())
            player = next(p for p in store.get_players() if p.id == int(player_id))
            store.add_players(id=tournament.id, dict=player.to_dict(), table="tournaments")

            total_players += 1
            nb_player += 1

        return "manage_tournaments", None

    
    @classmethod
    def update(cls, store, route_params):
        tournament_id = route_params

        for index, object in enumerate(store["tournaments"]):
            if object.id == tournament_id:
                data = TournamentView.update_tournament()
                store["tournaments"][index] = Tournament(tournament_id, **data)
            else:
                raise Exception(f"Tournament {tournament_id} not found")

        return "manage_tournaments", None

    @classmethod
    def delete(cls, store, route_params):
        store["tournaments"] = [
            t for t in store["tournaments"] if t.id != route_params
        ]

        return "manage_tournaments", None

    @classmethod
    def play_tournament(cls, store, route_params):
        # route_params -> tournament id
        # initiate the tournament
        tournament = store.load_tournament(route_params)

        round = len(tournament.rounds) + 1
        while round <= tournament.nb_rounds:
            r = tournament.create_round(round)
            store.save_round(id=tournament.id, dict=r.to_dict(), table="tournaments")

            choice = TournamentView.play_tournament(store.load_tournament(route_params))

            if choice == "1":
                return "play_round", tournament.id
            elif choice == "2":
                return "manage_tournaments", None
        
        return "manage_tournaments", None


                 
    @classmethod
    def play_round(cls, store, route_params):
        tournament = store.load_tournament(route_params)

        choice, match = TournamentView.play_round(tournament)

        if choice in ("1","2","3","4"):
            return "save_scores", [match, tournament.id]
        else:
            return "play_tournament", tournament.id

    @classmethod
    def save_scores(cls, store, route_params):
        match = route_params[0]
        tournament = store.load_tournament(route_params[1])
        
        choice = TournamentView.save_scores(match)
        null = None
        winner = None
        loser = None

        if choice == "1":
            winner = match.player_1.id
            loser = match.player_2.id
            store.save_results(tournament.id,match.name, "tournaments", match.update_results([1,0]))
        elif choice == "2":
            winner = match.player_2.id
            loser = match.player_1.id
            store.save_results(tournament.id,match.name, "tournaments", match.update_results([0,1]))
        elif choice == "3":
            null = {"player_1": match.player_1.id, "player_2": match.player_2.id}
            store.save_results(tournament.id, match.name, "tournaments", match.update_results([0.5,0.5]))



        
        scores = tournament.save_players_scores(winner, loser, null)
        print(type(scores))
        store.save_winner_score(tournament.id, "tournaments", scores)

        return "play_round", tournament.id





        



        