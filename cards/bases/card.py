from abc import ABC, abstractmethod
from enum import Enum
from modifiers import *


# Classes that a card can have
class CardClass:
    NONE = 0
    FIGHTING = 1
    TRAPPERS = 2
    SURVIVAL = 3
    BOOSTER = 4
    HANDY = 5

# Elements a card can have
class CardElement:
    Fire = 0
    Water = 1
    Electricity = 2
    Crush = 3
    Explosive = 4
    Poison = 5
    Ice = 6
    Gloom = 7
    Mushroom = 8

# Traits a card can have, card families also included in 100's
class CardTrait:
    Pikmin = 0
    Passive = 1
    Wall = 2
    Swarm = 3
    DolphinPart = 4
    DebtTreasure = 5
    FirstStrike = 6
    Burrowing = 7
    Digging = 8
    UpHigh = 9
    Explorer = 10
    MultiAttack = 11
    Indirect = 12

# Rarity which cards can have
Rarity = Enum(
    value="Rarity",
    names=[
        ("Plain",     0),
        ("Common",    1),
        ("Rare",      2),
        ("Very Rare", 3)])




# Base card abilities and stats 
class Card(ABC):
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
                 traits
                 ):
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

        self.weaknessDescription: list[str] = []
        self.abilityDescription: list[str] = []

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.

    

    # Provides description that shows what the abilities of the class are
    @abstractmethod
    def getDescription():
        raise NotImplemented("Subclasses must implement this method")
    
    # Reset stats for when a card is Returned or Discarded
    @abstractmethod
    def resetStats(self):
        raise NotImplemented("Subclasses must implement this method")
    


    # Basic function for entering a lane
    def onBeingPlayed(self, lane_index: int):

        ### Perform anything that should be done upon playing ###

        # ALWAYS go to entering a lane after
        self.onEnterLane(lane_index)


    # Basic function for entering a lane
    # This also changes the card's lane value
    def onEnterLane(self, lane_index: int):
        self.lane_index = lane_index

        ### Perform anything that should be done upon entering a lane ###
