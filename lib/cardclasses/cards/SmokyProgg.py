from ..bases.minion import *


class SmokyProgg(Minion):
    pass


def load_me():
    this_minion = SmokyProgg(
        set="1",  # str
        number=37,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Smoky Progg",  # str
        image="37_Smoky_Progg.png",  # str
        cardclass=2,  # int
        base_energy=7,  # int
        base_time=9,  # int
        elements=["Gloom"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect"],  # list[str]
        base_attack=2,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Gloom Wave", "Ethereal"],  # list[str](optional)
    )

    return this_minion
