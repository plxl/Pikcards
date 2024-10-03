from ..bases.minion import *


class CreepingChrysanthemumUnderground(Minion):
    pass


def load_me():
    this_minion = CreepingChrysanthemumUnderground(
        set="2",  # str
        number=26,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Creeping Chrysanthemum (Underground)",  # str
        image="026_Creeping_Chrysanthemum_(Underground).png",  # str
        cardclass=2,  # int
        base_energy=4,  # int
        base_time=8,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Digging"],  # list[str]
        base_attack=0,  # int
        base_health=6,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Fire", "Poison"],  # list[str](optional)
        base_abilities=["Ambush", "Root Share"],  # list[str](optional)
    )

    return this_minion
