import json

class SpriteSheet:
    def __init__(self, spritedata):
        self.sprite_library = []

        with open(spritedata, "r") as f:
            for sprite in json.load(spritedata):
                self.sprite_library.append(Sprite)




class Sprite:
    def __init__(self, name: str, short_name: str, location: tuple, connects: dict) -> None:
        self.name = name
        self.short_name = short_name
        self.loc = location
        self.connects = connects
