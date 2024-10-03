from ..bases.minion import *


class TitanDweevil(Minion):
    pass


def load_me():
    this_minion = TitanDweevil(
        set="2",  # str
        number=53,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Titan Dweevil",  # str
        image="053_Titan_Dweevil.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=["Fire", "Water", "Electricity", "Poison"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect"],  # list[str]
        base_attack=0,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=3,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Carry", "Carry Force", "Weapon Selection"],  # list[str](optional)
    )

    return this_minion
