from tile import Tile


class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Tile()] * width] * height

    def __str__(self):
        out = ""

        for x in range(self.width):
            line = ""
            for y in range(self.height):
                line += f"{self.grid[y][x]} "

            line += "\n"

            out += line

        return out

