from ..bases.item import *


class DreamMaterial(Item):
    pass


def load_me():
    this_item = DreamMaterial(
        set="2",  # str
        number=86,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Dream Material",  # str
        image="086_Dream_Material.png",  # str
        card_class=4,  # int
        base_energy=2,  # int
        base_time=10,  # int
        elements=[],  # list[str]
        immunities=["Electricity"],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Rub Off"],  # list[str](optional)
    )

    return this_item
