from ..bases.minion import *


class PikpikBean(Minion):
    pass


def load_me():
    this_minion = PikpikBean(
        set="C",  # str
        number=2,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Pikpik Bean?",  # str
        image="02_Pikpik_Bean.png",  # str
        cardclass=5,  # int
        base_energy=0,  # int
        base_time=0,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=0,  # int
        base_health=1,  # int
        defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Heal"],  # list[str](optional)
    )

    return this_minion
