class HomeView:

    @classmethod
    def home(cls):
        print("Welcome - Homepage\n")
        print("1. Manage players")
        print("2. Manage tournaments\n")
        print("Q. Exit\n")

        return input("Choice: ")
