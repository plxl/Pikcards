from ..bases.minion import *


class CrimsonCandypopBud(Minion):
    pass


def load_me():
    this_minion = CrimsonCandypopBud(
        set="1",  # str
        number=4,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Crimson Candypop Bud",  # str
        image="04_Crimson_Candypop_Bud.png",  # str
        cardclass=1,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Candypop"],  # list[str](optional)
    )

    return this_minion
