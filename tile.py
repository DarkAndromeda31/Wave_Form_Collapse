# import logging

from sprites import Sprite, SpriteSheet

# logging.basicConfig(level=logging.INFO)


class Tile:
    def __init__(self, spritesheet: SpriteSheet, coordinates: tuple, s: Sprite = None) -> None:
        self.coords = coordinates
        self.candidates = spritesheet.sprite_library.copy()

        if s is None:
            self.sprite = Sprite("Null", "#", (0, 0), "none",
                                 {"top": ["none"], "bottom": ["none"], "left": ["none"], "right": ["none"]}, 0)
        else:
            self.set_sprite(s)

        self.entropy = len(self.candidates)

    def __str__(self) -> str:
        return self.sprite.short_name

    def set_sprite(self, s: Sprite) -> None:
        self.sprite = s
        self.candidates = []
        self.entropy = 0

    def update_candidates(self, grid: list) -> int:
        if len(self.candidates) == 0:
            # logging.debug(f"{self.coords} has 0 candidates, exiting")
            return 0

        # logging.debug(str(self.coords) + " " + str([s.name for s in self.candidates]))

        x = self.coords[0]
        y = self.coords[1]

        if y > 0:
            top_edge = grid[y - 1][x].sprite.connects["bottom"]
        else:
            top_edge = ["none"]

        if y < len(grid) - 1:
            bottom_edge = grid[y + 1][x].sprite.connects["top"]
        else:
            bottom_edge = ["none"]

        if x > 0:
            left_edge = grid[y][x - 1].sprite.connects["right"]
        else:
            left_edge = ["none"]

        if x < len(grid[0]) - 1:
            right_edge = grid[y][x + 1].sprite.connects["left"]
        else:
            right_edge = ["none"]

        # logging.debug(f"t {top_edge} b {bottom_edge} l {left_edge} r {right_edge}")

        for sprite in self.candidates.copy():
            valid = True
            if top_edge != ["none"] and any(edge not in sprite.connects["top"] for edge in top_edge):
                # logging.debug(f"{self.coords} {sprite.name} removed, top invalid ({top_edge})")
                valid = False
            elif bottom_edge != ["none"] and any(edge not in sprite.connects["bottom"] for edge in bottom_edge):
                # logging.debug(f"{self.coords} {sprite.name} removed, bottom invalid ({bottom_edge})")
                valid = False
            elif left_edge != ["none"] and any(edge not in sprite.connects["left"] for edge in left_edge):
                # logging.debug(f"{self.coords} {sprite.name} removed, left invalid ({left_edge})")
                valid = False
            elif right_edge != ["none"] and any(edge not in sprite.connects["right"] for edge in right_edge):
                # logging.debug(f"{self.coords} {sprite.name} removed, right invalid ({right_edge})")
                valid = False
            else:
                # logging.debug(f"{self.coords} {sprite.name} correct")
                pass

            if not valid:
                self.candidates.remove(sprite)

        if len(self.candidates) == 1:
            # logging.info(f"tile {self.coords} set to {self.candidates[0].name} by default")
            self.set_sprite(self.candidates[0])

        self.entropy = len(self.candidates)

        return self.entropy
