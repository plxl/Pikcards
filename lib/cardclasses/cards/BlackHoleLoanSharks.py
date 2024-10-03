from ..bases.minion import *


class BlackHoleLoanSharks(Minion):
    pass


def load_me():
    this_minion = BlackHoleLoanSharks(
        set="C",  # str
        number=25,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Black Hole Loan Sharks",  # str
        image="25_Black_Hole_Loan_Sharks.png",  # str
        cardclass=5,  # int
        base_energy=6,  # int
        base_time=3,  # int
        elements=["Gloom", "Ice"],  # list[str]
        immunities=[],  # list[str]
        traits=["Burrowing", "Passive"],  # list[str]
        base_attack=2,  # int
        base_health=3,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Killer Debt"],  # list[str](optional)
    )

    return this_minion
