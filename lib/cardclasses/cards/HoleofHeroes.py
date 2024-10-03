from ..bases.exploration import *


class HoleofHeroes(Exploration):
    pass


def load_me():
    this_exploration = HoleofHeroes(
        set="2",  # str
        number=119,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Hole of Heroes",  # str
        image="119_Hole_of_Heroes.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Hole of Heroes"],  # list[str](optional)
    )

    return this_exploration
