from card import *


"""
    TO DO:
    - General works for Items, like what has to happen when one is played/adding abilities to the holder if the case
"""



# Base minion data, stats and actions
class Item(Card):
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

        self.weaknessDescription = weaknessDescriptions  # Descriptions of all weaknesses
        self.base_wd = weaknessDescriptions  # Weaknesses which the base card has
        self.abilityDescription = abilityDescriptions  # Descriptions of all abilities
        self.base_ad = abilityDescriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
        # Attributes unique to Items
    

        # Modifiers for the Item itself
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


        # Modifiers that are added to the holder
        self.bePlayedMinionModifiers: list[BePlayedModifier] = []
        self.enterLaneMinionModifiers: list[EnterLaneModifier] = []
        self.roundStartMinionModifiers: list[RoundStartModifier] = []
        self.turnStartMinionModifiers: list[TurnStartModifier] = []
        self.nightStartMinionModifiers: list[NightStartModifier] = []
        self.roundEndMinionModifiers: list[NightEndModifier] = []
        self.returnedMinionModifiers: list[ReturnedModifier] = []
        self.discardedMinionModifiers: list[DiscardedModifier] = []
        self.otherCardPlayedMinionModifiers: list[OtherCardPlayedModifier] = []
        self.otherCardLeavesMinionModifiers: list[OtherCardLeavesModifier] = []

        self.dealDamageMinionModifiers: list[DealDamageModifier] = []
        self.takeDamageMinionModifiers: list[TakeDamageModifier] = []
        self.beKilledMinionModifiers: list[BeKilledModifier] = []



    def getDescription(self):
        description: str = "ITEM\n"
        if len(self.weaknessDescription) > 0:
            description += "WEAKNESSES:\n"
            description += "\n".join(self.weaknessDescription)
            description += "\n"
        
        if len(self.abilityDescription) > 0:
            description += "ABILITIES:\n"
            description += "\n".join(self.abilityDescription)
        return description

    def resetStats(self):
        self.lane_index = -1
        self.energy = self.base_energy
        self.time = self.base_time
        self.weaknessDescription = self.base_wd
        self.abilityDescription = self.base_ad
