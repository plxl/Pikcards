from ..bases.minion import *


class IridescentGlintBeetle(Minion):
    pass


def load_me():
    this_minion = IridescentGlintBeetle(
        set="2",  # str
        number=23,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Iridescent Glint Beetle",  # str
        image="023_Iridescent_Glint_Beetle.png",  # str
        cardclass=5,  # int
        base_energy=3,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=["Piercing", "Gloom"],  # list[str]
        traits=["Wall"],  # list[str]
        base_attack=0,  # int
        base_health=5,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=["Crush"],  # list[str](optional)
        base_abilities=["Scuttle", "Glitter Hoard"],  # list[str](optional)
    )

    return this_minion
