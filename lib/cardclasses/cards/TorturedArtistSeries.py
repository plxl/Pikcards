from ..bases.item import *


class TorturedArtistSeries(Item):
    pass


def load_me():
    this_item = TorturedArtistSeries(
        set="2",  # str
        number=63,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Tortured Artist Series",  # str
        image="063_Tortured_Artist_Series.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=["Poison", "Gloom", "Piercing"],  # list[str]
        immunities=["Water", "First Strike"],  # list[str]
        traits=["Explorer", "Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_item
