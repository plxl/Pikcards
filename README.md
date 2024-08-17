# Table of contents
Please note that this current version only takes into account Minion-type cards

1. [Suggestions for basic additions](#suggestions-for-basic-additions)
2. [Traits on Minions](#traits-on-minions)  
[Defense](#defense)  
[Explosive](#explosive)  
[Gloom](#gloom)  
[First Strike](#first-strike)  
[Burrowing (!)](#burrowing)  
[Digging](#digging)  
[Explorer](#explorer)  
[Multi-Attack](#multi-attack)  
[Up High](#up-high)  
[Indirect](#indirect)  
[Swarm](#swarm)  
[Dolphin Part](#dolphin-part)  
[Debt Treasure](#debt-treasure)  
[Pikmin](#pikmin)  
[Wall](#wall)  
[Passive](#passive)  

3. [Basic Triggers for Minions](#basic-triggers-for-minions)  
[Deal Damage](#deal-damage)  
[Take damage + Weaknesses](#take-damage--weaknesses)  
[Be played](#be-played)  
[Enter a Lane](#enter-a-lane)  
[Discarded](#discarded)  
[Return](#return)  

4. [Ability Triggers on Minions](#ability-triggers-on-minions)  


5. [Game/Player actions triggered by Cards](#gameplayer-actions-triggered-by-cards)  
[Draw](#draw)  
[Conjure](#conjure)  
[Shuffle into Deck](#shuffle-into-deck)  





# Suggestions for basic additions:
- Separate **Health** and **MaxHealth** in cards. This way, cards won't heal over their base HP, but can still have HP increased by OverHeal.
- Give cards a **Defense** attribute, to make it simpler with calculating damage.
- Attribute for whether a card is currently **underground**
- Attribute for whether a card has **un-burrowed** during the current Round
- Add **Max Items** or any Carry Limit to Minions, so they can keep track of how many Items they can hold
- Add counter for how many turns a **Wall** has been on the field
- If there are two cards in the same lane, but neither are **dealing AND taking damage**, decrease their HP by one at the **end of the Night** (ignoring defense)
- Some form of cards **subscribing** to a function on the field that sends them if a new card has been played. Specifically for cards that react to other cards entering the field. This way, said cards may be pulled into that lane or trigger abilities.
- If a player has no cards to draw when they attempt to do so, they take 1 Health of damage.






# Traits on Minions
Traits that Minions can have, and their potential function


## Defense
Not so much a trait. ***Should be an attribute within the class itself, like Health and Attack are***.
Each point of *Defense* lowers damage *taken* by one.


## Explosive
While this is an attack type, cards with this type also *ignore* one (1) Defense on their opponent, essentially piercing said Defense.


## Gloom
While this is an attack type, cards with this type also *ignore* all Defense on their opponent, essentially piercing said Defense.

Gloom enemies can also damage opponents that are *Buried*, meaning they will not target the opposing player if a buried card is in a lane they are attacking.


## First Strike
Cards with First Strike perform their attacks before any other card does in their lane, giving them attack priority. This makes it so First Strike cards that defeat an opponent, don't get attacked in return.


## Burrowing
These cards can be "put underground" during their Player turn. "Burrowed" cards normally cannot be damaged, attacks in their lane instead going to the Player behind them.
When burrowed, said card will:
- Heal at the **end of the round**
- Un-burrow at the **Start of the next round**
- **Never** perform a basic attack

When a card un-burrows, it won't be able to bury during that same round

***I suggest to keep track of the following:***
- Whether they are buried or not
- Whether they un-buried during a round
- At the **end of the round**, reset the un-buried values of all cards that have it on true (so they can burrow again on the following round. Could be done after the check for Healing them 1HP)


## Digging
Cards with Digging are able to attack burrowed opponents.

On top of this, Digging cards deal **+2 Damage** to any Burrowed opponent.


## Explorer
When played into an Area, they will cost 1 less energy.
They are **OverHealed** 2HP when they are either played into an Area, or when an Area is played on the lane they are in.


## Multi-Attack
Will attack a second time after their first attack has landed


## Up High
A Trait that mainly other cards will check if you have. This is mainly used by *Areas*, since any Up High Minions aquire different effects from an *Area* than non-Up High cards would.

a.k.a. this doesn't do much special in the Minion itself, making this more like an attacking element gameplay-wise


## Indirect
A Trait that mainly other cards will check if you have. For example Counter-attacks or certain abilities won't trigger when hit by this.

a.k.a. this doesn't do much special in the Minion itself, making this more like an attacking element gameplay-wise


## Swarm
A Trait that mainly other cards will check if you have.

a.k.a. this doesn't do much special in the Minion itself, making this more like an attacking element gameplay-wise


## Dolphin Part
A Trait that mainly other cards will check if you have.

a.k.a. this doesn't do much special in the Minion itself, making this more like an attacking element gameplay-wise.


## Debt Treasure
A Trait that mainly other cards will check if you have.

a.k.a. this doesn't do much special in the Minion itself, making this more like an attacking element gameplay-wise.


## Pikmin
For each Pikmin on your side of the field, *Time* cost of *Items* goes down by one, not going below zero.

Additionally, during the owner turn, Pikmin can be [returned](#return) by spending double their time cost. When doing this, said Card's Time cost will become that value.


## Wall
They have a counter which ticks down. After three round on the field, they are discarded.  
Walls will not have Item effects applied to them while on the field.  
Walls cannot have their attack be increased.


## Passive
Passive cards cannot have their attack power increased from outside sources while on the field.  
When a Passive card attacks another Passive card or a [Wall](#wall), it only deals on damage.




# Basic Triggers for Minions

## Deal damage
**Basic:** Send *Attack Power* to all cards you are damaging. Also send your *traits and elements* so they may know whether they trigger theri own abilities and weaknesses.

**Possible difference:** Some may need to check the target for any elements or Traits, to know what type of attack to perform.
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   


## Take damage + Weaknesses
**Basic:** Receive the *attack power, traits and elements* from the attacker.  
Reduce any Defense from the attack power. If both the attacker and card itself are Passive, turn the received damage to 1.  
Then reduce HP by the final calculated result.  
If HP hits or goed below 0, the card [dies](#discarded)

**Possible difference:** Cards with ***Weaknesses*** will have additional calculations here, if the attacker has certain characteristics.  
Additionally, some cards may receive damage entirely differently, like halving all damage taken or returning opponents that deal certain amounts of damage.
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   


## Be played
**Basic:** Card is either played onto the field, or is revealed from being a Mystery Card.  
This also triggers when Summoned from a different card, which essentially is [conjuring](#conjure), but instead of gaining the card into your hand, it immediately enters the field.  
Being played always leads into [entering a lane](#enter-a-lane).

**Possible difference:** Some cards may have abilities thattrigger when it gets played.
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   


## Enter a lane
**Basic:** This *ALWAYS* happens when a card is [played](#be-played) onto the field.  
A card can also enter a lane by being moved into one.  
Other cards may receive note that you entered a lane and react to this. ([see suggestions](#suggestions-for-basic-additions))

**Possible difference:** Some cards may trigger abilities when the enter a lane.
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   


## Discarded
**Basic:** When triggered, the card is discarded from the field.

**Possible difference:** Some cards may trigger an ability upon being removed from the field
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   - 


## Return
**Basic:** When triggered, the card loses its items and after this is done is sent back to a player's hand.  
Usually, the card reverts back to its base stats. However, [Pikmin](#pikmin) cards will not have their Time cost reverted.  
***Since a card does not have to necessarily go back to its owner, a player has to be sent with the Return function.***

**Possible difference:** Some cards may trigger an ability upon being removed from the field
**Cards with abilities that affect this:**
Set 0 |  Set 1  |  Set 2  |  Set C  
---   |   ---   |   ---   |   ---   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   -   
\-   |   -   |   -   |   - 






# Game/Player actions triggered by Cards

## Draw
Player draws a certain amount of cards from the top of their deck.  
This is automatically called when a Round starts, but may be called from other places.  
***Drawing cards will not happen if a drawn card would put their hand above 10 cards held.***  
***If a player has no cards to draw, they take 1 damage for each card they would have pulled.***


## Conjure
Add a card into a player's hand that is not necessarily part of their deck.  
***Conjuring cards will not happen if a conjured card would put their hand above 10 cards held.***


## Shuffle into Deck
A new card/cards are placed in random spots into the deck. These cards don't need to be in the base deck per se.