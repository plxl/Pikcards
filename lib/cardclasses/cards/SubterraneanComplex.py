from ..bases.exploration import *


class SubterraneanComplex(Exploration):
    pass


def load_me():
    this_exploration = SubterraneanComplex(
        set="2",  # str
        number=108,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Subterranean Complex",  # str
        image="108_Subterranean_Complex.png",  # str
        cardclass=1,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Subterranean Complex"],  # list[str](optional)
    )

    return this_exploration
