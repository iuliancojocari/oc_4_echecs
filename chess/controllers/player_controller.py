from chess.models.player import Player
from chess.views.player_view import PlayerView
from chess.models.database import Database


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        """table = store.table("players")
        players = table.all()
        choice, player_id = PlayerView.display_list(Player.from_dict(players))"""
        choice, player_id = PlayerView.display_list(store["players"])

        if choice == "1":
            return "new_player", None
        elif choice == "2":
            return "edit_player", player_id
        elif choice == "3":
            return "delete_player", player_id
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        player = Player(**data)

        # we add the player to the store
        store["players"].append(player)
        #Database.save(store, player)

        return "list_player", None

    @classmethod
    def delete(cls, store, route_params):
        # remove the player from the store
        store["players"] = [
            p for p in store["players"] if p.id != route_params
        ]
        return "manage_players", None

    @classmethod
    def update(cls, store, route_params):
        """
        Update player information

        Attributes : 
        -   store : the list of players
        -   route_params : the player ID
        """

        player_id = route_params

        for index, object in enumerate(store["players"]):
            if object.id == player_id:
                data = PlayerView.update_player()
                store["players"][index] = Player(player_id, **data)
            else: 
                raise Exception(f"Player {player_id} not found")
            
        return "manage_players", None


        