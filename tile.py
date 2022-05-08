from sprites import Sprite


class Tile:
    def __int__(self):
        self.sprite_name = "No Sprite"
        self.sprite_loc = (0, 0)
        self.connects = {
            "up": -1,
            "down": -1,
            "left": -1,
            "right": -1,
        }

    def __str__(self):
        return self.sprite_name

    def set_sprite(self, s: Sprite) -> None:
        self.sprite_name = s.name
        self.sprite_loc = s.loc
        self.connects = s.connects
