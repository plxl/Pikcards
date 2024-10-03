from ..bases.minion import *


class Waterwraith(Minion):
    pass


def load_me():
    this_minion = Waterwraith(
        set="2",  # str
        number=52,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Waterwraith",  # str
        image="052_Waterwraith.png",  # str
        cardclass=3,  # int
        base_energy=2,  # int
        base_time=5,  # int
        elements=["Crush"],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=1,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Chase", "Roll Over"],  # list[str](optional)
    )

    return this_minion
