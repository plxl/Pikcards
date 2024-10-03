from ..bases.minion import *


class WateryBlowhog(Minion):
    pass


def load_me():
    this_minion = WateryBlowhog(
        set="2",  # str
        number=18,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Watery Blowhog",  # str
        image="018_Watery_Blowhog.png",  # str
        card_class=2,  # int
        base_energy=2,  # int
        base_time=5,  # int
        elements=["Water"],  # list[str]
        immunities=["Water"],  # list[str]
        traits=["Indirect", "Explorer"],  # list[str]
        base_attack=2,  # int
        base_health=4,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Draw"],  # list[str](optional)
    )

    return this_minion
