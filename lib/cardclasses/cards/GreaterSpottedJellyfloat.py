from ..bases.minion import *


class GreaterSpottedJellyfloat(Minion):
    pass


def load_me():
    this_minion = GreaterSpottedJellyfloat(
        set="2",  # str
        number=39,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Greater Spotted Jellyfloat",  # str
        image="039_Greater_Spotted_Jellyfloat.png",  # str
        cardclass=3,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Up High", "Indirect", "Passive"],  # list[str]
        base_attack=1,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Ice"],  # list[str](optional)
        base_abilities=["Power Suction", "Bubble"],  # list[str](optional)
    )

    return this_minion
