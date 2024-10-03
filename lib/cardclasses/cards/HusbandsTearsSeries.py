from ..bases.item import *


class HusbandsTearsSeries(Item):
    pass


def load_me():
    this_item = HusbandsTearsSeries(
        set="2",  # str
        number=68,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Husband's Tears Series",  # str
        image="068_Husband's_Tears_Series.png",  # str
        cardclass=4,  # int
        base_energy=1,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Power Boost"],  # list[str](optional)
    )

    return this_item
