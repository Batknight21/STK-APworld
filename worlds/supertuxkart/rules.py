from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rule_builder.rules import Has, HasAll, Rule
from . import tracks, difficulties

if TYPE_CHECKING:
    from .world import STKWorld

GP_LOCATIONS = [
    "Penguin Playground",
    "Off the Beat Entrack",
    "To the Moon and back",
    "At World Send"
]

def set_all_rules(world: STKWorld) -> None:
    set_normal_rules(world)
    set_completion_rule(world)

def set_normal_rules(world: STKWorld) -> None:
    for track in tracks.TRACKS:
        for difficulty in difficulties.DIFFICULTIES:
            if track.name == "Fort Magma": continue
            track_location = world.get_location(track.name + " " + difficulty.name)
            world.set_rule(track_location, Has(track.name, difficulty.id))

def set_completion_rule(world: STKWorld) -> None:
    pass
#    if world.options.goal == 0:
#        required_tracks = [track for track in tracks.TRACKS if not track.name == "Fort Magma"]
#
#        has_all_keys = Has("Key", world.options.required_keys.value)
#
#        world.set_completion_rule(has_all_keys & HasAll(*required_tracks))
#
#    elif world.options.goal == 1:
#        has_required_gps = Has(tracks.gps()[0].name, world.options.goal_difficulty + 1)
#        for track in tracks.gps():
#            if track == tracks.gps()[0]: continue
#            has_required_gps = has_required_gps & Has(track.name, world.options.goal_difficulty + 1)
#
#        world.set_completion_rule(has_required_gps)