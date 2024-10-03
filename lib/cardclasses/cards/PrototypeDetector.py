from ..bases.item import *


class PrototypeDetector(Item):
    pass


def load_me():
    this_item = PrototypeDetector(
        set="2",  # str
        number=80,  # int
        fifth=True,  # bool
        rarity=1,  # int
        name="Prototype Detector",  # str
        image="080_Prototype_Detector.png",  # str
        card_class=2,  # int
        base_energy=1,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Debt Treasure"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Shuffle", "Draw"],  # list[str](optional)
    )

    return this_item
