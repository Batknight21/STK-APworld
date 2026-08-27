from worlds.AutoWorld import WebWorld
from .options import option_groups

class STKWebWorld(WebWorld):
    game = "Super Tux Kart"
    theme = "dirt"
    tutorials = []
    option_groups = option_groups