from ..bases.exploration import *


class ChallengeMode(Exploration):
    pass


def load_me():
    this_exploration = ChallengeMode(
        set="C",  # str
        number=35,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Challenge Mode",  # str
        image="35_Challenge_Mode.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_exploration
