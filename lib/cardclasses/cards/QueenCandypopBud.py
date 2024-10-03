from ..bases.minion import *


class QueenCandypopBud(Minion):
    pass


def load_me():
    this_minion = QueenCandypopBud(
        set="2",  # str
        number=7,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Queen Candypop Bud",  # str
        image="007_Queen_Candypop_Bud.png",  # str
        cardclass=4,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=3,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Conjure", "Candypop"],  # list[str](optional)
    )

    return this_minion
