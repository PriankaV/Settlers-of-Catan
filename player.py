class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.resources = {"wheat": 0, "sheep": 0, "rocks": 0, "wood": 0, "bricks": 0}
        self.victory_points = 0
        self.settlements = []
        self.cities = []
        self.roads = []
        self.development_cards = []
        self.played_development_cards = []

    def can_build_settlement(self):
        return self.resources["wheat"] >= 1 and self.resources["sheep"] >= 1 and self.resources["wood"] >= 1 and self.resources["bricks"] >= 1

    def can_build_road(self):
        return self.resources["wood"] >= 1 and self.resources["bricks"] >= 1

    def can_build_city(self):
        return self.resources["wheat"] >= 2 and self.resources["rocks"] >= 3

    def can_buy_development_card(self):
        return self.resources["wheat"] >= 1 and self.resources["sheep"] >= 1 and self.resources["rocks"] >= 1

    def build_settlement(self, location):
        self.resources["wheat"] -= 1
        self.resources["sheep"] -= 1
        self.resources["wood"] -= 1
        self.resources["bricks"] -= 1
        self.settlements.append(location)
        self.victory_points += 1

    def build_road(self, location):
        self.resources["wood"] -= 1
        self.resources["bricks"] -= 1
        self.roads.append(location)

    def build_city(self, location):
        self.resources["wheat"] -= 2
        self.resources["rocks"] -= 3
        self.settlements.remove(location)
        self.cities.append(location)
        self.victory_points += 1

    def buy_development_card(self, card):
        self.resources["wheat"] -= 1
        self.resources["sheep"] -= 1
        self.resources["rocks"] -= 1
        self.development_cards.append(card)
