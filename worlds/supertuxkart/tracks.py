from enum import IntEnum

class UnlockDifficulty(IntEnum):
    LOCKED = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    SUPER_TUX = 4

class Track:
    name: str
    id: int
    unlock: UnlockDifficulty

    def __init__(self, name: str, track_id: int, unlock: UnlockDifficulty):
        self.name = name
        self.id = track_id
        self.unlock = unlock

TRACKS = [
    Track("Cornfield Crossing", 1, UnlockDifficulty.EASY),
    Track("Snow Peak", 2, UnlockDifficulty.EASY),
    Track("Volcan Island", 3, UnlockDifficulty.EASY),
    Track("Hacienda", 4, UnlockDifficulty.EASY),
    Track("Ravenbridge Mansion", 5, UnlockDifficulty.EASY),
    Track("Antediluvian Abyss", 6, UnlockDifficulty.EASY),
    Track("Nessie's Pond", 7, UnlockDifficulty.EASY),
    Track("Oliver Math", 8, UnlockDifficulty.LOCKED),
    Track("Gran Paradiso Island", 9, UnlockDifficulty.LOCKED),
    Track("Candela City", 10, UnlockDifficulty.LOCKED),
    Track("Light House", 11, UnlockDifficulty.LOCKED),
    Track("Snow Mountain", 12, UnlockDifficulty.LOCKED),
    Track("Minigolf", 13, UnlockDifficulty.LOCKED),
    Track("Black Forest", 14, UnlockDifficulty.LOCKED),
    Track("Mines", 15, UnlockDifficulty.LOCKED),
    Track("Shifting Sands", 16, UnlockDifficulty.EASY),
    Track("Zen Garden", 17, UnlockDifficulty.LOCKED),
    Track("STK Enterprise", 18, UnlockDifficulty.LOCKED),
    Track("xr591", 19, UnlockDifficulty.LOCKED),
    Track("Cocoa Temple", 20, UnlockDifficulty.LOCKED),
    Track("Penguin Playground", 21, UnlockDifficulty.LOCKED),
    Track("Off the Beaten Track", 22, UnlockDifficulty.LOCKED),
    Track("To the Moon and back", 23, UnlockDifficulty.LOCKED),
    Track("At World's End", 24, UnlockDifficulty.LOCKED),
    Track("Fort Magma", 25, UnlockDifficulty.SUPER_TUX)
]

def by_name(name: str) -> Track | None:
    for track in TRACKS:
        if track.name == name:
            return track

    return None

def locked() -> list[Track]:
    return [track for track in TRACKS if track.unlock == UnlockDifficulty.LOCKED]

def pre_unlocked() -> list[Track]:
    return [track for track in TRACKS if not track.unlock == UnlockDifficulty.LOCKED]

def gps() -> list[Track]:
    return [
        Track("Penguin Playground", 21, UnlockDifficulty.LOCKED),
        Track("Off the Beaten Track", 22, UnlockDifficulty.LOCKED),
        Track("To the Moon and back", 23, UnlockDifficulty.LOCKED),
        Track("At World's End", 24, UnlockDifficulty.LOCKED),
    ]