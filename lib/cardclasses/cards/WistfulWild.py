from ..bases.area import *


class WistfulWild(Area):
    pass


def load_me():
    this_area = WistfulWild(
        set="2",  # str
        number=106,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Wistful Wild",  # str
        image="106_Wistful_Wild.png",  # str
        cardclass=1,  # int
        base_energy=5,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Wistful Wild"],  # list[str](optional)
    )

    return this_area
