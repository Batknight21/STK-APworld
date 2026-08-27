from __future__ import annotations

from typing import TYPE_CHECKING, List

from BaseClasses import ItemClassification, Item

from . import tracks, util

if TYPE_CHECKING:
    from .world import STKWorld

NORMAL_ITEMS = {
    "Speed Boost": 26,
    "Nitro Canister": 27,
    "Random Powerup": 28,
    "Banana Trap": 29,
    "Nitro Ability": 30,
    "Skid Ability": 31,
    "Look Back Ability": 32,
    "Key": 33
}

NORMAL_ITEM_CLASSIFICATIONS = {
    "Speed Boost": ItemClassification.filler,
    "Nitro Canister": ItemClassification.filler,
    "Random Powerup": ItemClassification.filler,
    "Banana Trap": ItemClassification.trap,
    "Nitro Ability": ItemClassification.useful,
    "Skid Ability": ItemClassification.useful,
    "Look Back Ability": ItemClassification.useful,
    "Key": ItemClassification.progression
}

class STKItem(Item):
    game = "Super Tux Kart"

def get_items_to_id() -> dict[str, int]:
    items: dict[str, int] = {}
    for track in tracks.TRACKS:
        items[track.name] = track.id

    for item in NORMAL_ITEMS.keys():
        items[item] = NORMAL_ITEMS[item]

    return items

def get_random_filler_item_name(world: STKWorld) -> str:
    match world.random.randint(0, 1):
        case 0:
            return "Random Powerup"
        case 1:
            return "Nitro Canister"
    return "Random Powerup"

def create_item_with_correct_classification(world: STKWorld, name: str) -> STKItem:
    classification: ItemClassification
    item_id: int
    track = tracks.by_name(name)

    if not track is None:
        classification = ItemClassification.progression
        item_id = track.id

    else:
        classification = NORMAL_ITEM_CLASSIFICATIONS[name]
        item_id = NORMAL_ITEMS[name]

    return STKItem(name, classification, item_id, world.player)

def create_all_items(world: STKWorld) -> None:
    items: list[str] = []

    for track in tracks.TRACKS:
        for i in range(4):
            items.append(track.name)

    if world.options.nitro:
        items += ["Nitro Ability"]

    if world.options.skid:
        items += ["Skid Ability"]

    if world.options.look_back:
        items += ["Look Back Ability"]

    for i in range(world.options.generated_keys):
        items.append("Key")

    itempool: list[Item] = [world.create_item(item) for item in items]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    for track in tracks.pre_unlocked():
        for i in range(track.unlock):
            world.push_precollected(world.create_item(track.name))
