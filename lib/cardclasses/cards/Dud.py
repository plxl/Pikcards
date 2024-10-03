from ..bases.item import *


class Dud(Item):
    pass


def load_me():
    this_item = Dud(
        set="0",  # str
        number=0,  # int
        fifth=False,  # bool
        rarity=-1,  # int
        name="Dud",  # str
        image="Dud.png",  # str
        card_class=0,  # int
        base_energy=0,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Dud"],  # list[str](optional)
    )

    return this_item
