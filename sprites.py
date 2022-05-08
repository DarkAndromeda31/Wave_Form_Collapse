class Sprite:
    def __int__(self, name: str, short_name: str, location: tuple, connects: dict) -> None:
        self.name = name
        self.short_name = short_name
        self.loc = location
        self.connects = connects

