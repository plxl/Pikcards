from ..bases.minion import *


class BlastWall(Minion):
    pass


def load_me():
    this_minion = BlastWall(
        set="1",  # str
        number=73,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Blast Wall",  # str
        image="73_Blast_Wall.png",  # str
        cardclass=3,  # int
        base_energy=3,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Defense", "Wall"],  # list[str]
        base_attack=0,  # int
        base_health=8,  # int
        defense=1,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
