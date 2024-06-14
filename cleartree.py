from gdpc import __url__, Editor, Block, geometry

def clear_trees_and_leaves(editor,x,y,z):
    log_types = ["minecraft:oak_log", "minecraft:spruce_log", "minecraft:birch_log", "minecraft:jungle_log", "minecraft:acacia_log", "minecraft:dark_oak_log"]
    leaf_types = ["minecraft:oak_leaves", "minecraft:spruce_leaves", "minecraft:birch_leaves", "minecraft:jungle_leaves", "minecraft:acacia_leaves", "minecraft:dark_oak_leaves"]

    x1=x;y1=y;z1=z;

    for x in range(x-30, x):
        y=y1
        for y in range(y-8, y+8):
            z=z1
            for z in range(z+60, z+83):
                block = editor.getBlock((x, y, z))
                if block.id in log_types or block.id in leaf_types:
                    editor.placeBlock((x, y, z), Block("air"))