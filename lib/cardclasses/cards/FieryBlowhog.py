from ..bases.minion import *


class FieryBlowhog(Minion):
    pass


def load_me():
    this_minion = FieryBlowhog(
        set="1",  # str
        number=20,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Fiery Blowhog",  # str
        image="20_Fiery_Blowhog.png",  # str
        cardclass=3,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=["Fire"],  # list[str]
        immunities=["Fire"],  # list[str]
        traits=["Indirect", "Explorer"],  # list[str]
        base_attack=1,  # int
        base_health=6,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Draw"],  # list[str](optional)
    )

    return this_minion
