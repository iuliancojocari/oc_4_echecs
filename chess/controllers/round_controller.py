from chess.views.round_view import RoundView


class RoundController:

    @classmethod
    def show_round(cls, store, route_params):
        tournament = route_params
        choice, match = RoundView.show_round(tournament)

        if choice in ("1","2","3","4"):
            return "save_score", [tournament, match]
        else:
            return "play_tournament", tournament
