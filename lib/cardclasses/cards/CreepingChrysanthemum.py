from ..bases.minion import *


class CreepingChrysanthemum(Minion):
    pass


def load_me():
    this_minion = CreepingChrysanthemum(
        set="2",  # str
        number=26,  # int
        fifth=False,  # bool
        rarity=-1,  # int
        name="Creeping Chrysanthemum",  # str
        image="026_Creeping_Chrysanthemum_(Aboveground).png",  # str
        cardclass=0,  # int
        base_energy=4,  # int
        base_time=8,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Burrowing"],  # list[str]
        base_attack=5,  # int
        base_health=6,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Fire", "Poison"],  # list[str](optional)
        base_abilities=["Re-Burrow", "Failed Attack"],  # list[str](optional)
    )

    return this_minion
