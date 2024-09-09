import json
from enum import Enum
from os import listdir
from os import path, getcwd


"""
    TO DO:
    - Make this able to import Lane classes
        - This will make the performAttack function much more versatile, and able to check for things like Snagret weaknesses and Crawmad

    - Remove requirement of parser and json files (def ToJSON and part of def load_cards)
    - Turn CardElement and CardTrait into actual used elements
    - Simplify rarity Enum

    - die/discarded
        - If happens when petrified, provide Nectar
    - make player draw
    - make player conjure
    - setStatus (blind, burrow, stun, petrified, panic, bubble)

    - start round
        - If wall, increase. If 3, die
    - start of night
    - end of night
    - end of round

    - change Items held (both for gaining and losing one)
"""



# Classes that a card can have
class CardClass:
    NONE = 0
    FIGHTING = 1
    TRAPPERS = 2
    SURVIVAL = 3
    BOOSTER = 4
    HANDY = 5

# Types that a card can have
class CardType:
    Minion = 0
    Item = 1
    Area = 2
    Exploration = 3

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

# Traits a card can have
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



# Data needed to perform an attack
class AttackClass:
    def __init__(self, damageValue: int, targetLane: int, targetPlayer: int, attackElements, attackTraits):
        self.damageValue = damageValue  # Amount of damage being sent
        self.attackElements = attackElements  # Elements of the sent attack
        self.attackTraits = attackTraits  # Traits of the sent attack
        self.targetLane = targetLane  # Lane which is targeted
        self.targetPlayer = targetPlayer  # Side which is targeted (int)



# Base card abilities and stats
class Card:
    def __init__(self, 
            set,
            number,
            fifth,
            rarity,
            name,
            image,
            cardclass,
            cardtype,
            base_energy,
            base_time,
            base_attack,
            base_health,
            defense,
            maxcarry,
            elements,
            immunities,
            weaknesses,
            traits,
            abilities,
            additions,
            notes):
        self.set = set
        self.number = number
        self.fifth = fifth
        self.rarity = rarity
        self.name = name
        self.image = image
        self.cardclass = cardclass
        self.cardtype = cardtype

        self.base_energy = base_energy  # Standard energy cost of the card
        self.energy = base_energy  # current energy cost of the card
        self.base_time = base_time  # Standard time cost of the card
        self.time = base_time  # Current time cost of the card
        self.base_attack = base_attack  # Standard attack power of the card
        self.attack = base_attack  # Current attack power of the card
        self.base_health = base_health  # Standard Max Health of the card, used to prevent a card from healing over this number
        self.health = base_health  # Current Health of the card, used to calculate how much damage was taken
        self.base_defense = defense  # Standard max Defense of the card
        self.defense = defense  # Defense of the card
        self.maxcarry = maxcarry  # Maximum number of Items this card can hold

        self.elements = elements
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.traits = traits
        self.abilities = abilities
        self.additions = additions  # Should be removed once no longer needed
        self.notes = notes  # Should be removed once no longer needed

        self.blind = False  # Whether the card is displayed as a Blind Card
        self.burrowed = False  # Whether the card is burrowed
        self.just_unburrowed = False  # Whether the card has unburrowed during the round
        self.wallcounter = 0  # Counter for wall cards being on the field
        self.stun = False  # Whether the card is stunned
        self.petrified = False  # Whether the card is petrified
        self.petrified_nightstarted = False  # So petrified cards know Night has begun
        self.panic = False  # Whether the card is panicked
        self.bubble_time = 0  # Whether the card is bubbled. If the card has bubble, this is set to 12. If zero, it is not bubbled.

        self.hasBeenDamaged = False  # Whether the card took damage this turn
        self.owner: int = -1  # Owner player, p1 is 0, p2 is 1
        self.lane_index: int = -1  # Lane this is currently in. -1 for cards outside the field
    

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




    # Basic attack function.
    # Returns a list of targets (temporary)
    def performAttack(self):
        attacks: list[AttackClass] = []

        if self.stun:
        # If stunned, do not attack, but remove the Stun
            self.stun = False
            return attacks
        
        elif not self.burrowed and not self.petrified:
            # If not burrowed and not petrified, perform attack in this lane
            targetside = 0
            damage = self.attack

            if self.owner == 0:
                targetside = 1

            # If Panicked, only deal 1 damage
            if self.panic:
                damage = 1

            # Create the attack
            ac = AttackClass(damage, self.lane_index, targetside, self.elements, self.traits)
            attacks.append(ac)

            return attacks

        # Else it is always either burrowed or petrified, so don't attack
        return attacks
            
    
    # Used by takeDamage only
    def applyDamageOnDefense(self, damage, traits):
        defense = self.defense
        finaldamage = damage

        if self.petrified:
            defense = 0
            finaldamage += 2
        elif "Gloom" in traits:
            defense = 0
        elif "Explosive" in traits and defense > 0:
            defense -= 1
        
        finaldamage = max(0, finaldamage - defense)
        self.health -= finaldamage
        
        print(f"{self.name} took {finaldamage} damage!")

        # Set to damage taken and remove Panic upon taking any damage
        if finaldamage > 0:
            self.hasBeenDamaged = True

            if self.panic:
                self.panic = not self.panic
                print(f"{self.name} is no longer Panicking")


    # Basic function for taking damage, without weaknesses
    # If the card takes damage, remove Panicked state
    def takeDamage(self, incomingAttack: AttackClass):
        damage = incomingAttack.damageValue
        
        # Check if immune
        if bool(set(incomingAttack.attackElements).intersection(self.immunities)) or bool(set(incomingAttack.attackTraits).intersection(self.immunities)):
            print(f"{self.name} was immune to the attack")
        
        elif "Passive" in self.traits and "Passive" in incomingAttack.attackTraits:
            self.applyDamageOnDefense(1, incomingAttack.attackTraits)

        elif self.burrowed and "Digging" in incomingAttack.attackTraits:
            damage += 2
            self.applyDamageOnDefense(damage, incomingAttack.attackTraits)
        
        else:
            self.applyDamageOnDefense(damage, incomingAttack.attackTraits)


    # Reset stats for when a card is Returned or Discarded
    def resetStats(self):
        self.lane_index = -1
        self.attack = self.base_attack
        self.health = self.base_health
        self.energy = self.base_energy
        self.time = self.base_time
        self.defense = self.base_defense
        self.blind = False
        self.burrowed = False
        self.just_unburrowed = False
        self.wallcounter = 0
        self.stun = False
        self.petrified = False
        self.petrified_nightstarted = False
        self.panic = False
        self.bubble_time = 0
        self.hasBeenDamaged = False
        

    # Loads all existing cards from individual json files
    def load_cards():
        folder = path.join(getcwd(), "cards", "json")
        jsons = [
            path.join(folder, j) for j in listdir(folder) if j.lower().endswith(".json")
        ]

        print("Loading Cards...")
        for j in jsons:
            # print(f'Loading {j}...')
            f = open(j, "r")
            Cards.append(json.loads(f.read(), object_hook=lambda d: Card(**d)))
            f.close()


    # Turns card data into a json file, used by the parser
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


# List containing all cards
Cards: list[Card] = []