from ..bases.minion import *


class BlueOnion(Minion):
    pass


def load_me():
    this_minion = BlueOnion(
        set="1",  # str
        number=9,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Blue Onion",  # str
        image="09_Blue_Onion.png",  # str
        cardclass=3,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=4,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Gloom"],  # list[str](optional)
        base_abilities=["Onion"],  # list[str](optional)
    )

    return this_minion
