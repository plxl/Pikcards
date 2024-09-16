from lib.game import *
from time import sleep
import json
import pygame
import time
import sys
from threading import Thread
from copy import deepcopy
from typing import Tuple
import os

# Load all cards from JSON into memory
Card.load_cards()

# Load sample deck
f = open("decks.json")
decks = json.loads(f.read())
f.close()


# sample CLI game with random CPU player (no intelligence)
pname = input("What is your name?\n")
if len(pname.strip()) == 0:
    pname = "bigphish"

print("Select a deck:")
for deck in decks:
    i = decks.index(deck)
    print(f"{i + 1}. {deck["name"]}")
    
deck_selection = input("Select a number or leave blank for random: ")
deck_rand = random.randint(0, len(decks) - 1)
deck = decks[deck_rand]["cards"]
if deck_selection.isnumeric() and int(deck_selection) > 0 and int(deck_selection) <= len(decks):
    deck = decks[int(deck_selection) - 1]["cards"]
    del decks[int(deck_selection) - 1]
else:
    del decks[deck_rand]
        
cpu_deck = decks[random.randint(0, len(decks) - 1)]["cards"]

p1: Player = Player(pname, True)
p1.SetDeck(deck.copy())

p2: Player = Player("CPU", False)
p2.SetDeck(cpu_deck.copy())

p1.Draw(4)

p2.Draw(4)

p1.PrintHand()

# re draw any of the four cards (once only)
redrawn = 0
print(f"You have the option to re-draw any of your initial 4 cards once.")
rsel = "-1"
while redrawn < 4:
    rsel = input(
        "Select a number to re-draw or leave blank to continue with your current hand: "
    )
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
    print("There are no cards left in your deck that can be selected as a 5th...")
    print("Instead, you will simply draw the next card.")

else:

    print("You can pick one more card to join your hand from your deck...")
    print("Choose from the following:")
    available = p1.GetFifths()
    for i in range(len(available)):
        print(f"{i + 1}. {available[i].name}")
        sleep(0.1)

    fsel = "0"
    while True:
        fsel = input(
            "Select an option or leave blank to draw your next card from your deck: "
        )
        if fsel == "":
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
print("Would you prefer to start as the morning player?")
print("1. (Y)es\n2. (N)o\n3. (I) don't care\n")

pref = -1
while pref == -1:
    preference: str = input("Select an option and press enter: ")
    if preference == "1" or preference.lower() == "y":
        pref = 0
    elif preference == "2" or preference.lower() == "n":
        pref = 1
    elif preference == "3" or preference.lower() == "i" or len(preference) == 0:
        pref = 2

p2pref = random.randint(0, 2)
starting_player: int = 0
if p2pref == pref:
    starting_player = random.randint(0, 1)
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
game_loop = Thread(target = game.game_loop)
game_loop.start()

p1.GiveSpecific(deepcopy(next(c for c in Cards if c.name == "Red Pikmin")))


# Initialize Pygame
pygame.init()


# Screen dimensions
card_rw, card_rh = 400, 575
board_rw, board_rh = 2250, 2250
width, height = 800, 800
real_scale: float = width / board_rw
card_w, card_h = round(card_rw * real_scale), round(card_rh * real_scale)
print(f"[LOG] Start card scale: {card_w}, {card_h}")
height += card_h + 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pikcards")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
img_board = pygame.image.load("BoardA.png")
img_board2 = pygame.image.load("BoardA.png")

# Scale images
img_board = pygame.transform.scale(img_board, (800, 800))

# Set up font for text
fnt_16 =  pygame.font.Font("dfcraftsumistdw9.otf", 16)
fnt_32 =  pygame.font.Font("dfcraftsumistdw9.otf", 32)
fnt_48 =  pygame.font.Font("dfcraftsumistdw9.otf", 48)
fnt_72 =  pygame.font.Font("dfcraftsumistdw9.otf", 72)
fnt_96 =  pygame.font.Font("dfcraftsumistdw9.otf", 96)
fnt_128 = pygame.font.Font("dfcraftsumistdw9.otf", 128)

def get_font_that_fits(fonts: list[pygame.font.Font], text: str, max_width: int) -> pygame.font.Font:
    for font in fonts:
        fw, fh = font.size(text)
        if fw <= max_width:
            return font
        
    return fonts[-1]

player_name_labels: list[list] = []

for name in [p1.name, p2.name]:
    font = get_font_that_fits([fnt_96, fnt_72, fnt_48], name, 300)
    txt = font.render(name, True, BLACK)
    rec = txt.get_rect(center=(width // 2, height // 2))
    rec.x = 168
    rec.y = 0 - rec.height
    player_name_labels.append(([txt, rec]))
player_name_labels[1][1].y = 800

def easeInOutQuint(x: float) -> float:
    return 16 * x * x * x * x * x if x < 0.5 else 1 - ((-2 * x + 2) ** 5) / 2

import math

def ease_out_elastic(x: float) -> float:
    c4 = (2 * math.pi) / 3

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1


# Animation parameters
start_time = 0
end_time = 0
start = 0
dest = 0
def animate(func = ease_out_elastic) -> Tuple[bool, float]:
    t = time.time_ns()
    x = (t - start_time) / (end_time - start_time)
    if func is not None:
        x = func(x)
        
    x = start + (dest - start) * x
    
    if t >= end_time:
        return [True, x]
    return [False, x]
        
_x = 0
_y = 0

p2_energy = (76, 54)
p2_time = (560, 60)
p2_health = (728, 56)

p1_energy = (76, 740)
p1_time = (560, 746)
p1_health = (728, 742)

# lanes start at x 10, width 140, 30 pixel sep, 136 from top,
    
p1_name_anim = [False, False]
p2_name_anim = [False, False]
draggable_images: list[DraggableImage] = []

def add_outline_to_image(image: pygame.Surface, thickness: int, color: tuple, color_key: tuple = (255, 0, 255)) -> pygame.Surface:
    mask = pygame.mask.from_surface(image)
    mask_surf = mask.to_surface(setcolor=color)
    mask_surf.set_colorkey((0, 0, 0))

    new_img = pygame.Surface((image.get_width() + 2, image.get_height() + 2))
    new_img.fill(color_key)
    new_img.set_colorkey(color_key)

    for i in -thickness, thickness:
        new_img.blit(mask_surf, (i + thickness, thickness))
        new_img.blit(mask_surf, (thickness, i + thickness))
    new_img.blit(image, (thickness, thickness))

    return new_img

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        for img in draggable_images:
            img.handle_event(event)
            
        # get the most valid mouse_down to handle
        # otherwise multiple cards can be clicked simultaneously which is undesirable
        last_mouse_down: DraggableImage = None
        for img in draggable_images:
            if img.awaiting_mouse_down:
                last_mouse_down = img
                img.awaiting_mouse_down = False
                
        if last_mouse_down is not None:
            last_mouse_down.handle_mouse_down(event.pos)
            
            
    if not p1_name_anim[0]:
        p1_name_anim[0] = True
        start_time = time.time_ns()
        end_time = start_time + 1 * (10**9)
        start = player_name_labels[0][1].y
        dest = 684
    
    if not p1_name_anim[1]:
        p1_name_anim[1], x = animate()
        player_name_labels[0][1].y = x
    
    if not p2_name_anim[0] and p1_name_anim[1]:
        p2_name_anim[0] = True
        start_time = time.time_ns()
        end_time = start_time + 1 * (10**9)
        start = player_name_labels[1][1].y
        dest = 32
        
    if not p2_name_anim[1] and p1_name_anim[1]:
        p2_name_anim[1], x = animate()
        player_name_labels[1][1].y = x
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        _x -= 1
    if keys[pygame.K_RIGHT]:
        _x += 1
    if keys[pygame.K_UP]:
        _y -= 1
    if keys[pygame.K_DOWN]:
        _y += 1
        
    # print(f'{_x}, {_y}')
    
    screen.fill(BLACK)

    # Draw board
    screen.blit(img_board, (0, 0))
    # screen.blit(img_board2, (_x, _y))
    
    txt_p1e = fnt_96.render(str(p1.energy), True, BLACK)
    rec_p1e = txt_p1e.get_rect(center=(width // 2, height // 2))
    rec_p1e.x = p1_energy[0] - rec_p1e.width / 2
    rec_p1e.y = p1_energy[1] - rec_p1e.height / 2
    screen.blit(txt_p1e, rec_p1e)
    
    txt_tme = fnt_32.render("time", True, BLACK)
    txt_tme_ = add_outline_to_image(txt_tme, 2, (255,255,255))
    rec_tme = txt_tme_.get_rect(center=(width // 2, height // 2))
    rec_tme.center = (560, 702)
    screen.blit(txt_tme_, rec_tme)
    
    txt_p1t = fnt_96.render(str(game.time), True, BLACK)
    rec_p1t = txt_p1t.get_rect(center=(width // 2, height // 2))
    rec_p1t.x = p1_time[0] - rec_p1t.width / 2
    rec_p1t.y = p1_time[1] - rec_p1t.height / 2
    screen.blit(txt_p1t, rec_p1t)
    
    txt_p1h = fnt_72.render(str(p1.health), True, BLACK)
    rec_p1h = txt_p1h.get_rect(center=(width // 2, height // 2))
    rec_p1h.x = p1_health[0] - rec_p1h.width / 2
    rec_p1h.y = p1_health[1] - rec_p1h.height / 2
    screen.blit(txt_p1h, rec_p1h)
    
    txt_p2e = fnt_96.render(str(p2.energy), True, BLACK)
    rec_p2e = txt_p2e.get_rect(center=(width // 2, height // 2))
    rec_p2e.x = p2_energy[0] - rec_p2e.width / 2
    rec_p2e.y = p2_energy[1] - rec_p2e.height / 2
    screen.blit(txt_p2e, rec_p2e)
    
    txt_rnd = fnt_32.render("round", True, BLACK)
    txt_rnd_ = add_outline_to_image(txt_rnd, 2, (255,255,255))
    rec_rnd = txt_rnd_.get_rect(center=(width // 2, height // 2))
    rec_rnd.center = (560, 16)
    screen.blit(txt_rnd_, rec_rnd)
    
    txt_p2t = fnt_96.render(str(game.round + 1), True, BLACK)
    rec_p2t = txt_p2t.get_rect(center=(width // 2, height // 2))
    rec_p2t.x = p2_time[0] - rec_p2t.width / 2
    rec_p2t.y = p2_time[1] - rec_p2t.height / 2
    screen.blit(txt_p2t, rec_p2t)
    
    txt_p2h = fnt_72.render(str(p2.health), True, BLACK)
    rec_p2h = txt_p2h.get_rect(center=(width // 2, height // 2))
    rec_p2h.x = p2_health[0] - rec_p2h.width / 2
    rec_p2h.y = p2_health[1] - rec_p2h.height / 2
    screen.blit(txt_p2h, rec_p2h)

    screen.blit(player_name_labels[0][0], player_name_labels[0][1])
    screen.blit(player_name_labels[1][0], player_name_labels[1][1])
    
    fps = str(int(clock.get_fps()))
    fps_t = fnt_16.render(fps, True, (0, 0, 0))
    fps_tt = add_outline_to_image(fps_t, 2, (255,255,255))
    screen.blit(fps_tt, (4, 4))
    
    # draw hand
    for i, card in enumerate(p1.hand):
        # get this card's default position
        # x from 10 to 646 (159 apart when 5 or less cards)
        if len(p1.hand) <= 5: cardx = 10 + i * 159
        else: cardx = 10 + round(i * (636 / (len(p1.hand) - 1)))
        cardy = 810
            
        if type(card.image) == str:
            # load the image
            print(f'[LOG] Converting "{card.image}" into a draggable image')
            image_filename = path.join(getcwd(), "cards", "images", card.image)
            card.image = DraggableImage(image_filename, cardx, cardy, (card_w, card_h))
            draggable_images.append(card.image)
        
        # get the card position centered
        centered = card.image.topleft_to_center((cardx, cardy))
        # if the card's default position needs to be updated, then we need to reset it
        if not card.image.locked and card.image.default_position[0] != centered[0]:
            # update default and target (moves it there)
            card.image.default_position = centered
            card.image.target_pos = card.image.default_position
            # unzoom in case it is zoomed, and reset any conditions
            card.image.zoomed = False
            card.image.mouse_down = False
            card.image.dragging = False
            card.image.prepare_anim()
        
        # update card variables
        card.image.update()
        
        
        # if dragging, draw valid drop slots
        if card.image.dragging:
            valid_lanes = game.GetCardPlayableLanes(p1, card)
            card.image.drop_in_lane = -1
            for l, isvalid in enumerate(valid_lanes):
                if not isvalid: continue
                s = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
                topleft = (
                    10 + l * 159,
                    460
                )
                r = s.get_rect(topleft=topleft)
                r2 = s.get_rect().scale_by(0.8, 0.8)
                opacity = 50
                if r.collidepoint(card.image.mouse_pos[0], card.image.mouse_pos[1]):
                    opacity = 100
                    card.image.drop_in_lane = l
                    def on_drop():
                        game.lanes[card.image.drop_in_lane].minions[0].append(card)
                        # p1.hand.remove(card)
                        if game.morning_player == p1:
                            game.time += card.time
                        else:
                            game.time -= card.time
                        p1.energy -= card.energy
                        card.image.locked = True
                    card.image.on_dropped = on_drop
                    
                
                
                pygame.draw.rect(
                    s,
                    (0, 0, 255, opacity),
                    r2,
                    0,
                    6
                )
                screen.blit(pygame.transform.box_blur(s, 2, False), r)
                
        # draw card to screen
        card.image.draw(screen)
                

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick()
