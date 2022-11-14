class ReportsView:

    @classmethod
    def display_menu(cls):
        print("1. List all players")
        print("2. List all tournament players")
        print("3. List all tournaments")
        print("4. List all tournament rounds")
        print("5. List all tournament matches\n")
        print("H. Homepage")

        choice = input("Choice: ")

        return choice

    @classmethod
    def display_all_players(cls, players):
        

        print("ID\tFirst Name\tLast Name\tDate of birth\tSex\tRank")
        for player in players:
            print(f"{player.id}\t{player.first_name}\t{player.last_name}\t{player.date_of_birth}\t{player.sex}\t{player.rank}")

        print("\n1. Reports")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def display_tournaments(cls, tournaments):
        for tournament in tournaments:
            print(
                f"{tournament.id}\t{tournament.name}\t{tournament.location}\t{tournament.date}\t"
            )

        choice = int(input("\nEnter tournament id : "))

        return choice
    
    @classmethod
    def display_tournament_players(cls, players):
        for player in players:
            print(f"{player.id}\t{player.first_name}\t{player.last_name}\t{player.date_of_birth}\t{player.sex}\t{player.rank}")
        
        print("\n1. Reports")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def display_all_tournaments(cls, tournaments):
        print("ID\tName\tDescription\nLocation\tDate\tTime Control")
        for tournament in tournaments:
            print( f"{tournament.id}\t{tournament.name}\t{tournament.description}\t{tournament.location}\t{tournament.date}\t{tournament.time_control}")

        print("\n1. Reports")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def display_tournament_rounds(cls, tournament):
        print("\nRound Name\tStart date\tEnd Date")
        for round in tournament.rounds:
            print(f"{round.name}\t{round.start_date}\t{round.end_date}")


        print("\n1. Reports")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice

    @classmethod
    def display_tournament_matches(cls, tournament):
        for round in tournament.rounds:
            print(f"\n->{round.name}:")

            for match in round.matches:
                print(
                    f"# {match.name} - {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} - Results : {match.results}"
                )

        print("\n1. Reports")
        print("H. Homepage\n")

        choice = input("Choice: ")

        return choice