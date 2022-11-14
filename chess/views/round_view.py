class RoundView:
    @classmethod
    def show_round(cls, tournament):
        # we select the last "round" of the list
        round = tournament.rounds[-1]

        # show matchs list
        print(f"{round.name}")
        for match in round.matchs:
            text = (
                f"\t{match.name} - {match.player_1.first_name} {match.player_1.last_name}"
                f" vs {match.player_2.first_name} {match.player_2.last_name} - {match.results}"
            )
            print(text)

        # show options
        for match in round.matchs:
            options = 0
            if len(match.results) == 0:
                print(f"Enter results match {match.name}")
                options += 1

        if options == 0:
            choice = "0"
            return choice, None
        else:
            choice = input("Choice: ")
            extra_info = None

            if choice == "1":
                extra_info = round.matchs[0]
            elif choice == "2":
                extra_info = round.matchs[1]
            elif choice == "3":
                extra_info = round.matchs[2]
            elif choice == "4":
                extra_info = round.matchs[3]

            return choice, extra_info
