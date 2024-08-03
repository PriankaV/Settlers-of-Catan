import random

class Tile:
    def __init__(self, resource, number):
        self.resource = resource
        self.number = number
        self.color = self.get_color(resource)

    def get_color(self, resource):
        colors = {
            'wood': 'darkgreen',
            'bricks': 'brown',
            'sheep': 'lightgreen',
            'wheat': 'yellow',
            'rocks': 'gray',
            'desert': 'khaki'
        }
        return colors.get(resource, 'white')

class Board:
    def __init__(self):
        resources = ['wood'] * 4 + ['bricks'] * 3 + ['sheep'] * 4 + ['wheat'] * 4 + ['rocks'] * 3 + ['desert']
        random.shuffle(resources)
        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        random.shuffle(numbers)

        self.tiles = []
        number_index = 0
        for resource in resources:
            if resource == 'desert':
                self.tiles.append(Tile(resource, None))
            else:
                self.tiles.append(Tile(resource, numbers[number_index]))
                number_index += 1

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.resources = {'wood': 0, 'bricks': 0, 'sheep': 0, 'wheat': 0, 'rocks': 0}
        self.victory_points = 0
        self.development_cards = []
        self.played_development_cards = []
        self.settlements = []
        self.cities = []

    def can_build_settlement(self):
        return self.resources['wood'] >= 1 and self.resources['bricks'] >= 1 and self.resources['sheep'] >= 1 and self.resources['wheat'] >= 1

    def build_settlement(self, location):
        self.resources['wood'] -= 1
        self.resources['bricks'] -= 1
        self.resources['sheep'] -= 1
        self.resources['wheat'] -= 1
        self.settlements.append(location)
        self.victory_points += 1

    def can_build_road(self):
        return self.resources['wood'] >= 1 and self.resources['bricks'] >= 1

    def build_road(self, location):
        self.resources['wood'] -= 1
        self.resources['bricks'] -= 1

    def can_build_city(self):
        return self.resources['wheat'] >= 2 and self.resources['rocks'] >= 3

    def build_city(self, location):
        self.resources['wheat'] -= 2
        self.resources['rocks'] -= 3
        self.cities.append(location)
        self.victory_points += 1

    def can_buy_development_card(self):
        return self.resources['sheep'] >= 1 and self.resources['wheat'] >= 1 and self.resources['rocks'] >= 1

    def buy_development_card(self, card):
        self.resources['sheep'] -= 1
        self.resources['wheat'] -= 1
        self.resources['rocks'] -= 1
        self.development_cards.append(card)

class GameWithMarketPort:
    def __init__(self, num_players):
        self.players = [Player(i) for i in range(num_players)]
        self.board = Board()
        self.current_turn = 0

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def draw_development_card(self):
        cards = ['Victory Point'] * 5 + ['Road Building'] * 2 + ['Monopoly'] * 2 + ['Year of Plenty'] * 2 + ['Robber'] * 14
        random.shuffle(cards)
        if cards:
            return cards.pop()

    def play_development_card(self, player, card):
        # Placeholder for card effects implementation
        pass
