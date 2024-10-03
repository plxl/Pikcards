from ..bases.minion import *


class FieryBulblax(Minion):
    pass


def load_me():
    this_minion = FieryBulblax(
        set="2",  # str
        number=14,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Fiery Bulblax",  # str
        image="014_Fiery_Bulblax.png",  # str
        cardclass=1,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=["Fire"],  # list[str]
        immunities=["Ice"],  # list[str]
        traits=[],  # list[str]
        base_attack=4,  # int
        base_health=4,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Water"],  # list[str](optional)
        base_abilities=["Panic"],  # list[str](optional)
    )

    return this_minion
