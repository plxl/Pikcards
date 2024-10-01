import os
import json
import re


from lib.cardclasses.bases import area, card, exploration, item, minion, modifiers

class OldCard:
    def __init__(self, dic={}, **kwargs) -> None:
        self.set: str = "0"
        self.number: int = 0
        self.fifth: bool = True
        self.rarity: int = 0
        self.name: str = "CARD"
        self.image: str = "IMAGE.png"
        self.cardclass: int = 0
        self.cardtype: int = 0
        self.base_energy: int = 0
        self.base_time: int = 0
        self.base_attack: int = 0
        self.base_health: int = 0
        self.defense: int = 0
        self.maxcarry: int = 0
        self.additions: list = []
        self.elements: list = []
        self.immunities: list = []
        self.weaknesses: list = []
        self.traits: list = []
        self.abilities: list = []
        self.notes: str = "NOTES"
        
        self.__dict__.update(dic)
        self.__dict__.update(kwargs)
        

files = [open(f"./cards/json/{f}") for f in os.listdir("./cards/json")]

cards: list[object] = [json.loads(f.read()) for f in files]

for f in files: f.close()

for c in cards:
    c: OldCard = OldCard(c)
    
    card_name = "".join(re.findall(r"[a-zA-Z0-9]+", c.name))
    if card_name[0].isnumeric():
        card_name = "_" + card_name
    
    card_type = "UNK"
    if c.cardtype == 0: card_type = "Minion"
    elif c.cardtype == 1: card_type = "Item"
    elif c.cardtype == 2: card_type = "Area"
    elif c.cardtype == 3: card_type = "Exploration"
    else: raise Exception(f"Card / Class Type not valid: {c.cardtype}")
    
    card_class = c.cardclass + 1
    load_function = f"""
{card_name}(
        set = "{c.set}", # str
        number = {c.number}, # int
        fifth = {c.fifth}, # bool
        rarity = {c.rarity}, # int
        name = "{c.name}", # str
        image = "{c.image}", # str
        cardclass = {card_class}, # int
        base_energy = {c.base_energy}, # int
        base_time = {c.base_time}, # int
        elements = {str([f'"{e}"' for e in c.elements])}, # list[str]
        immunities = {str([f'"{e}"' for e in c.immunities])}, # list[str]
        traits = {str([f'"{e}"' for e in c.traits])}, # list[str]
""".strip()


    if card_type == "Minion": load_function += f"""
        base_attack = {c.base_attack}, # int
        base_health = {c.base_health}, # int
        defense = {c.defense}, # int
        maxcarry = {c.maxcarry}, # int
    """.rstrip()
    
    elif card_type == "Area": load_function += """
        description = "Description", # str
    """.rstrip()
    
    if card_type == "Exploration": load_function += """
        description = "Description", # str
    """.rstrip()
    
    if len(c.weaknesses) > 0: load_function += f"""
        weakness_descriptions = {
            str([w for w in c.weaknesses])
        }, # list[str](optional)
    """.rstrip()
    else: load_function += """
        weakness_descriptions = [], # list[str](optional)
    """.rstrip()
    
    if len(c.abilities) > 0: load_function += f"""
        ability_descriptions = {
            str([a for a in c.abilities])
        } # list[str](optional)
    """.rstrip()
    else: load_function += """
        ability_descriptions = [] # list[str](optional)
    """.rstrip()
        
    load_function += "\n    )"
    
    py = f"""
from ..bases.{card_type.lower()} import *

class {card_name}({card_type}):
    pass


def load_me():
    this_{card_type.lower()} = {load_function}
    
    return this_{card_type.lower()}
    
""".strip()
    
    f = open(f"./lib/cardclasses/cards/{card_name}.py", 'w')
    f.write(py)
    f.close()
