from ..bases.area import *


class PNF404(Area):
    pass


def load_me():
    this_area = PNF404(
        set="C",  # str
        number=34,  # int
        fifth=False,  # bool
        rarity=1,  # int
        name="PNF-404",  # str
        image="34_PNF-404.png",  # str
        card_class=5,  # int
        base_energy=3,  # int
        base_time=4,  # int
        elements=[],  # list[str]
        immunities=[],  # list[str]
        traits=[],  # list[str]
        description="Description",  # str
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["PNF-404"],  # list[str](optional)
    )

    return this_area
