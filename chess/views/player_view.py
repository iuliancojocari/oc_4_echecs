class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("Players list\n")
        print("ID\tFirst Name\tLast Name\tScore")
        for player in players:
            print(f"{player.id}\t{player.first_name}\t{player.last_name}\t")

        print("\n1. New player")
        print("2. Edit player")
        print("3. Delete player\n")
        print("Q. Exit")
        print("H. Homepage\n")

        choice = input("Choice: ")
        extra_info = None

        if choice in ("2", "3"):
            extra_info = int(input("Enter player Id: "))

        return choice, extra_info
    
    @classmethod
    def update_player(cls):
        print(f"Edit player \n")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_of_birth = input("Date of birth: ")
        sex = input("Sex (H or F): ")

        print("Player edited !")

        return {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "sex": sex
        }


    @classmethod
    def create_player(cls):
        print("New Player\n")
        id = int(input("ID: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        date_of_birth = input("Date of birth (DD-MM-YYYY): ")
        sex = input("Sex (H or F): ")
        
        return {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "sex": sex
        }
