from ..bases.minion import *


class PeanutButterBloyster(Minion):
    pass


def load_me():
    this_minion = PeanutButterBloyster(
        set="C",  # str
        number=14,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Peanut Butter Bloyster",  # str
        image="14_Peanut_Butter_Bloyster.png",  # str
        cardclass=5,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=["Water", "Gloom", "Poison"],  # list[str]
        immunities=["Water", "Crush"],  # list[str]
        traits=["Explorer"],  # list[str]
        base_attack=2,  # int
        base_health=2,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Ink Spread"],  # list[str](optional)
    )

    return this_minion
