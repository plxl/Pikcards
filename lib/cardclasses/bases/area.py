from .card import *

# Base area data, stats and actions
class Area(Card):
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
        description: str,
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

        self.description = description
        self.base_desc = description

        self.base_weaknesses = base_weaknesses  # Weaknesses which the base card has
        self.weaknesses = base_weaknesses  # Descriptions of all weaknesses
        self.base_abilities = base_abilities  # Abilities which the base card has
        self.abilities = base_abilities  # Descriptions of all abilities

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
        # Attributes unique to Areas
        
        # Modifiers
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

        self.this_area_entered_modifiers: list[OtherCardPlayedModifier] = []

    

    # Provides description that shows what the abilities of the class are
    def get_description(self):
        full_description: str = f"Area {self.name}\n"
        full_description += self.description
        return full_description
    
    # Reset stats for when a card is Returned or Discarded
    def reset_stats(self):
        self.lane_index = -1
        self.energy = self.base_energy
        self.time = self.base_time
        self.description = self.base_desc
