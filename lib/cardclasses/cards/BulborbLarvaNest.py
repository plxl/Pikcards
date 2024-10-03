from ..bases.minion import *


class BulborbLarvaNest(Minion):
    pass


def load_me():
    this_minion = BulborbLarvaNest(
        set="C",  # str
        number=11,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Bulborb Larva Nest",  # str
        image="11_Bulborb_Larva_Nest.png",  # str
        card_class=5,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Burrowing", "Passive"],  # list[str]
        base_attack=0,  # int
        base_health=4,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Digging", "Burrowing"],  # list[str](optional)
        base_abilities=["Conjure"],  # list[str](optional)
    )

    return this_minion
