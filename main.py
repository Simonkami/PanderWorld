import random
import sys
import numpy as np

from time import *
from glm import ivec2, ivec3
from interfaceUtils import runCommand

from gdpc import __url__, Editor, Block, geometry
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError
from gdpc.vector_tools import Y, addY, dropY, line3D, circle, fittingCylinder

from Building import house1,house2,house3,small_house,Pavilion,Tower,store,honey_farm
from Building2 import elevator,airship,basement,underground,underground_space,underground_main_enter,panda_statue,road,museum,create_textured_road,pond,fireworks,bamboo
import middle_building

def summon_panda(x,y,z):
    genes = ['normal', 'lazy', 'worried', 'playful', 'aggressive', 'weak', 'brown']
    main_gene= random.choice(genes)
    hidden_gene= random.choice(genes)
    command_panda = f"summon minecraft:panda {x} {y} {z} {{MainGene:{main_gene}, HiddenGene:{hidden_gene}}}"
    runCommand(command_panda)

biome_blocks = {
    "minecraft:plains": Block("grass_block"),
    "minecraft:desert": Block("sandstone"),
    "minecraft:forest": Block("grass_block"),
    "minecraft:savanna_plateau": Block("grass_block"),
    "minecraft:taiga": Block("grass_block"),
    "minecraft:swamp": Block("grass_block"),
    "minecraft:jungle": Block("grass_block"),
    "minecraft:snowy_tundra": Block("snow_block"),
    "minecraft:frozen_river":Block("snow_block"),
    "minecraft:snowy_plains":Block("snow_block"),
    "minecraft:snowy_taiga":Block("snow_block"),
    "minecraft:snowy_beach":Block("snow_block"),
    "minecraft:mushroom_fields": Block("grass_block"),
    "minecraft:mountains": Block("stone"),
}

def sethouse(x,h1,z):
    house_functions=[
        house1.house1,
        house2.house2,
        house3.house3
    ]
    
    house_function = random.choice(house_functions)
    house_function(x+82,h1+1,z-40,"e")
    house_function = random.choice(house_functions)
    house_function(x+81,h1+1,z,"e")
    house_function = random.choice(house_functions)
    house_function(x+80,h1+1,z+35,"e")
    small_house.smallhouse(x+75,h1,z+70,"w")
    
    house_function = random.choice(house_functions)
    house_function(x-82,h1+1,z-40,"w")
    house_function = random.choice(house_functions)
    house_function(x-81,h1+1,z,"w")
    house_function = random.choice(house_functions)
    house_function(x-80,h1+1,z+35,"w")
    small_house.smallhouse(x-75,h1,z+70,"e")
    
    house_function = random.choice(house_functions)
    house_function(x-40,h1+1,z+82,"s")
    house_function = random.choice(house_functions)
    house_function(x,h1+1,z+81,"s")
    house_function = random.choice(house_functions)
    house_function(x+35,h1+1,z+80,"s")
    #small_house.smallhouse(x+70,h1,z+75,"n")
    
    house_function = random.choice(house_functions)
    house_function(x-40,h1+1,z-82,"n")
    house_function = random.choice(house_functions)
    house_function(x,h1+1,z-81,"n")
    house_function = random.choice(house_functions)
    house_function(x+35,h1+1,z-80,"n")
    Pavilion.buildPavilion(x+70,h1,z-75,"n")

    underground.underground(x-95,h1-15,z-95)



def main():
    
    editor = Editor(buffering=True)

    command_time="scoreboard objectives add Timer dummy"
    runCommand(command_time)

    command1="gamerule commandBlockOutput false" #mute all output of command blocks
    command2="gamerule doTileDrops false"
    command3="gamerule doFireTick false"
    runCommand(command1) 
    runCommand(command2)
    runCommand(command3)
    
    try:
        buildArea = editor.getBuildArea()
    except BuildAreaNotSetError:
        print(
            "Error: failed to get the build area!\n"
            "Make sure to set the build area with the /setbuildarea command in-game.\n"
            "For example: /setbuildarea ~0 0 ~0 ~64 200 ~64"
        )
        sys.exit(1)

    print("Loading world slice...")
    buildRect = buildArea.toRect()
    worldSlice = editor.loadWorldSlice(buildRect)

    heightmap = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]  #get worldslice
    meanHeight = np.mean(heightmap)         #meanheight
    groundCenter = addY(buildRect.center, meanHeight)   #center of the BuildArea

    print("World slice loaded!")

    x=groundCenter.x
    y=groundCenter.y
    z=groundCenter.z
    
    #each biome has it's floor block
    biome = worldSlice.getBiomeGlobal((x, y, z))
    print(biome)
    block = biome_blocks.get(biome, Block("grass_block"))
    
    #make sure the enter is always on the ground
    localPos_enter = ivec2(x-80, z+83)
    enter_ground_height = heightmap[x-buildRect.offset[0]-80,z-buildRect.offset[1]+83]
    y=enter_ground_height

    
    h=40            #height of the underground
    h1=y-30-h  #the most deep place in the underground 
    
    #clear_trees_and_leaves(editor, x,y,z)w
    
    
    #underground space
    underground_space.underground_space(x+100,h1,z+100,x-100,h1+h,z-100,block)
    
    command4="kill @e[type=!player]"
    runCommand(command4)
    
    #enter
    airship.airship(x-80, y+100, z+90)
    underground_main_enter.underground_main_enter(x-80,enter_ground_height,z+83,enter_ground_height-h1-13,biome)
    
    #middle_building
    middle_building.middle_building(x,h1,z)

    #house
    sethouse(x,h1,z)
    
    #road
    road.road(x-64,h1,z-64)
    road.road_z(x-60,h1,z+94);road.road_z(x-60,h1,z+85);road.road_z(x-60,h1,z+76);road.road_z(x-60,h1,z+67)

    #panda statue
    panda_statue.panda_statue(x-90,h1,z+72)

    #museum
    
    museum.museum1(x-80,h1-22,z+72)
    
    #sign
    editor.placeBlock((x-64,h1+1,z+87),Block("oak_sign",{"rotation": "0"},data="{front_text: {messages: ['{\"text\": \"Museum\"}', '{\"text\": \"\"}', '{\"text\": \"The history of \"}', '{\"text\": \"PanderWorld\"}']}}"))
    editor.placeBlock((x-64,h1,z+87),Block("oak_sign",{"rotation": "0"},data="{front_text: {messages: ['{\"text\": \"Dive into the well\"}', '{\"text\": \"for our \"}', '{\"text\": \"settlement\"}', '{\"text\": \" history\"}']}}"))
    editor.placeBlock((x-64,h1+1,z+86),Block("oak_sign",{"rotation": "8"},data="{front_text: {messages: ['{\"text\": \"Museum\"}', '{\"text\": \"\"}', '{\"text\": \"The history of \"}', '{\"text\": \"PanderWorld\"}']}}"))
    editor.placeBlock((x-64,h1,z+86),Block("oak_sign",{"rotation": "8"},data="{front_text: {messages: ['{\"text\": \"Dive into the well\"}', '{\"text\": \"for our \"}', '{\"text\": \"settlement\"}', '{\"text\": \" history\"}']}}"))
    editor.placeBlock((x-63,h1,z+99),Block("oak_sign",{"rotation": "12"},data="{front_text: {messages: ['{\"text\": \"B2\"}', '{\"text\": \"\"}', '{\"text\": \"\"}', '{\"text\": \"PanderWorld\"}']}}"))
    editor.placeBlock((x-70,h1,z+78),Block("oak_sign",{"rotation": "12"},data="{front_text: {messages: ['{\"text\": \"Our Heroine\"}', '{\"text\": \"\"}', '{\"text\": \"\"}', '{\"text\": \"ZhuXin\"}']}}"))
    editor.placeBlock((x-59,h1+1,z+99),Block("oak_wall_sign",{"facing":"north"},data="{front_text: {messages: ['{\"text\": \"\"}', '{\"text\": \"B2->B1\"}', '{\"text\": \"\"}', '{\"text\": \"\"}']}}"))
    editor.placeBlock((x-63,h1+57,z+99),Block("oak_wall_sign",{"facing":"north"},data="{front_text: {messages: ['{\"text\": \"\"}', '{\"text\": \"B1->B2\"}', '{\"text\": \"\"}', '{\"text\": \"\"}']}}"))
    editor.placeBlock((x-63,h1-19,z+86),Block("oak_wall_sign",{"facing":"east"},data="{front_text: {messages: ['{\"text\": \"\"}', '{\"text\": \"B3->B2\"}', '{\"text\": \"\"}', '{\"text\": \"\"}']}}"))

    #ruined airship
    localPos_airship1 = ivec2(x-random.randint(0,60), z+random.randint(0,100))
    airship_height1 = heightmap[x-buildRect.offset[0]-random.randint(0,60), z-buildRect.offset[1]+random.randint(0,80)]
    localPos_airship1=addY(localPos_airship1, airship_height1-random.randint(10,25))
    airship.airship(localPos_airship1.x,localPos_airship1.y,localPos_airship1.z)
    
    localPos_airship2 = ivec2(x-random.randint(0,100), z+random.randint(0,60))
    airship_height2 = heightmap[x-buildRect.offset[0]-random.randint(0,80), z-buildRect.offset[1]+random.randint(0,60)]
    localPos_airship2=addY(localPos_airship2, airship_height2-random.randint(10,30))
    airship.airship(localPos_airship2.x,localPos_airship2.y,localPos_airship2.z)
    
    localPos_airship3 = ivec2(x-random.randint(0,60), z+random.randint(80,150))
    airship_height3 = heightmap[x-buildRect.offset[0]-random.randint(0,60), z-buildRect.offset[1]+random.randint(80,150)]
    localPos_airship3=addY(localPos_airship3, airship_height3-random.randint(10,30))
    airship.airship(localPos_airship3.x,localPos_airship3.y,localPos_airship3.z)
    
    localPos_airship4 = ivec2(x-random.randint(80,150), z+random.randint(0,60))
    airship_height4 = heightmap[x-buildRect.offset[0]-random.randint(80,150), z-buildRect.offset[1]+random.randint(0,60)]
    localPos_airship4=addY(localPos_airship4, airship_height4-random.randint(10,30))
    airship.airship(localPos_airship4.x,localPos_airship4.y,localPos_airship4.z)
    
    #summon pandas
    for i in range (1,random.randint(25,30)):
        summon_panda(x+random.randint(-70,70) ,h1+1 ,z+random.randint(-60,60))
    
    #fireworks
    Block_time=Block()
    Block_time.id="repeating_command_block"
    Block_time.data='{Command:"/scoreboard players add @a Timer 1"}'    
    
    Block_timereset=Block()
    Block_timereset.id="repeating_command_block"
    Block_timereset.data='{Command:"/scoreboard players set @a[scores={Timer=300..}] Timer 0"}'
    
    editor.placeBlock((x,h1-10,z+1),Block_time)
    editor.placeBlock((x,h1-10,z+2),Block_timereset)
    editor.placeBlock((x,h1-11,z+1),Block("redstone_block"))
    editor.placeBlock((x,h1-11,z+2),Block("redstone_block")) 
    
    fireworks.fireworks(x+20,h1-8,z-20)
    fireworks.fireworks(x-20,h1-8,z-20)
    fireworks.fireworks(x+20,h1-8,z+20)
    fireworks.fireworks(x-20,h1-8,z+10)
    fireworks.fireworks(x+25,h1-8,z+25)
    fireworks.fireworks(x+21,h1-8,z-23)
    fireworks.fireworks(x+23,h1-8,z-16)
    fireworks.fireworks(x+24,h1-8,z+29)
    fireworks.fireworks(x+17,h1-8,z+26)
    fireworks.fireworks(x+19,h1-8,z-11)
    


    
   
begin_time = time()
main()
end_time = time()
print("run time:", end_time-begin_time)