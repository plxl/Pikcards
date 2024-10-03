from ..bases.area import *


class TheFinalTrial(Area):
    pass


def load_me():
    this_area = TheFinalTrial(
        set="1",  # str
        number=80,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="The Final Trial",  # str
        image="80_The_Final_Trial.png",  # str
        cardclass=1,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Final Trial"],  # list[str](optional)
    )

    return this_area
