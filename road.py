from gdpc import Editor, Block, editor,geometry
from Building2 import light

editor = Editor(buffering=True)

def road_x(x,y,z):
    light.light_r(x,y,z+2)
    light.light_l(x,y,z-2)
    
    geometry.placeCuboid( 
        editor,
        (x-4,y-1,z-1), 
        (x+4,y-1,z+1), 
        Block("dirt_path")
    )

def road_z(x,y,z):
    light.light_r(x+2,y,z)
    light.light_l(x-2,y,z)
    
    geometry.placeCuboid( 
        editor,
        (x-1,y-1,z-4), 
        (x+1,y-1,z+4), 
        Block("dirt_path")
    )

def road(x,y,z):
    for i in range (0,13):
        road_x(x+9*i,y,z)
        road_x(x+9*i,y,z+119)
        road_z(x,y,z+9*i)
        road_z(x+119,y,z+9*i)
    