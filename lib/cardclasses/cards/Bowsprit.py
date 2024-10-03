from ..bases.item import *


class Bowsprit(Item):
    pass


def load_me():
    this_item = Bowsprit(
        set="1",  # str
        number=68,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Bowsprit",  # str
        image="68_Bowsprit.png",  # str
        card_class=3,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Defense Boost"],  # list[str](optional)
    )

    return this_item
