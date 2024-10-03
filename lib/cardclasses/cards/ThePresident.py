from ..bases.minion import *


class ThePresident(Minion):
    pass


def load_me():
    this_minion = ThePresident(
        set="2",  # str
        number=2,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="The President",  # str
        image="002_The_President.png",  # str
        cardclass=2,  # int
        base_energy=5,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Burrowing"],  # list[str]
        base_attack=0,  # int
        base_health=7,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Inflict Debt", "Conjure"],  # list[str](optional)
    )

    return this_minion
