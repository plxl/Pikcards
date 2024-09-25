from card import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from item import Item


"""
    TO DO:
    - Make owner get nectar if card is killed while petrified in onDiscarded
    - Make walls discard upon reaching timer in onRoundStart
    - Stalemate/Staredown damage, using a Minion's hasBeenDamaged

    - If a Minion with Items is Discarded or Returned, first Discard their Items, then perform the Minion action

    - The entirity of Bubbled
"""






# Base minion data, stats and actions
class Minion(Card):
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

                 base_attack,
                 base_health,
                 defense,
                 maxcarry,

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

        # Attributes unique to Minions
        self.base_attack = base_attack  # Standard attack power of the card
        self.attack = base_attack  # Current attack power of the card
        self.base_health = base_health  # Standard Max Health of the card, used to prevent a card from healing over this number
        self.max_health = base_health  # Max Health of the card in gameplay, can be changed by Overhealing and such
        self.health = base_health  # Current Health of the card, used to calculate how much damage was taken
        self.base_defense = defense  # Standard max Defense of the card
        self.defense = defense  # Defense of the card
        self.maxcarry = maxcarry  # Maximum number of Items this card can hold
        self.heldItems: list['Item'] = []  # Items that this is holding

        self.blind = False  # Whether the card is displayed as a Blind Card
        self.burrowed = False  # Whether the card is burrowed
        self.just_unburrowed = False  # Whether the card has unburrowed during the round
        self.wallcounter = 0  # Counter for wall cards being on the field
        self.stun = False  # Whether the card is stunned
        self.petrified = False  # Whether the card is petrified
        self.petrified_nightstarted = False  # So petrified cards know Night has begun
        self.panic = False  # Whether the card is panicked
        self.panicCounter = 0  # Counts the rounds it has been panicked, max of 3
        self.bubble_time = 0  # Whether the card is bubbled. If the card has bubble, this is set to 12. If zero, it is not bubbled.
        self.hasBeenDamaged = False  # Whether the card took damage this turn, for stalemate/staredown damage

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

        self.dealDamageModifiers: list[DealDamageModifier] = []
        self.takeDamageModifiers: list[TakeDamageModifier] = []
        self.beKilledModifiers: list[BeKilledModifier] = []


    # Provides description that shows what the abilities of the class are
    def getDescription(self):
        description: str = "MINION\n"
        if len(self.weaknessDescription) > 0:
            description += "WEAKNESSES:\n"
            description += "\n".join(self.weaknessDescription)
            description += "\n"
        
        if len(self.abilityDescription) > 0:
            description += "ABILITIES:\n"
            description += "\n".join(self.abilityDescription)
        return description

    # Reset stats for when a card is Returned or Discarded
    def resetStats(self):
        self.lane_index = -1
        self.attack = self.base_attack
        self.max_health = self.base_health
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
        self.panicCounter = 0
        self.bubble_time = 0
        self.hasBeenDamaged = False
        self.weaknessDescription = self.base_wd
        self.abilityDescription = self.base_ad




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
            ac = AttackClass(damage, self.lane_index, targetside, self)

            for attMod in self.dealDamageModifiers:
                ac = attMod.modify(ac)
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
                self.panicCounter = 0
                print(f"{self.name} is no longer Panicking")


    # Basic function for taking damage, without weaknesses
    # If the card takes damage, remove Panicked state
    def takeDamage(self, incomingAttack: AttackClass):
        # Apply take damage modifiers
        modifiedAttack = incomingAttack
        for attMod in self.takeDamageModifiers:
            modifiedAttack = attMod.modify(self, modifiedAttack)
        
        damage = modifiedAttack.damageValue
        
        attackerTraits = modifiedAttack.attackerCard.traits

        # Check if immune
        if bool(set(modifiedAttack.attackerCard.elements).intersection(self.immunities)) or bool(set(attackerTraits).intersection(self.immunities)):
            print(f"{self.name} was immune to the attack")
        
        elif "Passive" in self.traits and "Passive" in attackerTraits:
            self.applyDamageOnDefense(1, attackerTraits)

        elif self.burrowed and "Digging" in attackerTraits:
            damage += 2
            self.applyDamageOnDefense(damage, attackerTraits)
        
        else:
            self.applyDamageOnDefense(damage, attackerTraits)


    # Minion function for the card being discarded, checks if killed by another cards as well
    def onDiscarded(self, killedBy: Card = None):
        if killedBy is not None:
            for killedMod in self.beKilledModifiers:
                killedMod.modify(self, killedBy)

            if self.petrified:
                # Provide the owner with Nectar
                print(f"{self.name} was killed while Petrified, so its owner should get a Nectar!")
        
        for discMod in self.discardedModifiers:
            discMod.modify(self)
        
        self.resetStats()

        # Call remote function to discard this card


    # Minion Function for being healed
    def beHealed(self, amount: int, overheal: bool = False):
        if overheal:
            print(f"{self.name} overhealed by {amount} Health")
            self.health += amount
            if self.health > self.max_health:
                self.max_health = self.base_health
        else:
            self.health = min(self.max_health, self.health + amount)
            print(f"{self.name} healed by {amount} Health")




    def onRoundStart(self, round: int):
        if "Wall" in self.traits:
            self.wallcounter += 1

        self.hasBeenDamaged = False

        if self.burrowed:
            self.burrowed = not self.burrowed
            self.just_unburrowed = True
            print(f"{self.name} just unburrowed")

        if self.wallcounter < 3:
            for rsMod in self.roundStartModifiers:
                rsMod.modify(self, round)
        else:
            print(f"{self.name} is a long-lasting wall and disappears")
            # Call remote function to discard this


    def onRoundEnd(self):
        if self.panic:
            self.panicCounter += 1

            if self.panicCounter > 2:
                self.panic = not self.panic
                self.panicCounter = 0
                print(f"{self.name} is no longer Panicking")
        
        if self.burrowed:
            self.beHealed(1)

        if self.just_unburrowed:
            self.just_unburrowed = not self.just_unburrowed
        
        for reMod in self.nightEndModifiers:
            reMod.modify(self)


    def onNightStart(self):
        if self.petrified:
            self.petrified_nightstarted = True
        
        for nsMod in self.nightStartModifiers:
            nsMod.modify(self)


    def onNightEnd(self):
        if self.petrified and self.petrified_nightstarted:
            self.petrified = not self.petrified
            self.petrified_nightstarted = not self.petrified_nightstarted
            print(f"{self.name} is no longer Petrified")
        
        for neMod in self.nightEndModifiers:
            neMod.modify(self)
