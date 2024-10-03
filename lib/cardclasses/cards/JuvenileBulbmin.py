from ..bases.minion import *


class JuvenileBulbmin(Minion):
    pass


def load_me():
    this_minion = JuvenileBulbmin(
        set="2",  # str
        number=17,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Juvenile Bulbmin",  # str
        image="017_Juvenile_Bulbmin.png",  # str
        cardclass=3,  # int
        base_energy=1,  # int
        base_time=1,  # int
        elements=[],  # list[str]
        immunities=["Fire", "Water", "Electricity", "Poison", "Ice"],  # list[str]
        traits=["Pikmin"],  # list[str]
        base_attack=1,  # int
        base_health=1,  # int
        base_defense=0,  # int
        maxcarry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=[],  # list[str](optional)
    )

    return this_minion
