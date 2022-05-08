from sprites import Sprite


class Tile:
    def __init__(self, s: Sprite = None) -> None:
        if s is None:
            self.sprite_name = "No Sprite"
            self.short_name = "#"
            self.sprite_loc = (0, 0)
            self.connects = {
                "up": -1,
                "down": -1,
                "left": -1,
                "right": -1,
            }
        else:
            self.set_sprite(s)

    def set_sprite(self, s: Sprite) -> None:
        self.sprite_name = s.name
        self.short_name = s.short_name
        self.sprite_loc = s.loc
        self.connects = s.connects

    def __str__(self) -> str:
        return self.short_name
