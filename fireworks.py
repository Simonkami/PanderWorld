from gdpc import  Editor, Block, geometry
import random
from interfaceUtils import runCommand

editor = Editor(buffering=True)

def fireworks(x,y,z):

    #random color
    r=random.randint(0,16777215)
    g=random.randint(0,16777215)
    b=random.randint(0,16777215)

    t=random.randint(20,40)

    Block1=Block()
    Block1.id="repeating_command_block"
    Block1.data= f'{{Command:"/execute if entity @a[scores={{Timer=299..}}] run summon firework_rocket {x} {y+10} {z} {{LifeTime:{t},FireworksItem:{{id:\\"minecraft:firework_rocket\\",Count:1b,tag:{{Fireworks:{{Flight:1,Explosions:[{{Type:0,Colors:[I;{r},{g},{b}],Flicker:1,Trail:1}}]}}}}}}}}"}}'
    
    editor.placeBlock((x,y,z),Block1)
    
    editor.placeBlock((x,y-1,z),Block("redstone_block"))


