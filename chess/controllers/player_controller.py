from chess.models.player import Player
from chess.views.player_view import PlayerView
from chess.models.store import Store 


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, player_id = PlayerView.display_list(store.get_players())

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
        #player = Player(**data)

        # we add the player to the store
        #store["players"].append(player)
        #Database.save(store, player)
        store.save("players", Player(**data).to_dict())

        return "manage_players", None

    @classmethod
    def delete(cls, store, route_params):
        # remove the player from the store
        store.delete(id=route_params, table="players")
        
        return "manage_players", None

    @classmethod
    def update(cls, store, route_params):
        """
        Update player information
        """

        player_id = route_params
    
        data = PlayerView.update_player()
        
        store.edit(id=player_id, dict=Player(player_id,**data).to_dict(), table="players")

            
        return "manage_players", None


        