from lib.game import *

"""
    Parses the spreadsheet's exported TSV file into the Card.JSON files.

    This is a TEMPORARY FILE and will likely be gone once we have parsed everything perfectly.
    
    TO DO:
    Fix traits (and all lists probably) from only registering the first and last line.
      See Set 1 No 28 Burrowing Snagret traits for example. Should have 3, only has 2.
    FURTHER: Additions boolean doesnt set to true if there's a negative value (like -X)
      should be somewhat simple fix, remember to do the if + section as well as if '-' sec
"""

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
            str(values[0]),  # set
            int(str(values[1]).split(',')[0]),  # number
            True if 'yes' in str(values[2]).lower() else False,  # fifth
            Rarity[str(values[3]).title()].value,  # rarity
            str(values[4]),  # name
            "",  # image
            Class[str(values[5]).upper()].value,  # class
            Type[str(values[6]).title()].value,  # type
            0,
            0,
            0,
            0,
            [False, False, False, False],
            fix_list(values[11]),  # elements
            fix_list(values[12]),  # immunities
            fix_list(values[13]),  # weaknesses
            # traits and special traits
            fix_list(values[14]) + fix_list(values[15]),
            fix_list(values[16]),  # abilities
            '' if 'none' in str(values[17]).lower(
            ) else fix_list(values[17])[-1]  # notes
        )
        card.energy, card.additions[0] = fix_integer(values[7])
        card.time, card.additions[1] = fix_integer(values[8])
        card.attack, card.additions[2] = fix_integer(values[9])
        card.health, card.additions[3] = fix_integer(values[10])

        filename = card.name
        if card.set == '1' or card.set.lower() == 'c':
            filename = f"{str(card.number).zfill(2)}_{
                card.name.replace(' ', '_')}"
        elif card.set == '2':
            filename = f"{str(card.number).zfill(3)}_{
                card.name.replace(' ', '_')}"
        elif card.set == '0':
            filename = f"{card.name.replace(' ', '_')}"

        filename = filename.replace('?', '')
        card.image = filename + '.png'

        f = open(f'cards\\json\\{card.set}_{filename}.json', 'w')
        f.write(card.toJSON())
        f.close()
        print(f"{i+1}: Written JSON")
