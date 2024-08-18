

s = """
Paper Bag
Paper Bag
Paper Bag
Paper Bag
Fire Geyser
Fire Geyser
Fire Geyser
Fire Geyser
Iridescent Glint Beetle
Iridescent Glint Beetle
Blast Wall
Blast Wall
Blast Wall
Blast Wall
Covering Mold
Covering Mold
Covering Mold
Covering Mold
Armored Cannon Beetle
Armored Cannon Beetle
Armored Cannon Beetle
Gatling Groink
Gatling Groink
Gatling Groink
Mamuta
Mamuta
Mamuta
Mamuta
Toady Bloyster
Toady Bloyster
Toady Bloyster
Toady Bloyster
Ranging Bloyster
Ranging Bloyster
Ranging Bloyster
Ranging Bloyster
Snow Bulborb
Snow Bulborb
Snow Bulborb
Snow Bulborb
"""

for line in s.split("\n"):
    if len(line.strip()) == 0:
        continue
    
    print(f'"{line}",')