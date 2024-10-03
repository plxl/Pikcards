from ..bases.item import *


class GluonDrive(Item):
    pass


def load_me():
    this_item = GluonDrive(
        set="1",  # str
        number=56,  # int
        fifth=False,  # bool
        rarity=0,  # int
        name="Gluon Drive",  # str
        image="56_Gluon_Drive.png",  # str
        cardclass=3,  # int
        base_energy=4,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Gluon Conversion"],  # list[str](optional)
    )

    return this_item
