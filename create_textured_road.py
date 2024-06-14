import random
from gdpc import geometry, Block, Editor

editor = Editor()

def create_textured_road(start_x, start_y, start_z, length, width, direction='z'):
    stone_types = [
        Block("stone"),
        Block("cobblestone"),
        Block("stone_bricks"),
        Block("mossy_cobblestone"),
        Block("andesite")
    ]
    
    if direction == 'z':
        end_x = start_x + width - 1
        end_z = start_z + length - 1
    elif direction == 'x':
        end_x = start_x + length - 1
        end_z = start_z + width - 1
    else:
        raise ValueError("Direction must be 'x' or 'z'")

    
    for x in range(start_x, end_x + 1):
        for z in range(start_z, end_z + 1):
            
            road_material = random.choice(stone_types)
            editor.placeBlock((x, start_y, z), road_material)


