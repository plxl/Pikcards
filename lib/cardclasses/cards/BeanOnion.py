from ..bases.minion import *


class BeanOnion(Minion):
    pass


def load_me():
    this_minion = BeanOnion(
        set="C",  # str
        number=3,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Bean Onion",  # str
        image="03_Bean_Onion.png",  # str
        cardclass=5,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=4,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Gloom"],  # list[str](optional)
        base_abilities=["Onion"],  # list[str](optional)
    )

    return this_minion
