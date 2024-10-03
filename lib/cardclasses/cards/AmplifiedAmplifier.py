from ..bases.item import *


class AmplifiedAmplifier(Item):
    pass


def load_me():
    this_item = AmplifiedAmplifier(
        set="2",  # str
        number=88,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Amplified Amplifier",  # str
        image="088_Amplified_Amplifier.png",  # str
        cardclass=4,  # int
        base_energy=3,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_item
