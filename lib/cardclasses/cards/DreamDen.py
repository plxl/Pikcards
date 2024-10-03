from ..bases.exploration import *


class DreamDen(Exploration):
    pass


def load_me():
    this_exploration = DreamDen(
        set="2",  # str
        number=120,  # int
        fifth=True,  # bool
        rarity=2,  # int
        name="Dream Den",  # str
        image="120_Dream_Den.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Dream Den"],  # list[str](optional)
    )

    return this_exploration
