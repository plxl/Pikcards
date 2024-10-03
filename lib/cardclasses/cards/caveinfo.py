from ..bases.exploration import *


class caveinfo(Exploration):
    pass


def load_me():
    this_exploration = caveinfo(
        set="C",  # str
        number=36,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="caveinfo",  # str
        image="36_caveinfo.png",  # str
        cardclass=5,  # int
        base_energy=0,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["caveinfo"],  # list[str](optional)
    )

    return this_exploration
