from ..bases.minion import *


class LapisLazuliCandypopBud(Minion):
    pass


def load_me():
    this_minion = LapisLazuliCandypopBud(
        set="1",  # str
        number=10,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Lapis Lazuli Candypop Bud",  # str
        image="10_Lapis_Lazuli_Candypop_Bud.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Passive"],  # list[str]
        base_attack=0,  # int
        base_health=2,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Candypop"],  # list[str](optional)
    )

    return this_minion
