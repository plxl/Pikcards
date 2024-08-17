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

4. [Other Triggers for specific cards](#other-triggers-for-specific-cards)  
[Different card enters field/lane](#a-different-card-enters-the-fieldlane)  
[Different card leaves field/lane](#a-different-card-leaves-the-fieldlane)   

5. [Game/Player actions](#gameplayer-actions)  
[Draw](#draw)  
[Conjure](#conjure)  
[Shuffle into Deck](#shuffle-into-deck)  
[Start of Round](#start-of-round)  
[Start of Night](#start-of-night)  
[End of Night](#end-of-night)  
[End of Round](#end-of-round)  

6. [Abilities not (fully) Taken into account](#abilities-not-fully-taken-into-account)  






# Suggestions for basic additions:
- Separate **Health** and **MaxHealth** in cards. This way, cards won't heal over their base HP, but can still have HP increased by OverHeal.
- Give cards a **Defense** attribute, to make it simpler with calculating damage.
- Attribute for whether a card is currently **underground**
- Attribute for whether a card has **un-burrowed** during the current Round
- Add **Max Items** or any Carry Limit to Minions, so they can keep track of how many Items they can hold
- Add counter for how many turns a **Wall** has been on the field
- If there are two cards in the same lane, but neither are **dealing AND taking damage**, decrease their HP by one at the **end of the Night** (ignoring defense)
- Some form of cards **subscribing** to a function on the field that sends them if a new card has been played or removed. Specifically for cards that react to other cards entering or leaving the field. This way, said cards may be pulled into that lane or trigger abilities.
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
**Basic:** Send *Attack Power* to all cards you are damaging. Also send your *traits and elements* so they may know whether they trigger their own abilities and weaknesses.

**Possible difference:** Some may need to check the target for any elements or Traits, to know what type of attack to perform.
**Cards with abilities that affect this:**
Set 0              | Set 1 | Set 2 | Set C 
---                |  ---  |  ---  |  ---  
Puckering Blinnow-3|  021  |  014,w  | 006-2 
\-                 |  025  | 019-2 | 009-3  
\-                 | 030-2 |  021  |  024 
\-                 | 036-2 | 026a-2| 026-1  
\-                 | 038-2 | 033-2 |   -   
\-                 |   -   |  039  |   -   
\-                 |   -   | 041-1 |   -   
\-                 |   -   |  043  |   -   
\-                 |   -   | 046-2 |   -   
\-                 |   -   |048-1,2|   -   
\-                 |   -   |051-1,2|   -   
\-                 |   -   | 053-3 |   -   
\-                 |   -   | 098-2 |   -   
\-                 |   -   | 102-1 |   -   
\-                 |   -   |   -   |   -   


## Take damage + Weaknesses
**Basic:** Receive the *attack power, traits and elements* from the attacker.  
Reduce any Defense from the attack power. If both the attacker and card itself are Passive, turn the received damage to 1.  
Then reduce HP by the final calculated result.  
If HP hits or goed below 0, the card [dies](#discarded)

**Possible difference:** Cards with ***Weaknesses*** will have additional calculations here, if the attacker has certain characteristics.  
Additionally, some cards may receive damage entirely differently, like halving all damage taken or returning opponents that deal certain amounts of damage.
**Cards with abilities that affect this:**
Cards with a '\*' have this triggered due to their being [Wall](#wall) or [Passive](#passive), and being attacked by another *Passive* card.  
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---   
\-    | 003*-1|005-1,2|  002 
\-    | 004*-1| 004*-1|  003*  
\-    | 006*-1| 006*-1| 004*-1
\-    |  007* | 007*-2|006-1,3
\-    |  009* | 008*-1|  007* 
\-    |  010* |  009* |  008  
\-    |  011* |  015* |  011*  
\-    | 026*-2|  023* |  014  
\-    |  027* | 024*-2|  016*  
\-    | 034*-1|  027* |  021* 
\-    | 035-2 |  028* |  022* 
\-    |  035* |  036* |  024*
\-    |  072* |  037  |  025*
\-    |  073* |  038* |  026* 
\-    |  074* |  039* |  029* 
\-    |  075* | 041-2 |  030 
\-    |   -   |  042* |   -   
\-    |   -   |  043* |   -   
\-    |   -   | 050-2 |   -   
\-    |   -   | 097*-1|   -   
\-    |   -   | 098*-1|   -   
\-    |   -   | 099*-1|   -   
\-    |   -   | 100*-1|   -   
\-    |   -   |  101* |   -   
\-    |   -   |  102* |   -   
\-    |   -   |   -   |   -   
  
**Cards with weaknesses triggered in this:**
Set 0      | Set 1 | Set 2 | Set C 
---        |  ---  |  ---  |  ---  
Albino D.B.|  003  | 008-1 |  003  
\-         |  006  |  009  | 005-1  
\-         |  009  |  010  | 011-1 
\-         |  013  |  013  |  024  
\-         |  015  |  020  |  026  
\-         |  017  |  021  |  029  
\-         |  018  |  023  |  030  
\-         |  019  |  026  |   -   
\-         |  025  |  028  |   -   
\-         |  029  |  029  |   -   
\-         | 034-1 |  030  |   -   
\-         |  035  |  031  |   -   
\-         |  036  |  032  |   -   
\-         |  075  |  033  |   -   
\-         |   -   |  034  |   -   
\-         |   -   |  038  |   -   
\-         |   -   |  039  |   -   
\-         |   -   |  045  |   -   
\-         |   -   |  046  |   -   
\-         |   -   | 099-1 |   -   
\-         |   -   |  102  |   -   
\-         |   -   |   -   |   -   


## Be played
**Basic:** Card is either played onto the field, or is revealed from being a Mystery Card.  
This also triggers when Summoned from a different card, which essentially is [conjuring](#conjure), but instead of gaining the card into your hand, it immediately enters the field.  
Being played always leads into [entering a lane](#enter-a-lane).

**Possible difference:** Some cards may have abilities that trigger when it gets played.  
**Cards with abilities that affect this:**
Set 0              | Set 1 | Set 2 | Set C 
---                |  ---  |  ---  |  ---  
Puckering Blinnow-1|001-1,2| 001-2 |009-1,2  
Puckering Blinnow-2|  017  | 002-2 |  010 
\-                 |  031  | 003-1 |  012  
\-                 |  033  | 019-1 |  013  
\-                 | 036-1 | 028-1 |  015  
\-                 | 039-3 |  034  |020-1,2  
\-                 |   -   |  038  |023-1,2 
\-                 |   -   |  039  |  025 
\-                 |   -   | 045-2 | 026-2  
\-                 |   -   |054-1,3|   -   
\-                 |   -   | 102-2 |   -   
\-                 |   -   |   -   |   -   


## Enter a lane
**Basic:** This *ALWAYS* happens when a card is [played](#be-played) onto the field.  
A card can also enter a lane by being moved into one.  
Other cards may receive note that you entered a lane and react to this. ([see suggestions](#suggestions-for-basic-additions))

**Possible difference:** Some cards may trigger abilities when the enter a lane.  
**Cards with abilities that affect this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    |  018  |  027  |   -   
\-    |  019  | 052-2 |   -   
\-    | 030-1 |   -   |   -   
\-    |   -   |   -   |   -   


## Discarded
**Basic:** When triggered, the card is discarded from the field.

**Possible difference:** Some cards may trigger an ability upon being removed from the field  
**Cards with abilities that affect this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    |  004  |  004  |  001  
\-    |  007  |  006  |  016  
\-    |  010  |  007  | 026-3
\-    |  020  | 016-1 |  029  
\-    | 027-1 |  018  |  109  
\-    | 075-2 |  049  |   -   
\-    |   -   |  101  |   -   
\-    |   -   |   -   |   -   


## Return
**Basic:** When triggered, the card loses its items and after this is done is sent back to a player's hand.  
Usually, the card reverts back to its base stats. However, [Pikmin](#pikmin) cards will not have their Time cost reverted.  
***Since a card does not have to necessarily go back to its owner, a player has to be sent with the Return function.***

**Possible difference:** Some cards may trigger an ability upon being removed from the field  
**Cards with abilities that affect this:**  
Cards with a '\*' have this triggered due to their [Pikmin Trait](#pikmin). They will, in that case, check whether their Onion is on the side of the field.  
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    |  002* | 003*,2|  001* 
\-    |  005* |  005* |  026*  
\-    |  009* |  017* |   -   
\-    |  020  |  018  |   -   
\-    |  031* |  102* |   - 
\-    |   -   |   -   |   - 





# Other Triggers for specific cards

## A different card enters the field/lane
Some cards may trigger an ability upon a different card being played, or more specifically a different card entering their own or adjacent lanes  
**Cards with abilities that subscribe to this:**
Set 0                | Set 1 | Set 2 | Set C 
---                  |  ---  |  ---  |  ---  
Puckering Blinnow-2,w|  018  | 026u-1|009-2,w  
\-                   |  019  | 029-1 | 023-2  
\-                   |  031  | 030-1 |   -   
\-                   |   -   | 031-1 |   -   
\-                   |   -   | 032-1 |   - 
\-                   |   -   | 033-1 |   -   
\-                   |   -   |  034  |   - 
\-                   |   -   | 050-1 |   - 
\-                   |   -   | 052-1 |   - 
\-                   |   -   |   -   |   - 


## A different card leaves the field/lane
Some cards may trigger an ability upon a different card being removed, or more specifically a different card leaving their own or adjacent lanes in certain ways  
**Cards with abilities that subscribe to this:**
Set 0              | Set 1 | Set 2 | Set C 
---                |  ---  |  ---  |  ---  
Puckering Blinnow-2|  018  |  034  | 009-2 
\-                 |  019  |   -   | 032-2 
\-                 |  031  |   -   |   -   
\-                 |   -   |   -   |   -   





# Game/Player actions

## Draw
Player draws a certain amount of cards from the top of their deck.  
This is automatically called when a Round starts, but may be called from other places.  
***Drawing cards will not happen if a drawn card would put their hand above 10 cards held.***  
***If a player has no cards to draw, they take 1 damage for each card they would have pulled.***  

Certain cards need to know when a player pulls a card, so they may need to subscribe to an event that lets them know this.  
**Cards with abilities that subscribe to this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 038-1 | 045-1 |   -   
\-    |   -   |   -   |   -   


## Conjure
Add a card into a player's hand that is not necessarily part of their deck.  
***Conjuring cards will not happen if a conjured card would put their hand above 10 cards held.***

Certain cards need to know when a player pulls a card, so they may need to subscribe to an event that lets them know this.  
**Cards with abilities that subscribe to this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 038-1 |023-2,w|   -   
\-    |   -   | 045-1 |   -   
\-    |   -   |   -   |   -   


## Shuffle into Deck
A new card/cards are placed in random spots into the deck. These cards don't need to be in the base deck per se.


## Start of Round
Some abilities may be triggered at the start of the Round, after certain other things have been done.  
**Cards with abilities that subscribe to this:**
Set 0      | Set 1 | Set 2 | Set C 
---        |  ---  |  ---  |  ---  
Albino D.B.|  022  |  015  | 007-1
\-         |   -   |  027  |   -   
\-         |   -   | 040-1 |   -   
\-         |   -   | 044-1 |   -   
\-         |   -   |   -   |   - 


## Start of Night
Some abilities may be triggered at the start of the Night, after certain other things have been done.  
**Cards with abilities that subscribe to this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 026-1 |023-1,w|  022 
\-    |   -   | 024-1 |   -   
\-    |   -   |   -   |   -   


## End of Night
Some abilities may be triggered at the end of the Night, after certain other things have been done.  
**Cards with abilities that subscribe to this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 037-1 | 044-2 |   -   
\-    |   -   |   -   |   -   


## End of Round
Some abilities may be triggered at the end of the Round, after certain other things have been done.  
**Cards with abilities that subscribe to this:**
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 027-2 |  020  |  011  
\-    | 075-1 | 026u-2|   -   
\-    |   -   | 028-2 |   -   
\-    |   -   |   -   |   -   





# Abilities not (fully) taken into account
Abilities that would only allow for Counter-attacking have a '\*'
Set 0 | Set 1 | Set 2 | Set C 
---   |  ---  |  ---  |  ---  
\-    | 001-1 | 001-1 | 006-1* 
\-    |  011  | 002-2 |020-1,2 
\-    |  012  |  009  |  025
\-    |  013  | 016-2 |  020w 
\-    |  034* |  022  |   -   
\-    | 035-1 | 026a-1|   -   
\-    | 037-2 | 029-2 |   -   
\-    |039-1,2| 030-2 |   -   
\-    |  028w | 031-2 |   -   
\-    |   -   | 032-2 |   -   
\-    |   -   |  035  |   -   
\-    |   -   |  036  |   -   
\-    |   -   | 040-2 |   -   
\-    |   -   | 046-1 |   -   
\-    |   -   |053-1,2|   -   
\-    |   -   | 054-2 |   -   
\-    |   -   |  099* |   -   
\-    |   -   |  014w |   -   
\-    |   -   |  015w |   -   
\-    |   -   |  033w |   -   
\-    |   -   |  047w |   -    
\-    |   -   |   -   |   -    

For *Set 2 016-2* (Bulbmin, Pikmin-like), perhaps integrating it in a function that calls the data of a card whenever another needs it?

For Hermit Crawmad and Goolix-1, maybe they could be able to subscribe on their adjacent lanes/minions to know when they are attacked?