import json
from PIL import Image


class SpriteSheet:
    def __init__(self, spritedata: str, sprite_image: str) -> None:
        self.sprite_library = []

        with open(spritedata, encoding='utf-8') as f:
            for sprite in json.load(f):
                self.sprite_library.append(
                    Sprite(sprite["name"], sprite["short_name"], tuple(sprite["location"]), sprite["type"],
                           sprite["connects"], sprite["weight"]))

        # Generate "stamps" for tiles
        with Image.open(sprite_image) as im:
            width, height = im.size

            self.image_bank = []
            for y in range(0, height, 16):
                row = []
                for x in range(0, width, 16):
                    stamp = im.crop((x, y, x + 16, y + 16))

                    row.append(stamp)
                self.image_bank.append(row)


class Sprite:
    def __init__(self, name: str, short_name: str, location: tuple, tile_type: str, connects: dict, weight: int) -> None:
        self.name = name
        self.short_name = short_name
        self.loc = location
        self.type = tile_type
        self.connects = connects
        self.weight = weight
