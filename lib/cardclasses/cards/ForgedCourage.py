from ..bases.item import *


class ForgedCourage(Item):
    pass


def load_me():
    this_item = ForgedCourage(
        set="2",  # str
        number=85,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Forged Courage",  # str
        image="085_Forged_Courage.png",  # str
        cardclass=4,  # int
        base_energy=3,  # int
        base_time=1,  # int
        elements=["Fire"],  # list[str]
        immunities=["Fire"],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_item
