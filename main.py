from boards import TileMap
from sprites import SpriteSheet

sheet = SpriteSheet("./resources/sprites.json", "./resources/WaveFunctionTiles.png")

world_map = TileMap(sheet, 10, 10)


for i in range(len(sheet.sprite_library)):
        world_map.grid[i // 10][i % 10].set_sprite(sheet.sprite_library[i])

print(world_map)

world_map.render_map()
