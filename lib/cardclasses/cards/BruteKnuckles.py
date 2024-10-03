from ..bases.item import *


class BruteKnuckles(Item):
    pass


def load_me():
    this_item = BruteKnuckles(
        set="2",  # str
        number=82,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Brute Knuckles",  # str
        image="082_Brute_Knuckles.png",  # str
        cardclass=1,  # int
        base_energy=5,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Digging", "Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Power Punch"],  # list[str](optional)
    )

    return this_item
