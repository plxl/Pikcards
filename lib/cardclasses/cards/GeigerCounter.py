from ..bases.item import *


class GeigerCounter(Item):
    pass


def load_me():
    this_item = GeigerCounter(
        set="1",  # str
        number=64,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Geiger Counter",  # str
        image="64_Geiger_Counter.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Immunity Warning"],  # list[str](optional)
    )

    return this_item
