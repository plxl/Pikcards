from ..bases.minion import *


class ElectricGate(Minion):
    pass


def load_me():
    this_minion = ElectricGate(
        set="2",  # str
        number=97,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Electric Gate",  # str
        image="097_Electric_Gate.png",  # str
        cardclass=4,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=["Electricity"],  # list[str]
        immunities=[],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Shock"],  # list[str](optional)
    )

    return this_minion
