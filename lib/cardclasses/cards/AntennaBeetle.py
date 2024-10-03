from ..bases.minion import *


class AntennaBeetle(Minion):
    pass


def load_me():
    this_minion = AntennaBeetle(
        set="2",  # str
        number=36,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Antenna Beetle",  # str
        image="036_Antenna_Beetle.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Disruption"],  # list[str](optional)
    )

    return this_minion
