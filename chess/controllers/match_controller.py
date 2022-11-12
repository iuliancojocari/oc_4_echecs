from chess.models.match import Match
from chess.views.match_view import MatchView


class MatchController:

    @classmethod
    def save_score(cls, route_params):
        match = route_params[1]
        tournament = route_params[0]

        winner = MatchView.save_score(match)
        match.update_score(winner)

        return "show_round", tournament
    