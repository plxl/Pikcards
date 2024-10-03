from ..bases.item import *


class Sagittarius(Item):
    pass


def load_me():
    this_item = Sagittarius(
        set="1",  # str
        number=46,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Sagittarius",  # str
        image="46_Sagittarius.png",  # str
        card_class=2,  # int
        base_energy=3,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Converge Power"],  # list[str](optional)
    )

    return this_item
