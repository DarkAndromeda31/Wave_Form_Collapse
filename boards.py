from random import randint

from tile import Tile


class TileMap:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = [[Tile((x, y)) for x in range(width)] for y in range(height)]

    def __getitem__(self, key: int) -> list:
        return self.grid[key]

    def __str__(self) -> str:
        out = ""

        for x in range(self.width):
            line = ""
            for y in range(self.height):
                line += f"{self.grid[y][x]} "

            line += "\n"

            out += line

        return out

    def update_wavefunction(self):
        # TODO: complete update_wavefunction()

        for row in self.grid:
            for tile in row:
                tile.update_candidates()

    def __pick_random_tile(self):
        return (randint(0, self.width - 1), randint(0, self.height - 1))
