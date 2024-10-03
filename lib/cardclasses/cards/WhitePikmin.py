from ..bases.minion import *


class WhitePikmin(Minion):
    pass


def load_me():
    this_minion = WhitePikmin(
        set="2",  # str
        number=5,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="White Pikmin",  # str
        image="005_White_Pikmin.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=["Poison"],  # list[str]
        immunities=["Poison"],  # list[str]
        traits=["Digging", "Pikmin"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Poison Body", "Speedy Feet"],  # list[str](optional)
    )

    return this_minion
