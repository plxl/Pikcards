from ..bases.minion import *


class HocotateShip(Minion):
    pass


def load_me():
    this_minion = HocotateShip(
        set="2",  # str
        number=54,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Hocotate Ship",  # str
        image="054_Hocotate_Ship.png",  # str
        cardclass=4,  # int
        base_energy=5,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=["Poison", "Mushroom", "Piercing"],  # list[str]
        traits=["Indirect"],  # list[str]
        base_attack=0,  # int
        base_health=5,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Mega Income", "Sales Pitch", "Big Heal"],  # list[str](optional)
    )

    return this_minion
