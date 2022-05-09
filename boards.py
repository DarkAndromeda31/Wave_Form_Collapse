from random import randint
from PIL import Image

from tile import Tile
from sprites import SpriteSheet


class TileMap:
    def __init__(self, sprite_sheet: SpriteSheet, width: int, height: int) -> None:
        self.sprite_sheet = sprite_sheet
        self.width = width
        self.height = height
        self.grid = [[Tile((x, y)) for x in range(width)] for y in range(height)]

    def __getitem__(self, key: int) -> list:
        return self.grid[key]

    def __str__(self) -> str:
        out = "╔" + "═" * self.width + "╗\n"

        for y in range(self.height):
            line = "║"
            for x in range(self.width):
                line += f"{self.grid[y][x]}"

            line += "║\n"

            out += line

        out += "╚" + "═" * self.width + "╝\n"

        return out

    def render_map(self):
        map_image = Image.new("RGB", (self.width * 16, self.height * 16), color="black")

        for x in range(self.width):
            for y in range(self.height):
                tile = self.grid[y][x]
                stamp = self.sprite_sheet.image_bank[tile.sprite.loc[1]][tile.sprite.loc[0]]
                paste_location = (x * 16, y * 16, (x + 1) * 16, (y + 1) * 16)

                map_image.paste(stamp, paste_location)

            map_image.save("./out/map.png")

    def update_wavefunction(self):
        # TODO: complete update_wavefunction()

        for row in self.grid:
            for tile in row:
                tile.update_candidates()

    def __pick_random_tile(self):
        return (randint(0, self.width - 1), randint(0, self.height - 1))
