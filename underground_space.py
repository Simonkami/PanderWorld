from gdpc import Editor, Block,geometry
import random

editor = Editor(buffering=True)

def underground_space(x1,y1,z1,x2,y2,z2,block):#y1<y2

    geometry.placeCuboid( #wall
        editor,
        (x1, y1, z1), # Corner 1
        (x2, y2, z1), # Corner 2
        Block("black_wool")
    )
    
    geometry.placeCuboid( #wall
        editor,
        (x1, y1, z2), # Corner 1
        (x2, y2, z2), # Corner 2
        Block("black_wool")
    )
    
    geometry.placeCuboid( #wall
        editor,
        (x1, y1, z1), # Corner 1
        (x1, y2, z2), # Corner 2
        Block("black_wool")
    )
    
    geometry.placeCuboid( #wall
        editor,
        (x2, y1, z1), # Corner 1
        (x2, y2, z2), # Corner 2
        Block("black_wool")
    )
    
    geometry.placeCuboid( #celling
        editor,
        (x1, y2, z1), # Corner 1
        (x2, y2, z2), # Corner 2
        Block("black_wool")
    )

    geometry.placeCuboid( #floor
        editor,
        (x1, y1-1, z1), # Corner 1
        (x2, y1-1, z2), # Corner 2
        block
    )
    
    geometry.placeCuboid( #air
        editor,
        (x1-1, y1, z1-1), # Corner 1
        (x2+1, y2-1, z2+1), # Corner 2
        Block("air")
    )
    
    geometry.placeCuboid( #air
        editor,
        (x1-1, y1, z1-1), # Corner 1
        (x2+1, y2-30, z2+1), # Corner 2
        Block("air")
    )
    
    geometry.placeCuboid( #light
        editor,
        (x1-1, y1, z1-1), # Corner 1
        (x2+1, y1, z2+1), # Corner 2
        Block("light",{"level":"15"})
    )
    
       

    #stars in the sky
    num_lanterns = 150
    if x1 > x2:
        x1, x2 = x2, x1
    if z1 > z2:
        z1, z2 = z2, z1
        
    for _ in range(num_lanterns):
        x = random.randint(x1, x2)
        y = y2  
        z = random.randint(z1, z2)
        editor.placeBlock((x, y, z), Block("sea_lantern"))
        
    #stars on the wall
    
    for _ in range(num_lanterns-90):
        x = x1
        y = random.randint(y2-20, y2)  
        z = random.randint(z1, z2)
        editor.placeBlock((x, y, z), Block("sea_lantern"))
    for _ in range(num_lanterns-90):
        x = x2
        y = random.randint(y2-20, y2)  
        z = random.randint(z1, z2)
        editor.placeBlock((x, y, z), Block("sea_lantern"))
    for _ in range(num_lanterns-90):
        x = random.randint(x1, x2)
        y = random.randint(y2-20, y2)  
        z = z1
        editor.placeBlock((x, y, z), Block("sea_lantern"))
    for _ in range(num_lanterns-90):
        x = random.randint(x1, x2)
        y = random.randint(y2-20, y2)  
        z = z2
        editor.placeBlock((x, y, z), Block("sea_lantern"))
        
