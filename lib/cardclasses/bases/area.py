from .card import *

# Base area data, stats and actions
class Area(Card):
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

                 weaknessDescriptions: list[str] = [],
                 abilityDescriptions: list[str] = []
                 
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
        self.baseDesc = description

        self.weaknessDescription = weaknessDescriptions  # Descriptions of all weaknesses
        self.base_wd = weaknessDescriptions  # Weaknesses which the base card has
        self.abilityDescription = abilityDescriptions  # Descriptions of all abilities
        self.base_ad = abilityDescriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
        # Attributes unique to Areas
        
        # Modifiers
        self.bePlayedModifiers: list[BePlayedModifier] = []
        self.enterLaneModifiers: list[EnterLaneModifier] = []
        self.roundStartModifiers: list[RoundStartModifier] = []
        self.turnStartModifiers: list[TurnStartModifier] = []
        self.nightStartModifiers: list[NightStartModifier] = []
        self.roundEndModifiers: list[NightEndModifier] = []
        self.returnedModifiers: list[ReturnedModifier] = []
        self.discardedModifiers: list[DiscardedModifier] = []
        self.otherCardPlayedModifiers: list[OtherCardPlayedModifier] = []
        self.otherCardLeavesModifiers: list[OtherCardLeavesModifier] = []

        self.areaEnteredModifiers: list[OtherCardPlayedModifier] = []

    

    # Provides description that shows what the abilities of the class are
    def getDescription(self):
        fullDescription: str = f"AREA {self.name}\n"
        fullDescription += self.description
        return fullDescription
    
    # Reset stats for when a card is Returned or Discarded
    def resetStats(self):
        self.lane_index = -1
        self.energy = self.base_energy
        self.time = self.base_time
        self.description = self.baseDesc
