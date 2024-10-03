from abc import ABC, abstractmethod
from enum import Enum
from .modifiers import *



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

                 weakness_descriptions: list[str] = [],
                 ability_descriptions: list[str] = []
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

        self.weakness_description = weakness_descriptions  # Descriptions of all weaknesses
        self.base_wd = weakness_descriptions  # Weaknesses which the base card has
        self.ability_description = ability_descriptions  # Descriptions of all abilities
        self.base_ad = ability_descriptions  # Abilities which the base card has

        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field.
        
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

    

    # Provides description that shows what the abilities of the class are
    @abstractmethod
    def get_description(self):
        raise NotImplemented("Subclasses must implement this method")
    
    # Reset stats for when a card is Returned or Discarded
    @abstractmethod
    def reset_stats(self):
        raise NotImplemented("Subclasses must implement this method")
    


    # Basic function for entering a lane
    def on_being_played(self, entered_lane: 'Lane'):

        for playMod in self.be_played_modifiers:
            playMod.modify(self, entered_lane)

        # ALWAYS go to entering a lane after
        self.on_enter_lane(entered_lane)


    # Basic function for entering a lane
    # This also changes the card's lane value
    def on_enter_lane(self, entered_lane: 'Lane'):
        self.lane_index = entered_lane.lane_index

        for enterMod in self.enter_lane_modifiers:
            enterMod.modify(self, entered_lane)


    # Basic function for the card being returned
    def on_returned(self, returned_by_card: 'Card'):
        for returnMod in self.returned_modifiers:
            returnMod.modify(self, returned_by_card)
        
        self.reset_stats()

        # Call remote function to return this card, with possibility to call specific player(s)


    # Basic function for the card being discarded
    def on_discarded(self):
        for discMod in self.discarded_modifiers:
            discMod.modify(self)
        
        self.reset_stats()

        # Call remote function to discard this card




    # Basic function for abilities that trigger upon round start
    def on_round_start(self, round: int):
        for rsMod in self.round_start_modifiers:
            rsMod.modify(self, round)


    # Basic function for abilities that trigger upon turn start
    def on_turn_start(self):
        for tsMod in self.turn_start_modifiers:
            tsMod.modify(self)


    # Basic function for abilities that trigger upon night start
    def on_night_start(self):
        for nsMod in self.night_start_modifiers:
            nsMod.modify(self)


    # Basic function for abilities that trigger upon night end
    def on_night_end(self):
        for neMod in self.night_end_modifiers:
            neMod.modify(self)


    # Basic function for abilities that trigger upon round end
    def on_round_end(self):
        for reMod in self.round_end_modifiers:
            reMod.modify(self)



    # Basic function for abilities that trigger upon another card entering the field
    def on_other_card_played(self, other_card: 'Card', played_in_lane: 'Lane'):
        for otherPlayedMod in self.other_card_played_modifiers:
            otherPlayedMod.modify(self, other_card, played_in_lane)


    # Basic function for abilities that trigger upon another card leaving a lane for any reason
    def on_other_card_leaves(self, other_card: 'Card', leaves_lane: 'Lane', left_because: str):
        for otherLeftMod in self.other_card_leaves_modifiers:
            otherLeftMod.modify(self, other_card, leaves_lane, left_because)
