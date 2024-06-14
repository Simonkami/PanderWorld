from gdpc import __url__, Editor, Block, geometry
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError
import time
from interfaceUtils import runCommand

from glm import floor

from Building2 import elevator,airship,basement,underground,underground_space,underground_enter,underground_stairs

editor = Editor(buffering=True)

biome_blocks = {
    "minecraft:plains": Block("grass_block"),
    "minecraft:desert": Block("sandstone"),
    "minecraft:forest": Block("grass_block"),
    "minecraft:savanna_plateau": Block("grass_block"),
    "minecraft:taiga": Block("grass_block"),
    "minecraft:swamp": Block("grass_block"),
    "minecraft:jungle": Block("grass_block"),
    "minecraft:snowy_tundra": Block("snow_block"),
    "minecraft:mushroom_fields": Block("grass_block"),
    "minecraft:mountains": Block("stone")
}

def underground_main_enter(x,y,z,h,biome):
	
	underground_enter.underground_enter(x,y-2,z,biome)
	underground_stairs.underground_stairs(x,y-16,z)
	

	
	elevator.elevator(x+17,y-h-16,z+21,h+1)
	
	
	editor.placeBlock((x+21,y-15,z+16),Block("spruce_planks"))
	editor.placeBlock((x+20,y-15,z+16),Block("spruce_planks"))
	editor.placeBlock((x+19,y-15,z+16),Block("spruce_planks"))
	editor.placeBlock((x+18,y-15,z+16),Block("spruce_planks"))
	editor.placeBlock((x+17,y-15,z+16),Block("spruce_planks"))
	
	x1=x;y1=y;z1=z;
	for x in range (x,x+29):
		y=y1
		for y in range (y-4,y):
			z=z1
			for z in range (z,z+31):
				if biome=="minecraft:desert":
					editor.placeBlock((x, y-1, z), Block("minecraft:sandstone"))    
				elif biome=="minecraft:snowy_tundra":
					editor.placeBlock((x, y-1, z), Block("minecraft:snow_block"))                   
				elif biome=="minecraft:frozen_river":
					editor.placeBlock((x, y-1, z), Block("minecraft:snow_block"))    
				elif biome=="minecraft:snowy_plains":
					editor.placeBlock((x, y-1, z), Block("minecraft:snow_block"))  
				elif biome=="minecraft:snowy_taiga":
					editor.placeBlock((x, y-1, z), Block("minecraft:snow_block"))  
				elif biome=="minecraft:snowy_beach":
					editor.placeBlock((x, y-1, z), Block("minecraft:snow_block"))
				elif biome=="minecraft:mountains":
					editor.placeBlock((x, y-1, z), Block("minecraft:stone"))
	
	"""
	x1=x;y1=y;z1=z;
	for x in range(x+12, x+19):
		y=y1
		for y in range(y+3-2, y+5):
			z=z1
			for z in range(z+17, z+18):
				block = editor.getBlock((x, y, z))
				if biome == "minecraft:desert" and block.id == "minecraft:spruce_stairs":
					editor.placeBlock((x, y, z), Block("minecraft:sandstone_stairs[facing=north,half=top,shape=straight,waterlogged=false]"))
				elif biome == "minecraft:mountains" and block.id == "minecraft:spruce_stairs":
					editor.placeBlock((x, y, z), Block("minecraft:stone_stairs[facing=north,half=top,shape=straight,waterlogged=false]"))
					
	

	#editor.placeBlock((x+19,y-h-13,z+17),Block("minecraft:stone_button[face=floor,facing=north,powered=true]"))
	#editor.placeBlock((x+20,y-h-15,z+17),Block("air"))
	"""

	


