from ..bases.item import *


class AnalogComputer(Item):
    pass


def load_me():
    this_item = AnalogComputer(
        set="1",  # str
        number=52,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Analog Computer",  # str
        image="52_Analog_Computer.png",  # str
        card_class=1,  # int
        base_energy=2,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Copy"],  # list[str](optional)
    )

    return this_item
