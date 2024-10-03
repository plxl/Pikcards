from ..bases.item import *


class EternalFuelDynamo(Item):
    pass


def load_me():
    this_item = EternalFuelDynamo(
        set="1",  # str
        number=41,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Eternal Fuel Dynamo",  # str
        image="41_Eternal_Fuel_Dynamo.png",  # str
        cardclass=1,  # int
        base_energy=2,  # int
        base_time=10,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=["Dolphin Part"],  # list[str]
        base_weaknesses=["Indirect"],  # list[str](optional)
        base_abilities=["Pain Power"],  # list[str](optional)
    )

    return this_item
