from ..bases.item import *


class SpaceFloat(Item):
    pass


def load_me():
    this_item = SpaceFloat(
        set="1",  # str
        number=48,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Space Float",  # str
        image="48_Space_Float.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Weightless", "Item Rescue"],  # list[str](optional)
    )

    return this_item
