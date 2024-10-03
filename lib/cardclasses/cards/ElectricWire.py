from ..bases.minion import *


class ElectricWire(Minion):
    pass


def load_me():
    this_minion = ElectricWire(
        set="2",  # str
        number=98,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Electric Wire",  # str
        image="098_Electric_Wire.png",  # str
        cardclass=4,  # int
        base_energy=3,  # int
        base_time=2,  # int
        elements=["Electricity"],  # list[str]
        immunities=[],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=3,  # int
        base_health=2,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Shock", "Static"],  # list[str](optional)
    )

    return this_minion
