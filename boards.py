# import logging
import random
from random import randint
from PIL import Image

from tile import Tile
from sprites import SpriteSheet


# logging.basicConfig(level=logging.DEBUG)


class TileMap:
    def __init__(self, sprite_sheet: SpriteSheet, width: int, height: int) -> None:
        self.sprite_sheet = sprite_sheet
        self.width = width
        self.height = height
        self.grid = [[Tile(sprite_sheet, (x, y)) for x in range(width)] for y in range(height)]

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

    def update_wavefunction(self) -> int:
        # Update all tiles
        total_entropy = 0
        for row in self.grid:
            for tile in row:
                total_entropy += tile.update_candidates(self.grid)
        # logging.info(f"total entropy = {total_entropy}")

        return total_entropy

    def collapse_wavefunction(self) -> None:
        MAX_ENTROPY = self.width * self.height * len(self.sprite_sheet.sprite_library)
        MAX_TILE_ENTROPY = len(self.sprite_sheet.sprite_library)

        total_entropy = MAX_ENTROPY
        chosen_tile = None
        while total_entropy > 0:
            # Pick tile to set
            for e_level in range(2, MAX_TILE_ENTROPY + 2):
                candidates = []
                for row in self.grid:
                    for tile in row:
                        if tile.entropy == e_level:
                            candidates.append(tile)

                if len(candidates) > 0:
                    chosen_tile = random.choice(candidates)
                    break

            if chosen_tile == None:
                # logging.info("No possibilities, exiting")
                return

            chosen_tile.set_sprite(
                random.choices(chosen_tile.candidates, [sprite.weight for sprite in chosen_tile.candidates])[0])

            # logging.info(f"tile {chosen_tile.coords} set to {chosen_tile.sprite.name}")

            total_entropy = self.update_wavefunction()
