from ..bases.item import *


class DreamSeries(Item):
    pass


def load_me():
    this_item = DreamSeries(
        set="2",  # str
        number=71,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Dream Series",  # str
        image="071_Dream_Series.png",  # str
        card_class=4,  # int
        base_energy=2,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_item
