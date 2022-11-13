from chess.controllers.timestamp import get_timestamp


class TournamentView:
    @classmethod
    def display_list(cls, tournaments):
        print("List of tournaments\n")
        print("ID\tName\tLocation\tDate")

        for tournament in tournaments:
            print(
                f"{tournament.id}\t{tournament.name}\t{tournament.location}\t{tournament.date}"
            )

        if len(tournaments) == 0:
            print("\n1. New tournament")
        else:
            print("\n1. New tournament")    
            print("2. Load tournament")
            print("3. Edit tournament")
            print("4. Delete tournament\n")
        print("H. Homepage")
        print("Q. Exit\n")

        choice = input("Choice: ")
        extra_info = None

        if choice in ("2", "3", "4"):
            extra_info = int(input("\nEnter tournament Id: "))

        return choice, extra_info

    @classmethod
    def create_tournament(cls):
        print("Create tournament\n")
        id = input("Id: ")
        name = input("Name: ")
        location = input("Location: ")
        date = input("Date (DD-MM-YYYY): ")
        description = input("Description: ")
        print("Time control:\n\t1. Bullet\n\t2. Blitz\n\t3. Coup rapide")
        choice = input("Time control option : ")
        if choice == "1":
            time_control = "Bullet"
        elif choice == "2":
            time_control = "Blitz"
        elif choice == "3":
            time_control = "Coup rapide"

        return {
            "id": id,
            "name": name,
            "location": location,
            "date": date,
            "description": description,
            "time_control": time_control,
        }

    @classmethod
    def load_tournament(cls, tournament):
        print("Tournament overview\n")
        print(f"Id: {tournament.id}")
        print(f"Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Date: {tournament.date}")
        print("Players : ")
        print("\tID\tFirst Name\tLast Name")
        for player in tournament.players:
            print(f"\t{player.id}\t{player.first_name}\t{player.last_name}")

        if len(tournament.players) == 8:
            if len(tournament.rounds) == tournament.nb_rounds:
                print("\nTournament finished !\n")
            else:
                print("\n1. Play tournament")
        elif len(tournament.rounds) == tournament.nb_rounds:
            print("Tournament finished !")
        else:
            print("\n1. Add player to the tournament")
        print("2. Manage tournaments")

        print("\nQ. Exit")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def update_tournament(cls):
        print(f"Update tournament\n")

        name = input("Name: ")
        location = input("Location: ")
        date = input("Date (DD-MM-YYYY): ")
        description = input("Description: ")

        return {
            "name": name,
            "location": location,
            "date": date,
            "description": description,
        }

    @classmethod
    def add_players(cls, players):
        print("ID\tFirst Name\tLast Name")
        for player in players:
            print(f"{player.id}\t{player.first_name}\t{player.last_name}")

        choice = input("Enter Id: ")

        return choice

    @classmethod
    def play_tournament(cls, tournament):
        print(f"Id: {tournament.id}")
        print(f"Name : {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Date: {tournament.date}")
        print("Players : ")
        print("\tID\tFirst Name\tLast Name\tRank")
        for player in tournament.players:
            print(
                f"\t{player.id}\t{player.first_name}\t{player.last_name}\t{player.rank}"
            )
        
        for round in tournament.rounds:
            print(f"\n->{round.name}:")

            for match in round.matches:
                print(
                    f"# {match.name} - {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} - Results : {match.results}"
                )

        round = len(tournament.rounds)
        print(f"\n1. Play round {round}")
        print("2. Manage tournaments\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def play_round(cls, tournament):
        # we select the last "round" of the list
        round = tournament.rounds[-1]

        # show matchesess list
        print(f"{round.name}:")
        for match in round.matches:
            print(
                f"# {match.name} - {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} - {match.results}"
            )
        print("")
        # show options
        options = 0
        for match in range(len(round.matches)):
            if len(round.matches[match].results) == 0:
                print(f"{match + 1}. Enter results - {round.matches[match].name}")
                options += 1
        
        if options == 0:
            return "0", None
        else: 
            choice = input("\nChoice: ")
            extra_info = None

            if choice == "1":
                extra_info = round.matches[0]
            elif choice == "2":
                extra_info = round.matches[1]
            elif choice == "3":
                extra_info = round.matches[2]
            elif choice == "4":
                extra_info = round.matches[3]

            return choice, extra_info
            
    
    @classmethod
    def save_scores(cls, match):
        print("Winner:\n")
        print(f"1. {match.player_1.first_name} {match.player_1.last_name}")
        print(f"2. {match.player_2.first_name} {match.player_2.last_name}")
        print("3. Match null")

        choice = input("\nChoice: ")

        return choice