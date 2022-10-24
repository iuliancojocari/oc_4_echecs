class Player:
    def __init__(self, id, first_name, last_name, date_of_birth, sex, rank=0) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank