from ..bases.exploration import *


class FrontierCavern(Exploration):
    pass


def load_me():
    this_exploration = FrontierCavern(
        set="2",  # str
        number=109,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Frontier Cavern",  # str
        image="109_Frontier_Cavern.png",  # str
        cardclass=3,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Frontier Cavern"],  # list[str](optional)
    )

    return this_exploration
