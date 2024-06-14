from gdpc import Editor, Block,geometry

editor = Editor(buffering=True)

def light_r(x,y,z):
    editor.placeBlock((x,y,z),Block("spruce_fence"))
    editor.placeBlock((x,y+1,z),Block("spruce_fence"))
    editor.placeBlock((x,y+2,z),Block("spruce_fence"))
    editor.placeBlock((x,y+3,z),Block("spruce_fence"))
    editor.placeBlock((x,y+4,z),Block("spruce_fence"))
    editor.placeBlock((x,y+5,z),Block("spruce_fence"))
    editor.placeBlock((x,y+5,z-1),Block("spruce_fence"))
    editor.placeBlock((x,y+4,z-1),Block("chain"))
    editor.placeBlock((x,y+3,z-1),Block("lantern"))

def light_l(x,y,z):
    editor.placeBlock((x,y,z),Block("spruce_fence"))
    editor.placeBlock((x,y+1,z),Block("spruce_fence"))
    editor.placeBlock((x,y+2,z),Block("spruce_fence"))
    editor.placeBlock((x,y+3,z),Block("spruce_fence"))
    editor.placeBlock((x,y+4,z),Block("spruce_fence"))
    editor.placeBlock((x,y+5,z),Block("spruce_fence"))
    editor.placeBlock((x,y+5,z+1),Block("spruce_fence"))
    editor.placeBlock((x,y+4,z+1),Block("chain"))
    editor.placeBlock((x,y+3,z+1),Block("lantern"))