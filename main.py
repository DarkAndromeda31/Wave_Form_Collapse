from boards import TileMap
from sprites import SpriteSheet


sheet = SpriteSheet("./resources/sprites.json", "./resources/WaveFunctionTiles.png")

world_map = TileMap(sheet, 50, 50)

world_map.grid[14][14].set_sprite(sheet.sprite_library[1])
# world_map.grid[14][28].set_sprite(sheet.sprite_library[1])

try:
    world_map.collapse_wavefunction()
except Exception as e:
    world_map.render_map()
    raise e

print(world_map)

world_map.render_map()
