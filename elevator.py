
from gdpc.interface import placeBlocks
from glm import ivec2, ivec3
from interfaceUtils import runCommand

from gdpc import __url__, Editor, Block, geometry
from gdpc.vector_tools import Y, addY, dropY, line3D, circle, fittingCylinder

editor = Editor(buffering=True)

def elevator_start(x,y,z):
    
    geometry.placeCuboid( #place smooth_quartz
        editor,
        (x,y,z), # Corner 1
        (x+4,y+2,z-5), # Corner 2
        Block("smooth_quartz")
    )
    
    editor.placeBlock((x+2,y,z-2),Block("note_block"))
    
    editor.placeBlock((x+2,y+1,z-2),Block("observer",{"facing": "down"}))
    editor.placeBlock((x+2,y+1,z-3),Block("redstone_wire",{"north": "side"}))
    editor.placeBlock((x+2,y+1,z-4),Block("redstone_wire",{"north": "side"}))
    
    editor.placeBlock((x+2,y+2,z-2),Block("slime_block"))
    editor.placeBlock((x+1,y+2,z-2),Block("sticky_piston",{"facing": "up"}))
    editor.placeBlock((x+3,y+2,z-2),Block("sticky_piston",{"facing": "up"}))
                                          
    editor.placeBlock((x+2,y+3,z-2),Block("sticky_piston",{"facing": "down"}))
    editor.placeBlock((x+1,y+3,z-2),Block("slime_block"))
    editor.placeBlock((x+3,y+3,z-2),Block("slime_block"))
    editor.placeBlock((x+1,y+3,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+1,y+3,z-1),Block("smooth_quartz"))
    editor.placeBlock((x+3,y+3,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+3,y+3,z-1),Block("smooth_quartz"))
    editor.placeBlock((x+2,y+3,z-4),Block("stone_button",{"face": "floor"}))
    

    editor.placeBlock((x+1,y+4,z-2),Block("slime_block"))
    editor.placeBlock((x+3,y+4,z-2),Block("slime_block"))
    editor.placeBlock((x+2,y+4,z-2),Block("observer",{"facing": "up"}))
    editor.placeBlock((x+1,y+4,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+1,y+4,z-1),Block("smooth_quartz"))
    editor.placeBlock((x+3,y+4,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+3,y+4,z-1),Block("smooth_quartz"))
    
    
    editor.placeBlock((x+1,y+5,z-2),Block("shroomlight"))
    editor.placeBlock((x+3,y+5,z-2),Block("shroomlight"))


def elevator_end(x,y,z,h):
    editor.placeBlock((x,y+h,z),Block("smooth_stone"))
    editor.placeBlock((x+1,y+h,z),Block("smooth_stone"))
    editor.placeBlock((x+2,y+h,z),Block("smooth_stone"))
    editor.placeBlock((x+3,y+h,z),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h,z),Block("smooth_stone"))
    editor.placeBlock((x,y+h,z-1),Block("smooth_stone"))
    editor.placeBlock((x,y+h,z-3),Block("smooth_stone"))
    editor.placeBlock((x,y+h,z-4),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h,z-1),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h,z-3),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h,z-4),Block("smooth_stone"))
    editor.placeBlock((x+1,y+h,z-4),Block("smooth_stone"))
    editor.placeBlock((x+2,y+h,z-4),Block("smooth_stone"))
    editor.placeBlock((x+3,y+h,z-4),Block("smooth_stone"))
    editor.placeBlock((x,y+h,z-2),Block("obsidian"))
    editor.placeBlock((x+4,y+h,z-2),Block("obsidian"))

    editor.placeBlock((x+2,y+h+3,z-2),Block("note_block"))
    editor.placeBlock((x+3,y+h+3,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+2,y+h+3,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+1,y+h+3,z-3),Block("smooth_quartz"))
    editor.placeBlock((x+2,y+h+3,z-4),Block("stone_button",{"face": "wall"}))

    editor.placeBlock((x+2,y+h+4,z-2),Block("obsidian"))
    editor.placeBlock((x,y+h+4,z),Block("smooth_stone"))
    editor.placeBlock((x+1,y+h+4,z),Block("smooth_stone"))
    editor.placeBlock((x+2,y+h+4,z),Block("smooth_stone"))
    editor.placeBlock((x+3,y+h+4,z),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h+4,z),Block("smooth_stone"))
    editor.placeBlock((x,y+h+4,z-1),Block("smooth_stone"))
    editor.placeBlock((x,y+h+4,z-3),Block("smooth_stone"))
    editor.placeBlock((x,y+h+4,z-4),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h+4,z-1),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h+4,z-3),Block("smooth_stone"))
    editor.placeBlock((x+4,y+h+4,z-4),Block("smooth_stone"))
    editor.placeBlock((x+1,y+h+4,z-4),Block("smooth_stone"))
    editor.placeBlock((x+2,y+h+4,z-4),Block("smooth_stone"))
    editor.placeBlock((x+3,y+h+4,z-4),Block("smooth_stone"))
    editor.placeBlock((x,y+h+4,z-2),Block("obsidian"))
    editor.placeBlock((x+4,y+h+4,z-2),Block("obsidian"))

def elevator_wall(x,y,z,h):
    #��
    geometry.placeCuboid(
    editor,
    (x,y,z), 
    (x,y+h+3,z), 
    Block("smooth_stone")
    )
    
    geometry.placeCuboid(
    editor,
    (x,y,z-4), 
    (x,y+h+3,z-4), 
    Block("smooth_stone")
    )
    
    geometry.placeCuboid(
    editor,
    (x+4,y,z-4), 
    (x+4,y+h+3,z-4), 
    Block("smooth_stone")
    )
    
    geometry.placeCuboid(
    editor,
    (x+4,y,z), 
    (x+4,y+h+3,z), 
    Block("smooth_stone")
    )
    #glass wall
    
    geometry.placeCuboid(
    editor,
    (x+1,y+4,z), 
    (x+3,y+h+3,z), 
    Block("glass_pane")
    )
    
    geometry.placeCuboid(
    editor,
    (x+1,y+4,z-4), 
    (x+3,y+h,z-4), 
    Block("glass_pane")
    )
    
    editor.placeBlock((x+2,y+5,z-4),Block("air"))
    editor.placeBlock((x+2,y+4,z-4),Block("air"))

def place_air(x,y,z,h):
    geometry.placeCuboid( #place air
        editor,
        (x,y,z), # Corner 1
        (x+4,y+h+4,z-5), # Corner 2
        Block("air")
    )


def elevator(x,y,z,h): #h is height of the elevator
    place_air(x,y,z,h)
    elevator_start(x,y,z)
    elevator_wall(x,y,z,h)
    elevator_end(x,y,z,h)
    #command_block for moving elevator
    Block_1=Block()
    Block_1.id="command_block"
    Block_1.data=f'{{Command:"setblock {x+2} {y} {z-2} minecraft:note_block destroy"}}'
    
    editor.placeBlock((x+2,y+h+4,z-3),Block_1)
    
    Block_2=Block()
    Block_2.id="command_block"
    Block_2.data=f'{{Command:"setblock {x+2} {y+h+3} {z-2} minecraft:note_block destroy"}}'
    editor.placeBlock((x+2,y,z-4),Block_2)
                                                              