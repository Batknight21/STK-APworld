from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import util, tracks
from .difficulties import DIFFICULTIES

from . import options as stk_options

if TYPE_CHECKING:
    from .world import STKWorld

def get_location_to_id() -> dict[str, int]:
    locations: dict[str, int] = {}
    for track in tracks.locked():
        locations[track.name + " Unlock"] = track.id

    for difficulty in DIFFICULTIES:
        for track in tracks.TRACKS:
            element = track.name + " " + difficulty.name
            locations[element] = util.get_track_id(difficulty.id, track.id)

    return locations

class STKLocation(Location):
    game = "Super Tux Kart"

def create_all_locations(world: STKWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: STKWorld) -> None:
    overworld = world.get_region("Overworld")
    overworld.add_locations(get_location_to_id(), STKLocation)

def create_events(world: STKWorld) -> None:
    overworld = world.get_region("Overworld")

#    if world.options.goal == 0:
#        overworld.add_event("Fort Magma Goal Completed", "Victory", location_type=STKLocation, item_type=items.STKItem)
#
#    elif world.options.goal == 1:
#        overworld.add_event("Gp Goal Completed", "Victory", location_type=STKLocation, item_type=items.STKItem)
