from chess.views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store=None, input=None):
        choice = HomeView.home()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "manage_players"
        elif choice == "2":
            next = "manage_tournaments"
        return next, None
