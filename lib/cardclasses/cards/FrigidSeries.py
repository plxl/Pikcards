from ..bases.item import *


class FrigidSeries(Item):
    pass


def load_me():
    this_item = FrigidSeries(
        set="2",  # str
        number=65,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Frigid Series",  # str
        image="065_Frigid_Series.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Draw"],  # list[str](optional)
    )

    return this_item
