class Tile:
    def __init__(self, resource, number, symbol):
        self.resource = resource
        self.number = number
        self.symbol = symbol
        self.color = self.get_color(resource)

    def get_color(self, resource):
        colors = {
            "wood": "darkgreen",
            "bricks": "red",
            "sheep": "lightgreen",
            "wheat": "yellow",
            "rocks": "gray",
            "desert": "sandybrown"
        }
        return colors.get(resource, "white")
