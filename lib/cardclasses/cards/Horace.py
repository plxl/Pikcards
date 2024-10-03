from ..bases.minion import *


class Horace(Minion):
    pass


def load_me():
    this_minion = Horace(
        set="C",  # str
        number=109,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Horace",  # str
        image="109_Horace.png",  # str
        card_class=5,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=["Gloom", "Poison", "Explosive"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect", "Up High", "Multi-Attack"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_minion
