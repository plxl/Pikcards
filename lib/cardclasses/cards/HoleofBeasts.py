from ..bases.exploration import *


class HoleofBeasts(Exploration):
    pass


def load_me():
    this_exploration = HoleofBeasts(
        set="2",  # str
        number=110,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Hole of Beasts",  # str
        image="110_Hole_of_Beasts.png",  # str
        cardclass=4,  # int
        base_energy=0,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Hole of Beasts"],  # list[str](optional)
    )

    return this_exploration
