from ..bases.item import *


class UVLamp(Item):
    pass


def load_me():
    this_item = UVLamp(
        set="1",  # str
        number=61,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="UV Lamp",  # str
        image="61_UV_Lamp.png",  # str
        card_class=2,  # int
        base_energy=1,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Lure"],  # list[str](optional)
    )

    return this_item
