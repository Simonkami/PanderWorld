import random
from gdpc import  Editor, Block, geometry

editor = Editor(buffering=True)

def pond(x,y,z):
    
    geometry.placeCuboid(
        editor,
        (x,y-1,z), 
        (x+12,y-2,z+18), 
        Block("water")
        )

    lily_pad = Block("lily_pad")
    corals = [
        Block("brain_coral"), 
        Block("bubble_coral"), 
        Block("fire_coral"), 
        Block("horn_coral"), 
        Block("tube_coral")
    ]

    num_lily_pads = random.randint(10, 18)  
    num_corals = random.randint(10, 18)  

    for _ in range(num_lily_pads):
        lx = random.randint(x, x+12)
        lz = random.randint(z, z+18)
        editor.placeBlock((lx, y, lz), lily_pad)

    for _ in range(num_corals):
        cx = random.randint(x, x+12)
        cz = random.randint(z, z+18)
        coral_type = random.choice(corals)  
        editor.placeBlock((cx, y-2, cz), coral_type)