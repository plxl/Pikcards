from ..bases.minion import *


class LesserSpottedJellyfloat(Minion):
    pass


def load_me():
    this_minion = LesserSpottedJellyfloat(
        set="2",  # str
        number=38,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Lesser Spotted Jellyfloat",  # str
        image="038_Lesser_Spotted_Jellyfloat.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Up High", "Indirect", "Passive"],  # list[str]
        base_attack=0,  # int
        base_health=4,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Ice"],  # list[str](optional)
        base_abilities=["Power Suction"],  # list[str](optional)
    )

    return this_minion
