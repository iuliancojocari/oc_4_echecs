from chess.models.player import Player
from chess.views.player_view import PlayerView
from chess.models.store import Store 


class PlayerController:

    @classmethod
    def list(cls, route_params=None):
        """
        List all tournaments controller
        """
        choice, player_id = PlayerView.display_list(Store.get_players())

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
    def create(cls, route_params=None):
        """
        Create new player controller
        """
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # we add the player to the store
        Store.save("players", Player(**data).to_dict())

        return "manage_players", None

    @classmethod
    def delete(cls, route_params):
        """
        Remove player from the database
        """
        # remove the player from the store
        Store.delete(id=route_params, table="players")
        
        return "manage_players", None

    @classmethod
    def update(cls, route_params):
        """
        Update player information
        """
        player_id = route_params
    
        data = PlayerView.update_player()
        
        Store.edit(id=player_id, dict=Player(player_id,**data).to_dict(), table="players")

        return "manage_players", None


        