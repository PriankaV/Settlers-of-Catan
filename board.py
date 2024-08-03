import random
from tile import Tile

class Board:
    def __init__(self):
        self.tiles = self.generate_tiles()
        self.ports = self.generate_ports()

    def generate_tiles(self):
        resources = ["wood"] * 4 + ["bricks"] * 3 + ["sheep"] * 4 + ["wheat"] * 4 + ["rocks"] * 3 + ["desert"]
        random.shuffle(resources)

        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        random.shuffle(numbers)

        tiles = []
        for resource in resources:
            if resource == "desert":
                tile = Tile(resource, None, "desert.png")
            else:
                tile = Tile(resource, numbers.pop(), f"{resource}.png")
            tiles.append(tile)
        return tiles

    def generate_ports(self):
        # Port generation logic (same as before)
        ports = [
            {"trade_ratio": "2:1", "resource": "wheat"},
            {"trade_ratio": "2:1", "resource": "sheep"},
            {"trade_ratio": "2:1", "resource": "rocks"},
            {"trade_ratio": "2:1", "resource": "wood"},
            {"trade_ratio": "3:1", "resource": "any"},
            {"trade_ratio": "3:1", "resource": "any"},
            {"trade_ratio": "3:1", "resource": "any"},
            {"trade_ratio": "3:1", "resource": "any"},
        ]
        random.shuffle(ports)
        return ports

    def place_settlement(self, player, location):
        # Simplified for the example
        return True

    def place_road(self, player, location):
        # Simplified for the example
        return True
