from typing import Mapping, Any

from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world
from . import options as stk_options

class STKWorld(World):
    """
    SuperTuxKart is an open source racing game with a story mode unlike many others.
    Can you beat nolok in a race?
    """

    game = "Super Tux Kart"

    web = web_world.STKWebWorld()

    options_dataclass = stk_options.STKOptions
    options: stk_options.STKOptions

    location_name_to_id = locations.get_location_to_id()
    item_name_to_id = items.get_items_to_id()

    origin_region_name = "Overworld"

    def create_regions(self) -> None:
        regions.create_all_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.STKItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal", "goal_difficulty", "required_keys", "required_points",
            "nitro", "skid", "look_back", "death_link", "death_link_send_mode", "death_link_receive_mode"
        )