from ..bases.item import *


class FallingBoulders(Item):
    pass


def load_me():
    this_item = FallingBoulders(
        set="0",  # str
        number=0,  # int
        fifth=False,  # bool
        rarity=-1,  # int
        name="Falling Boulders",  # str
        image="Falling_Boulders.png",  # str
        cardclass=0,  # int
        base_energy=1,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Weightless", "Rockfall"],  # list[str](optional)
    )

    return this_item
