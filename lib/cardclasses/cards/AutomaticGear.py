from ..bases.item import *


class AutomaticGear(Item):
    pass


def load_me():
    this_item = AutomaticGear(
        set="1",  # str
        number=49,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Automatic Gear",  # str
        image="49_Automatic_Gear.png",  # str
        card_class=1,  # int
        base_energy=4,  # int
        base_time=8,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Element Spin", "One-Time Use"],  # list[str](optional)
    )

    return this_item
