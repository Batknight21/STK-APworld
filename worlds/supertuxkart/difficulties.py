class Difficulty:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

DIFFICULTIES = [
    Difficulty("Easy", 1),
    Difficulty("Normal", 2),
    Difficulty("Hard", 3),
    Difficulty("Supertux", 4)
]