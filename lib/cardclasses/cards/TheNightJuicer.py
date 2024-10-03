from ..bases.exploration import *


class TheNightJuicer(Exploration):
    pass


def load_me():
    this_exploration = TheNightJuicer(
        set="C",  # str
        number=17,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="The Night Juicer",  # str
        image="17_The_Night_Juicer.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["The Night Juicer"],  # list[str](optional)
    )

    return this_exploration
