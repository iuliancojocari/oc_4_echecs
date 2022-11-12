from chess.models.match import Match


class Round:

    def __init__(self, name, start_date, end_date="", matches=[]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches
    

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, store, dict):
        return cls(**{
            "name": dict["name"],
            "start_date": dict["start_date"],
            "end_date": dict["end_date"],
            "matches": [Match.from_dict(store, match) for match in dict["matches"]]
        })