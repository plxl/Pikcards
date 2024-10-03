from ..bases.minion import *


class BulborbLarva(Minion):
    pass


def load_me():
    this_minion = BulborbLarva(
        set="2",  # str
        number=15,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Bulborb Larva",  # str
        image="015_Bulborb_Larva.png",  # str
        cardclass=1,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["First Strike", "Passive"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=["Up High", "First Strike", "Crush", "Poison"],  # list[str](optional)
        base_abilities=["Transform"],  # list[str](optional)
    )

    return this_minion
