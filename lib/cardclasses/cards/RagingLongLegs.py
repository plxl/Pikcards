from ..bases.minion import *


class RagingLongLegs(Minion):
    pass


def load_me():
    this_minion = RagingLongLegs(
        set="2",  # str
        number=49,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Raging Long Legs",  # str
        image="049_Raging_Long_Legs.png",  # str
        cardclass=3,  # int
        base_energy=7,  # int
        base_time=4,  # int
        elements=["Crush"],  # list[str]
        immunities=["Crush"],  # list[str]
        traits=["Multi-Attack"],  # list[str]
        base_attack=5,  # int
        base_health=8,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Spawn"],  # list[str](optional)
    )

    return this_minion
