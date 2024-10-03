from ..bases.minion import *


class BurrowingSnagret(Minion):
    pass


def load_me():
    this_minion = BurrowingSnagret(
        set="1",  # str
        number=28,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Burrowing Snagret",  # str
        image="28_Burrowing_Snagret.png",  # str
        cardclass=2,  # int
        base_energy=4,  # int
        base_time=6,  # int
        elements=["Piercing"],  # list[str]
        immunities=[],  # list[str]
        traits=["Burrowing", "Up High", "Defense"],  # list[str]
        base_attack=3,  # int
        base_health=3,  # int
        base_defense=1,  # int
        maxcarry=1,  # int
        base_weaknesses=["First Strike"],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
