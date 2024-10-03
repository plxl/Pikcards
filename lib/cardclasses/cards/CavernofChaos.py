from ..bases.exploration import *


class CavernofChaos(Exploration):
    pass


def load_me():
    this_exploration = CavernofChaos(
        set="2",  # str
        number=118,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Cavern of Chaos",  # str
        image="118_Cavern_of_Chaos.png",  # str
        card_class=3,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Cavern of Chaos"],  # list[str](optional)
    )

    return this_exploration
