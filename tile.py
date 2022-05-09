from sprites import Sprite


class Tile:
    def __init__(self, coordinates: tuple, s: Sprite = None) -> None:
        self.coords = coordinates

        if s is None:
            self.sprite = Sprite("No Sprite", "#", (0, 0), {"up": -1, "down": -1, "left": -1, "right": -1})
        else:
            self.set_sprite(s)

    def __str__(self) -> str:
        return self.sprite.short_name

    def set_sprite(self, s: Sprite) -> None:
        self.sprite = s
        self.candidates = []

    def update_candidates(self):
        pass
