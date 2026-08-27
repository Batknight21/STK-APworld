from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import STKWorld

def create_all_regions(world: STKWorld) -> None:
    overworld = Region("Overworld", world.player, world.multiworld)
    world.multiworld.regions += [overworld]