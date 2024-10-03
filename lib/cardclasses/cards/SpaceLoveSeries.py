from ..bases.item import *


class SpaceLoveSeries(Item):
    pass


def load_me():
    this_item = SpaceLoveSeries(
        set="2",  # str
        number=69,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Space Love Series",  # str
        image="069_Space_Love_Series.png",  # str
        cardclass=2,  # int
        base_energy=0,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Health Boost"],  # list[str](optional)
    )

    return this_item
