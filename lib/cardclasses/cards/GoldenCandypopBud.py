from ..bases.minion import *


class GoldenCandypopBud(Minion):
    pass


def load_me():
    this_minion = GoldenCandypopBud(
        set="1",  # str
        number=7,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Golden Candypop Bud",  # str
        image="07_Golden_Candypop_Bud.png",  # str
        card_class=2,  # int
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
