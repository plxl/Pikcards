from ..bases.item import *


class RepugnantAppendage(Item):
    pass


def load_me():
    this_item = RepugnantAppendage(
        set="2",  # str
        number=83,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Repugnant Appendage",  # str
        image="083_Repugnant_Appendage.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Steady Feet", "Speedy Feet"],  # list[str](optional)
    )

    return this_item
