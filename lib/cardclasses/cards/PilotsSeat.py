from ..bases.item import *


class PilotsSeat(Item):
    pass


def load_me():
    this_item = PilotsSeat(
        set="1",  # str
        number=58,  # int
        fifth=True,  # bool
        rarity=0,  # int
        name="Pilot's Seat",  # str
        image="58_Pilot's_Seat.png",  # str
        card_class=1,  # int
        base_energy=2,  # int
        base_time=2,  # int
        elements=[],  # list[str]
        immunities=["Crush"],  # list[str]
        traits=["Up High", "Dolphin Part"],  # list[str]
        base_weaknesses=[],  # list[str](optional)
        base_abilities=["Return"],  # list[str](optional)
    )

    return this_item
