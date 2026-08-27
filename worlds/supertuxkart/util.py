from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import STKWorld

def get_track_id(difficulty: int, index: int) -> int:
    return int(f"{difficulty}{index:02d}")

def create_race_locations_for_difficulties(race_locations: list[str], prev: dict[str, int]) -> dict[str, int]:
    locations_to_ids: dict[str, int] = prev
    index = 0
    difficulties: dict[int, str] = {1: "Easy", 2 :"Normal", 3: "Hard", 4: "Supertux"}
    for difficulty_index in difficulties.keys():
        for race_location in race_locations:
            element = race_location + " " + difficulties[difficulty_index]
            locations_to_ids[element] = get_track_id(difficulty_index, index)
            index = index + 1
        index = 0

    return locations_to_ids
