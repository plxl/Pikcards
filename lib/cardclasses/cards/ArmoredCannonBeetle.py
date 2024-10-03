from ..bases.minion import *


class ArmoredCannonBeetle(Minion):
    pass


def load_me():
    this_minion = ArmoredCannonBeetle(
        set="1",  # str
        number=29,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Armored Cannon Beetle",  # str
        image="29_Armored_Cannon_Beetle.png",  # str
        cardclass=3,  # int
        base_energy=5,  # int
        base_time=5,  # int
        elements=["Crush"],  # list[str]
        immunities=["Piercing", "Explosive"],  # list[str]
        traits=["Defense", "Indirect", "Swarm"],  # list[str]
        base_attack=3,  # int
        base_health=6,  # int
        base_defense=1,  # int
        maxcarry=1,  # int
        base_weaknesses=["First Strike", "Up High"],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
