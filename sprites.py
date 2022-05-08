class Sprite:
    def __int__(self, name: str, location: tuple, connects: dict) -> None:
        self.name = name
        self.loc = location
        self.connects = connects
