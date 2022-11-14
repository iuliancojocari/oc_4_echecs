from chess.models.tournament import Tournament
from chess.models.store import Store
from chess.views.tournament_view import TournamentView


class TournamentController:
    @classmethod
    def list(cls, route_params=None):
        """
        The method display the tournaments list

        Parameters :
            route_params: None

        Returns:
            Returns the next route
        """

        choice, tournament_id = TournamentView.display_list(Store.get_tournaments())

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
    def create(cls, route_params=None):
        """
        The method create a new tournament

        Parameters:
            route_params: None

        Returns:
            Return the next route -> manage_tournaments
        """
        data = TournamentView.create_tournament()

        Store.save(table="tournaments", dict=Tournament(**data).to_dict())

        return "manage_tournaments", None

    @classmethod
    def load(cls, route_params):
        """
        Load tournament by id

        Parameters:
        - route_params : tournament id
        """
        tournament = Store.get_tournament_by_id(route_params)

        choice = TournamentView.load_tournament(tournament)

        if choice == "1":
            if len(tournament.players) == 8:
                return "play_tournament", tournament.id
            else:
                return "add_tournament_players", tournament.id
        elif choice == "2":
            return "manage_tournaments", None
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def update(cls, route_params):
        data = TournamentView.update_tournament()

        Store.edit(
            route_params, Tournament(route_params, **data).to_dict(), "tournaments"
        )

        return "manage_tournaments", None

    @classmethod
    def delete(cls, route_params):
        """
        Delete tournament

        Parameters:
        - route_params : tournament id
        """
        Store.delete(route_params, "tournaments")

        return "manage_tournaments", None

    @classmethod
    def add_tournament_players(cls, route_params):
        """
        Add tournament players (8 players by default)

        Parameters:
        - route params : tournament id
        """
        # route_params = tournament.id
        tournament = Store.get_tournament_by_id(route_params)
        total_players = len(tournament.players)

        print(f"Tournament players -> {total_players}\n")

        if total_players < 8:
            players_to_add = 8 - total_players

        print(f"Add {players_to_add} players\n")

        nb_player = 1
        while total_players < 8:
            player_id = TournamentView.add_players(Store.get_players())
            player = next(p for p in Store.get_players() if p.id == int(player_id))

            tournament.players.append(player)
            Store.update_tournament_info(
                id=tournament.id, dict=tournament.to_dict(), table="tournaments"
            )
            # Store.add_players(id=tournament.id, dict=player.id, table="tournaments")

            total_players += 1
            nb_player += 1

        return "play_tournament", None

    @classmethod
    def play_tournament(cls, route_params):
        """
        Play tournament

        Parameters:
        - route_params : tournament id
        """
        # initiate the tournament
        tournament = Store.get_tournament_by_id(route_params)

        round = len(tournament.rounds) + 1

        while round <= tournament.nb_rounds:
            tournament.create_round(round)

            Store.update_tournament_info(
                id=tournament.id, dict=tournament.to_dict(), table="tournaments"
            )

            choice = TournamentView.play_tournament(
                Store.get_tournament_by_id(route_params)
            )

            if choice == "1":
                return "play_round", tournament.id
            elif choice == "2":
                return "manage_tournaments", None

        return "update_player_ranking", None

    @classmethod
    def play_round(cls, route_params):
        """
        Play round

        Parameters:
        - route_params : tournament id
        """
        tournament = Store.get_tournament_by_id(route_params)

        choice, match = TournamentView.play_round(tournament)

        if choice in ("1", "2", "3", "4"):
            return "save_scores_and_results", [match, tournament.id]
        else:
            return "play_tournament", tournament.id

    @classmethod
    def save_scores_and_results(cls, route_params):
        """
        Save scores and match results
        """
        match = route_params[0]
        match_name = match.name
        tournament = Store.get_tournament_by_id(route_params[1])

        choice = TournamentView.save_scores(match)

        # get matches of the last round
        for match in tournament.rounds[-1].matches:
            if match_name == match.name:
                null = None
                winner = None
                loser = None
                if choice == "1":
                    winner = match.player_1.id
                    loser = match.player_2.id
                    # update match results
                    match.update_results(winner, loser, null)
                elif choice == "2":
                    winner = match.player_2.id
                    loser = match.player_1.id
                    # update match results
                    match.update_results(winner, loser, null)
                elif choice == "3":
                    null = {
                        "player_1": match.player_1.id,
                        "player_2": match.player_2.id,
                    }
                    # update match results
                    match.update_results(winner, loser, null)

        # save players scores
        tournament.save_players_scores(winner, loser, null)

        # set the round end_date
        tournament.set_round_end_date(tournament.rounds[-1])

        # refresh the record in the database
        Store.update_tournament_info(
            id=tournament.id,
            dict=tournament.to_dict(),
            table="tournaments",
        )

        return "play_round", tournament.id
