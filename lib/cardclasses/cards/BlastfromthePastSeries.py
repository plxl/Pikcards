from ..bases.item import *


class BlastfromthePastSeries(Item):
    pass


def load_me():
    this_item = BlastfromthePastSeries(
        set="2",  # str
        number=72,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Blast from the Past Series",  # str
        image="072_Blast_from_the_Past_Series.png",  # str
        card_class=2,  # int
        base_energy=3,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_item
