from ..bases.minion import *


class DecoratedCannonBeetle(Minion):
    pass


def load_me():
    this_minion = DecoratedCannonBeetle(
        set="2",  # str
        number=21,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Decorated Cannon Beetle",  # str
        image="021_Decorated_Cannon_Beetle.png",  # str
        cardclass=1,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=["Crush"],  # list[str]
        immunities=[],  # list[str]
        traits=["Indirect", "Digging"],  # list[str]
        base_attack=4,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Up High"],  # list[str](optional)
        base_abilities=["Magnet Attack"],  # list[str](optional)
    )

    return this_minion
