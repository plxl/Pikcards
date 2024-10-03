from ..bases.item import *


class ChronosReactor(Item):
    pass


def load_me():
    this_item = ChronosReactor(
        set="1",  # str
        number=59,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Chronos Reactor",  # str
        image="59_Chronos_Reactor.png",  # str
        cardclass=1,  # int
        base_energy=4,  # int
        base_time=6,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Convert Time"],  # list[str](optional)
    )

    return this_item
