from ..bases.minion import *


class Wollyhop(Minion):
    pass


def load_me():
    this_minion = Wollyhop(
        set="1",  # str
        number=24,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Wollyhop",  # str
        image="24_Wollyhop.png",  # str
        card_class=1,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=["Crush", "Water"],  # list[str]
        immunities=[],  # list[str]
        traits=["First Strike"],  # list[str]
        base_attack=4,  # int
        base_health=1,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
