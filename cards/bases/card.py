from abc import ABC, abstractmethod
from enum import Enum
from modifiers import *



"""
    TO DO:
    THINGS ABILITIES SHOULD BE ABLE TO TO FROM THE OUTSIDE:
    - For onReturned, Player or the Game needs a callable function that makes them remove a card from the field, then put it in the given player's hand
    - For some abilities and modifiers, somewhere needs a caalable function for:
        - Getting the entire field to read what's in it
        - Getting the entire Lane to read what's in it
        - Getting a specific player's hand
    - Observer type methods to the game, which cards can subscribe and unsubscribe to.
        - For other cards entering the field
        - For other cards leaving the field
    - More specific functions a card should be able to call:
        - Make specific player draw a card, potentially a specific one
        - Make specific player conjure a specific card

    OTHER:
    - Function in card itself to call the Draw or Conjure functions. This one should check if it has a status. If it does, fail to complete the action
"""






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

    GrubDog = 100
    Amphituber = 101
    Snavian = 102
    Mockiwi = 103

# Rarity which cards can have
Rarity = Enum(
    value="Rarity",
    names=[
        ("Plain",     0),
        ("Common",    1),
        ("Rare",      2),
        ("Very Rare", 3)])



# Base card data, stats and actions
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
                 traits,

                 weaknessDescriptions: list[str] = [],
                 abilityDescriptions: list[str] = []
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

        self.weaknessDescription = weaknessDescriptions  # Descriptions of all weaknesses
        self.base_wd = weaknessDescriptions  # Weaknesses which the base card has
        self.abilityDescription = abilityDescriptions  # Descriptions of all abilities
        self.base_ad = abilityDescriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
        # Modifiers
        self.bePlayedModifiers: list[BePlayedModifier] = []
        self.enterLaneModifiers: list[EnterLaneModifier] = []
        self.roundStartModifiers: list[RoundStartModifier] = []
        self.turnStartModifiers: list[TurnStartModifier] = []
        self.nightStartModifiers: list[NightStartModifier] = []
        self.nightEndModifiers: list[NightEndModifier] = []
        self.roundEndModifiers: list[RoundEndModifier] = []
        self.returnedModifiers: list[ReturnedModifier] = []
        self.discardedModifiers: list[DiscardedModifier] = []
        self.otherCardPlayedModifiers: list[OtherCardPlayedModifier] = []
        self.otherCardLeavesModifiers: list[OtherCardLeavesModifier] = []

    

    # Provides description that shows what the abilities of the class are
    @abstractmethod
    def getDescription(self):
        raise NotImplemented("Subclasses must implement this method")
    
    # Reset stats for when a card is Returned or Discarded
    @abstractmethod
    def resetStats(self):
        raise NotImplemented("Subclasses must implement this method")
    


    # Basic function for entering a lane
    def onBeingPlayed(self, enteredLane: 'Lane'):

        for playMod in self.bePlayedModifiers:
            playMod.modify(self, Lane)

        # ALWAYS go to entering a lane after
        self.onEnterLane(Lane)


    # Basic function for entering a lane
    # This also changes the card's lane value
    def onEnterLane(self, enteredLane: 'Lane'):
        self.lane_index = Lane.lane_index

        for enterMod in self.enterLaneModifiers:
            enterMod.modify(self, Lane)


    # Basic function for the card being returned
    def onReturned(self, returnedByCard: Card):
        for returnMod in self.returnedModifiers:
            returnMod.modify(self, returnedByCard)
        
        self.resetStats()

        # Call remote function to return this card, with possibility to call specific player(s)


    # Basic function for the card being discarded
    def onDiscarded(self):
        for discMod in self.discardedModifiers:
            discMod.modify(self)
        
        self.resetStats()

        # Call remote function to discard this card




    # Basic function for abilities that trigger upon round start
    def onRoundStart(self, round: int):
        for rsMod in self.roundStartModifiers:
            rsMod.modify(self, round)


    # Basic function for abilities that trigger upon turn start
    def onTurnStart(self):
        for tsMod in self.turnStartModifiers:
            tsMod.modify(self)


    # Basic function for abilities that trigger upon night start
    def onNightStart(self):
        for nsMod in self.nightStartModifiers:
            nsMod.modify(self)


    # Basic function for abilities that trigger upon night end
    def onNightEnd(self):
        for neMod in self.nightEndModifiers:
            neMod.modify(self)


    # Basic function for abilities that trigger upon round end
    def onRoundEnd(self):
        for reMod in self.nightEndModifiers:
            reMod.modify(self)



    # Basic function for abilities that trigger upon another card entering the field
    def onOtherCardPlayed(self, otherCard: Card, playedInLane: 'Lane'):
        for otherPlayedMod in self.otherCardPlayedModifiers:
            otherPlayedMod.modify(self, otherCard, playedInLane)


    # Basic function for abilities that trigger upon another card leaving a lane for any reason
    def onOtherCardLeaves(self, otherCard: Card, leavesLane: 'Lane', leftBecause: str):
        for otherLeftMod in self.otherCardLeavesModifiers:
            otherLeftMod.modify(self, otherCard, leavesLane, leftBecause)
