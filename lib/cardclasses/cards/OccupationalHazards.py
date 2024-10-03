from ..bases.area import *


class OccupationalHazards(Area):
    pass


def load_me():
    this_area = OccupationalHazards(
        set="C",  # str
        number=19,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="Occupational Hazards",  # str
        image="19_Occupational_Hazards.png",  # str
        card_class=5,  # int
        base_energy=4,  # int
        base_time=5,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Occupational Hazards"],  # list[str](optional)
    )

    return this_area
