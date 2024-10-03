from ..bases.item import *


class TheKey(Item):
    pass


def load_me():
    this_item = TheKey(
        set="2",  # str
        number=90,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="The Key",  # str
        image="090_The_Key.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_item
