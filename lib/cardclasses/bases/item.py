from .card import *


"""
    TO DO:
    - General works for Items, like what has to happen when one is played/adding abilities to the holder if the case
"""


# Base minion data, stats and actions
class Item(Card):
    def __init__(
        self,
        set,
        number,
        fifth,
        rarity,
        name,
        image,
        cardclass,
        base_energy,
        base_time,
        elements,
        immunities,
        traits,
        base_weaknesses: list[str] = [],
        base_abilities: list[str] = [],
    ):
        # Attributes for Card class
        self.set = set
        self.number = number
        self.fifth = fifth
        self.rarity = rarity
        self.name = name
        self.image = image
        self.cardclass = cardclass

        self.base_energy = base_energy  # Standard energy cost of the card
        self.energy = base_energy  # current energy cost of the card
        self.base_time = base_time  # Standard time cost of the card
        self.time = base_time  # Current time cost of the card

        self.elements = elements
        self.immunities = immunities
        self.traits = traits

        self.base_weaknesses = base_weaknesses  # Weaknesses which the base card has
        self.weaknesses = base_weaknesses  # Descriptions of all weaknesses
        self.base_abilities = base_abilities  # Abilities which the base card has
        self.abilities = base_abilities  # Descriptions of all abilities

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.

        # Attributes unique to Items

        # Modifiers for the Item itself
        self.be_played_modifiers: list[BePlayedModifier] = []
        self.enter_lane_modifiers: list[EnterLaneModifier] = []
        self.round_start_modifiers: list[RoundStartModifier] = []
        self.turn_start_modifiers: list[TurnStartModifier] = []
        self.night_start_modifiers: list[NightStartModifier] = []
        self.night_end_modifiers: list[NightEndModifier] = []
        self.round_end_modifiers: list[RoundEndModifier] = []
        self.returned_modifiers: list[ReturnedModifier] = []
        self.discarded_modifiers: list[DiscardedModifier] = []
        self.other_card_played_modifiers: list[OtherCardPlayedModifier] = []
        self.other_card_leaves_modifiers: list[OtherCardLeavesModifier] = []

        # Modifiers that are added to the holder
        self.minion_be_played_modifiers: list[BePlayedModifier] = []
        self.minion_enter_lane_modifiers: list[EnterLaneModifier] = []
        self.minion_round_start_modifiers: list[RoundStartModifier] = []
        self.minion_turn_start_modifiers: list[TurnStartModifier] = []
        self.minion_night_start_modifiers: list[NightStartModifier] = []
        self.minion_night_end_modifiers: list[NightEndModifier] = []
        self.minion_round_end_modifiers: list[RoundEndModifier] = []
        self.minion_returned_modifiers: list[ReturnedModifier] = []
        self.minion_discarded_modifiers: list[DiscardedModifier] = []
        self.minion_other_card_played_modifiers: list[OtherCardPlayedModifier] = []
        self.minion_other_card_leaves_modifiers: list[OtherCardLeavesModifier] = []

        self.minion_deal_damage_modifiers: list[DealDamageModifier] = []
        self.minion_take_damage_modifiers: list[TakeDamageModifier] = []
        self.minion_be_killed_modifiers: list[BeKilledModifier] = []

    def get_description(self):
        description: str = f"Item {self.name}\n"
        if len(self.weaknesses) > 0:
            description += "WEAKNESSES:\n"
            description += "\n".join(self.weaknesses)
            description += "\n"

        if len(self.abilities) > 0:
            description += "ABILITIES:\n"
            description += "\n".join(self.abilities)
        return description

    def reset_stats(self):
        self.lane_index = -1
        self.energy = self.base_energy
        self.time = self.base_time
        self.weaknesses = self.base_weaknesses
        self.abilities = self.base_abilities
