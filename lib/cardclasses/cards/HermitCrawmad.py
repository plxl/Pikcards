from ..bases.minion import *


class HermitCrawmad(Minion):
    pass


def load_me():
    this_minion = HermitCrawmad(
        set="2",  # str
        number=35,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Hermit Crawmad",  # str
        image="035_Hermit_Crawmad.png",  # str
        cardclass=4,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=["Piercing"],  # list[str]
        immunities=["Water", "Piercing", "First Strike"],  # list[str]
        traits=["Burrowing"],  # list[str]
        base_attack=2,  # int
        base_health=4,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Den Defense"],  # list[str](optional)
    )

    return this_minion
