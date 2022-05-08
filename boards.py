from tile import Tile


class TileMap:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = [[Tile() for _ in range(width)] for _ in range(height)]

    def __str__(self) -> str:
        out = ""

        for x in range(self.width):
            line = ""
            for y in range(self.height):
                line += f"{self.grid[y][x]} "

            line += "\n"

            out += line

        return out

