from ..bases.minion import *


class Honeywisp(Minion):
    pass


def load_me():
    this_minion = Honeywisp(
        set="1",  # str
        number=27,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Honeywisp",  # str
        image="27_Honeywisp.png",  # str
        cardclass=2,  # int
        base_energy=1,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Up High", "Passive"],  # list[str]
        base_attack=0,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Honey Provision", "Auto-Return"],  # list[str](optional)
    )

    return this_minion
