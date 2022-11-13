class Player:
    def __init__(self, id, first_name, last_name, date_of_birth, sex, rank=0) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank

    def to_dict(self):
        """
        Serialize player object
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "rank": self.rank
        }

    @classmethod
    def from_dict(cls, player_dict):
        """
        Deserialize player object
        """
        return cls(**{
            "id": player_dict["id"],
            "first_name": player_dict["first_name"],
            "last_name": player_dict["last_name"],
            "date_of_birth": player_dict["date_of_birth"],
            "sex": player_dict["sex"],
            "rank": player_dict["rank"]
        })        
        

  