from test.bases import WorldTestBase
from ..world import STKWorld

class STKTestBase(WorldTestBase):
    game = "Super Tux Kart"
    world: STKWorld