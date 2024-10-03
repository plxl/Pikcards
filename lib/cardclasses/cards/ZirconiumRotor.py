from ..bases.item import *


class ZirconiumRotor(Item):
    pass


def load_me():
    this_item = ZirconiumRotor(
        set="1",  # str
        number=57,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Zirconium Rotor",  # str
        image="57_Zirconium_Rotor.png",  # str
        card_class=4,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Part Creation"],  # list[str](optional)
    )

    return this_item
