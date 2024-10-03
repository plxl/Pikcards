from ..bases.minion import *


class Louie(Minion):
    pass


def load_me():
    this_minion = Louie(
        set="2",  # str
        number=1,  # int
        fifth=False,  # bool
        rarity=2,  # int
        name="Louie",  # str
        image="001_Louie.png",  # str
        card_class=1,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        base_attack=1,  # int
        base_health=5,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Gourmand", "Conjure"],  # list[str](optional)
    )

    return this_minion
