from ..bases.item import *


class InterstellarRadio(Item):
    pass


def load_me():
    this_item = InterstellarRadio(
        set="1",  # str
        number=67,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Interstellar Radio",  # str
        image="67_Interstellar_Radio.png",  # str
        cardclass=2,  # int
        base_energy=4,  # int
        base_time=3,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return Message"],  # list[str](optional)
    )

    return this_item
