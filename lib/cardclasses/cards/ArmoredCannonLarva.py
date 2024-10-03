from ..bases.minion import *


class ArmoredCannonLarva(Minion):
    pass


def load_me():
    this_minion = ArmoredCannonLarva(
        set="2",  # str
        number=20,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Armored Cannon Larva",  # str
        image="020_Armored_Cannon_Larva.png",  # str
        cardclass=2,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=["Crush"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect", "Burrowing"],  # list[str]
        base_attack=3,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Up High"],  # list[str](optional)
        base_abilities=["Transform"],  # list[str](optional)
    )

    return this_minion
