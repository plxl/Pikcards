from ..bases.minion import *


class SwoopingSnitchbug(Minion):
    pass


def load_me():
    this_minion = SwoopingSnitchbug(
        set="1",  # str
        number=21,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Swooping Snitchbug",  # str
        image="21_Swooping_Snitchbug.png",  # str
        cardclass=2,  # int
        base_energy=2,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["First Strike", "Up High", "Swarm"],  # list[str]
        base_attack=2,  # int
        base_health=2,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_minion
