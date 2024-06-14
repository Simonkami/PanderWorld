import random
from Building2 import elevator,airship,basement,underground,underground_space,underground_main_enter,panda_statue,road,museum,create_textured_road,pond,bamboo
from gdpc import __url__, Editor, Block, geometry
from Building import house1,house2,house3,small_house,Pavilion,blacksmith,Tower,store,honey_farm,well

def middle_building(x,h1,z):
    #tower
    Tower.buildTower(x,h1,z,3)

    #pond
    pond.pond(x+10,h1,z+10)
    pond.pond(x-23,h1,z+10)
    pond.pond(x+10,h1,z-26)
    pond.pond(x-23,h1,z-26)
    
    #road
    create_textured_road.create_textured_road(x+10,h1-1,z-2,40,5,"x")
    create_textured_road.create_textured_road(x-60,h1-1,z-2,50,5,"x")
    create_textured_road.create_textured_road(x-2,h1-1,z+10,40,5,"z")
    create_textured_road.create_textured_road(x-2,h1-1,z-60,50,5,"z")
    
    #honey_farm
    honey_farm.honey_farm(x+20,h1,z-50,"n")
    honey_farm.honey_farm(x+20,h1,z+42,"n")

    #black_smith
    blacksmith.blacksmith_main(x-48,h1,z+48,"n")
    blacksmith.blacksmith_main(x+44,h1,z+44,"e")
    blacksmith.blacksmith_main(x-48,h1,z-50,"w")
    blacksmith.blacksmith_main(x+42,h1,z-50,"s")
    
    #store
    store.store1(x-25,h1,z-42,"n")
    store.store2(x-25,h1,z+35,"s")
    
    #bamboo
    bamboo.bamboo(x-random.randint(4,8),h1-1,z-random.randint(11,17))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z-random.randint(11,17))
    bamboo.bamboo(x-random.randint(4,8),h1-1,z+random.randint(11,17))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z+random.randint(11,17))
    
    bamboo.bamboo(x-random.randint(4,8),h1-1,z-random.randint(18,24))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z-random.randint(18,24))
    bamboo.bamboo(x-random.randint(4,8),h1-1,z+random.randint(18,24))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z+random.randint(18,24))
    
    bamboo.bamboo(x-random.randint(4,8),h1-1,z-random.randint(25,29))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z-random.randint(25,29))
    bamboo.bamboo(x-random.randint(4,8),h1-1,z+random.randint(25,29))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z+random.randint(25,29))
    
    bamboo.bamboo(x-random.randint(4,8),h1-1,z-random.randint(30,33))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z-random.randint(30,33))
    bamboo.bamboo(x-random.randint(4,8),h1-1,z+random.randint(30,33))
    bamboo.bamboo(x+random.randint(4,8),h1-1,z+random.randint(30,33))
    
    bamboo.bamboo(x-random.randint(11,16),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(11,16),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(11,16),h1-1,z-random.randint(4,8))
    bamboo.bamboo(x-random.randint(11,16),h1-1,z-random.randint(4,8))
    
    bamboo.bamboo(x-random.randint(17,24),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(17,24),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(17,24),h1-1,z-random.randint(4,8))
    bamboo.bamboo(x-random.randint(17,24),h1-1,z-random.randint(4,8))
    
    bamboo.bamboo(x-random.randint(17,24),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(17,24),h1-1,z+random.randint(4,8))
    bamboo.bamboo(x+random.randint(17,24),h1-1,z-random.randint(4,8))
    bamboo.bamboo(x-random.randint(17,24),h1-1,z-random.randint(4,8))
    
    #well
    well.Wells(x-55,h1,z+22)
    well.Wells(x+48,h1,z-15)