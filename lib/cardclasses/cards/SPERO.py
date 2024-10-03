from ..bases.minion import *


class SPERO(Minion):
    pass


def load_me():
    this_minion = SPERO(
        set="C",  # str
        number=10,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="SPERO",  # str
        image="10_SPERO.png",  # str
        cardclass=5,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=["Poison", "Mushroom", "Piercing"],  # list[str]
        traits=["Up-High", "Indirect"],  # list[str]
        base_attack=0,  # int
        base_health=4,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Field Scan"],  # list[str](optional)
    )

    return this_minion
