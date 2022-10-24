class MatchView: 

    @classmethod
    def save_score(self, match):
        print(f"{match.name}\n")
        print(f"Winner:")
        print(f"\t1. {match.players_pairs[0].first_name}")
        print(f"\t2. {match.players_pairs[1].first_name}")
        print(f"\t3. Null")

        choice = input("\nChoice: ")

        return choice
