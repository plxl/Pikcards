from ..bases.minion import *


class PuffyBlowhog(Minion):
    pass


def load_me():
    this_minion = PuffyBlowhog(
        set="1",  # str
        number=33,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Puffy Blowhog",  # str
        image="33_Puffy_Blowhog.png",  # str
        card_class=2,  # int
        base_energy=2,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Up High", "Indirect"],  # list[str]
        base_attack=0,  # int
        base_health=3,  # int
        base_defense=0,  # int
        max_carry=1,  # int
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_minion
