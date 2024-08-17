from lib.classes import *
from lib.game import *
from beautifultable import BeautifulTable

from os import path, getcwd
import os, subprocess, platform

from pprint import pprint
import json

from time import sleep
from prettytable import PrettyTable


# s = """4 Red Pikmin
# 2 Red Onion
# 4 Yellow Pikmin
# 2 Yellow Onion
# 4 Doodlebugs
# 4 Bulborb Larva
# 4 Burrowing Snagret
# 4 Sovereign Bulblax
# 4 Stellar Orb
# 4 Bulblax Kingdom
# 2 Sagittarius
# 2 Survival Series"""

# cards = []
# for line in s.split('\n'):
#     num = int(line[:1])
#     for i in range(0, num):
#         cards.append(line[2:])

# for c in cards:
#     print(f'"{c}",')

Card.load_cards()

pname = input("What is your name?\n")
# pname = 'bigphish' # just because lazy

SampleDeck = [
    "Red Pikmin",
    "Red Pikmin",
    "Red Pikmin",
    "Red Pikmin",
    "Red Onion",
    "Red Onion",
    "Yellow Pikmin",
    "Yellow Pikmin",
    "Yellow Pikmin",
    "Yellow Pikmin",
    "Yellow Onion",
    "Yellow Onion",
    "Doodlebug",
    "Doodlebug",
    "Doodlebug",
    "Doodlebug",
    "Bulborb Larva",
    "Bulborb Larva",
    "Bulborb Larva",
    "Bulborb Larva",
    "Burrowing Snagret",
    "Burrowing Snagret",
    "Burrowing Snagret",
    "Burrowing Snagret",
    "Sovereign Bulblax",
    "Sovereign Bulblax",
    "Sovereign Bulblax",
    "Sovereign Bulblax",
    "Stellar Orb",
    "Stellar Orb",
    "Stellar Orb",
    "Stellar Orb",
    "Bulblax Kingdom",
    "Bulblax Kingdom",
    "Bulblax Kingdom",
    "Bulblax Kingdom",
    "Sagittarius",
    "Sagittarius",
    "Survival Series",
    "Survival Series"
]

# sample CLI game with random CPU player (no intelligence)
p1: Player = Player(pname, True)
p1.SetDeck(SampleDeck.copy())

p2: Player = Player("CPU", False)
p2.SetDeck(SampleDeck.copy())

p1.Draw(4)
p2.Draw(4)

p1.PrintHand()

# re draw any of the four cards (once only)
redrawn = 0
print(f"You have the option to re-draw any of your initial 4 cards once.")
rsel = '-1'
while redrawn < 4:
    rsel = input("Select a number to re-draw or leave blank to continue with your current hand: ")
    if not rsel.isnumeric():
        break
    
    r = int(rsel) - 1
    if r >= 0 and r < 4 - redrawn:
        # return card randomly into the deck (but not into the top 10 cards as per rules)
        c = p1.hand[r]
        top_deck = p1.deck[:10]
        half_deck = p1.deck[10:]
        half_deck.insert(random.randint(0, len(half_deck) - 1), c)
        p1.deck = top_deck + half_deck
        p1.hand.remove(c)
        p1.Draw(1)
        redrawn += 1
        p1.PrintHand(redrawn)
    else:
        print("Invalid input")
        
# fifth
available = p1.GetFifths()
if len(available) == 0:
    print('There are no cards left in your deck that can be selected as a 5th...')
    print('Instead, you will simply draw the next card.')

else:
    
    print('You can pick one more card to join your hand from your deck...')
    print("Choose from the following:")
    available = p1.GetFifths()
    for i in range(len(available)):
        print(f"{i + 1}. {available[i].name}")
        sleep(0.1)
    
    
    fsel = '0'
    while True:
        fsel = input('Select an option or leave blank to draw your next card from your deck: ')
        if fsel == '':
            p1.Draw(1)
            break
        
        if fsel.isnumeric:
            fsel = int(fsel)
            if fsel <= len(available) and fsel > 0:
                p1.DrawSpecific(available[fsel - 1])
                break
# CPU simply draws its next card for its fifth
p2.Draw(1)

p1.PrintHand()

# Starting player preference deciding
print('Would you prefer to start as the morning player?')
print("1. (Y)es\n2. (N)o\n3. (I) don't care\n")

pref = -1
while pref == -1:
    preference: str = input('Select an option and press enter: ')
    if preference == '1' or preference.lower() == 'y':
        pref = 0
    elif preference == '2' or preference.lower() == 'n':
        pref = 1
    elif preference == '3' or preference.lower() == 'i' or len(preference) == 0:
        pref = 2

p2pref = random.randint(0, 2)
starting_player: int = 0
if p2pref == pref: starting_player = random.randint(0, 1)
elif p2pref == 2:
    starting_player = pref
elif p2pref == 1:
    if pref == 2:
        starting_player = 0
    elif pref == 0:
        starting_player = 1
elif p2pref == 0:
    starting_player = 1 - pref
    
starting_player: Player = p1 if starting_player == 0 else p2

print(f"{p2.name}'s Preference: {p2pref+1}")
print(f"{p1.name}'s Preference: {pref+1}")
sleep(0.8)
print(f"{starting_player.name} will be the Starting Player!")

# Create game object and start the game loop
game = Game([p1, p2], starting_player)
game.game_loop()
exit()

#this is just my pikicards spreadsheet parser which needs work lol
''' TO DO: '''
''' Fix traits (and all lists probably) from only registering the first and last line.
      See Set 1 No 28 Burrowing Snagret traits for example. Should have 3, only has 2.    '''
''' FURTHER: Additions boolean doesnt set to true if there's a negative value (like -X)
      should be somewhat simple fix, remember to do the if + section as well as if '-' sec'''
def fix_list(val) -> list:
    val = str(val)
    if "none" in val.lower():
        return []
    
    if "  " in val:
        sl = [0]
        spaces = 0
        index = 0
        for c in val:
            if c == ' ':
                spaces += 1
                if spaces == 2:
                    sl.append(index - 1 - sl[-1])
            else:
                if spaces >= 2:
                    sl.append(index)
                
                spaces = 0
            
            index += 1
            
        sl.append(index)
        
        lst = []
        for i in range(0, int(len(sl) / 2)):
            lst.append(val[sl[i*2]:sl[i*2+1]])
        out = []
        for i in lst:
            if i.strip():
                out.append(i)
                
        return out
    
    return [x.strip() for x in val.split('\n')]

def fix_integer(val) -> list:
    val = str(val).lower().strip()
    if '-' in val or '?' in val:
        return [0, False]
    
    if val == 'x':
        return [0, True]
    
    if '+' in val:
        if val[0] == '+':
            return [0, True]
        return [int(val.split('+')[0]), True]
    
    return [int(val), False]
    
def parse_allcards_tsv():
    f = open('allcards.tsv', 'r')
    data = f.read()
    f.close()
    lines = data.split('\n')
    for i in range(8, len(lines)):
        if i == 12:
            continue
        values = lines[i].split('\t')
        card = Card(
            str(values[0]), # set
            int(str(values[1]).split(',')[0]), # number
            True if 'yes' in str(values[2]).lower() else False, # fifth
            Rarity[str(values[3]).title()].value, # rarity
            str(values[4]), # name
            "", # image
            Class[str(values[5]).upper()].value, # class
            Type[str(values[6]).title()].value, # type
            0,
            0,
            0,
            0,
            [False, False, False, False],
            fix_list(values[11]), # elements
            fix_list(values[12]), # immunities
            fix_list(values[13]), # weaknesses
            fix_list(values[14]) + fix_list(values[15]), # traits and special traits
            fix_list(values[16]), # abilities
            '' if 'none' in str(values[17]).lower() else fix_list(values[17])[-1] # notes
        )
        card.energy, card.additions[0] = fix_integer(values[7])
        card.time, card.additions[1] = fix_integer(values[8])
        card.attack, card.additions[2] = fix_integer(values[9])
        card.health, card.additions[3] = fix_integer(values[10])
        
        filename = card.name
        if card.set == '1' or card.set.lower() == 'c':
            filename = f"{str(card.number).zfill(2)}_{card.name.replace(' ', '_')}"
        elif card.set == '2':
            filename = f"{str(card.number).zfill(3)}_{card.name.replace(' ', '_')}"
        elif card.set == '0':
            filename = f"{card.name.replace(' ', '_')}"
            
        filename = filename.replace('?', '')
        card.image = filename + '.png'
        
        f = open(f'cards\\json\\{card.set}_{filename}.json', 'w')
        f.write(card.toJSON())
        f.close()
        print(f"{i+1}: Written JSON")