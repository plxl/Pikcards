from .card import *

# Base exploration data, stats and actions
class Exploration(Card):
    def __init__(self,
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

                 weakness_descriptions: list[str] = [],
                 ability_descriptions: list[str] = []
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

        self.weakness_description = weakness_descriptions  # Descriptions of all weaknesses
        self.base_wd = weakness_descriptions  # Weaknesses which the base card has
        self.ability_description = ability_descriptions  # Descriptions of all abilities
        self.base_ad = ability_descriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
        # Attributes unique to Areas
        
        # Modifiers
        self.bePlayedModifiers: list[BePlayedModifier] = []

    

    # Provides description that shows what the abilities of the class are
    def get_description(self):
        full_description: str = f"Exploration {self.name}\n"
        full_description += self.description
        return full_description
    
    # Reset stats for when a card is Returned or Discarded
    def reset_stats(self):
        self.lane_index = -1
        self.energy = self.base_energy
        self.time = self.base_time
        self.description = self.base_desc
