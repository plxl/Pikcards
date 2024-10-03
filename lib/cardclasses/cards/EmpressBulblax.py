from ..bases.minion import *


class EmpressBulblax(Minion):
    pass


def load_me():
    this_minion = EmpressBulblax(
        set="2",  # str
        number=44,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Empress Bulblax",  # str
        image="044_Empress_Bulblax.png",  # str
        cardclass=4,  # int
        base_energy=6,  # int
        base_time=5,  # int
        elements=["Crush"],  # list[str]
        immunities=["Piercing"],  # list[str]
        traits=[],  # list[str]
        base_attack=2,  # int
        base_health=8,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Spawn", "Field Roll"],  # list[str](optional)
    )

    return this_minion
