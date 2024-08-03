import tkinter as tk
from tkinter import messagebox
from game import GameWithMarketPort

class CatanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settlers of Catan")
        self.game = GameWithMarketPort(num_players=4)

        self.setup_ui()

    def setup_ui(self):
        self.board_frame = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.board_frame.pack()

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.build_settlement_button = tk.Button(self.control_frame, text="Build Settlement", command=self.build_settlement)
        self.build_settlement_button.pack(side=tk.LEFT)

        self.build_road_button = tk.Button(self.control_frame, text="Build Road", command=self.build_road)
        self.build_road_button.pack(side=tk.LEFT)

        self.build_city_button = tk.Button(self.control_frame, text="Build City", command=self.build_city)
        self.build_city_button.pack(side=tk.LEFT)

        self.buy_development_card_button = tk.Button(self.control_frame, text="Buy Development Card", command=self.buy_development_card)
        self.buy_development_card_button.pack(side=tk.LEFT)

        self.play_development_card_button = tk.Button(self.control_frame, text="Play Development Card", command=self.play_development_card)
        self.play_development_card_button.pack(side=tk.LEFT)

        self.next_turn_button = tk.Button(self.control_frame, text="Next Turn", command=self.next_turn)
        self.next_turn_button.pack(side=tk.LEFT)

        self.display_board()

    def display_board(self):
        self.board_frame.delete("all")
        hex_size = 50

        hex_positions = [
            (3, 0), (4, 0), (5, 0),
            (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
            (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
            (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
            (3, 4), (4, 4), (5, 4)
        ]

        for i, (col, row) in enumerate(hex_positions):
            x = col * (hex_size * 1.5)
            y = row * (hex_size * (3**0.5) / 2)
            if i < len(self.game.board.tiles):
                tile = self.game.board.tiles[i]
                self.draw_hexagon(x, y, hex_size, tile.color, tile.number)

    def draw_hexagon(self, x, y, size, color, number):
        points = [
            x, y - size,
            x + size * 0.87, y - size / 2,
            x + size * 0.87, y + size / 2,
            x, y + size,
            x - size * 0.87, y + size / 2,
            x - size * 0.87, y - size / 2,
        ]
        self.board_frame.create_polygon(points, fill=color, outline="black")

        if number is not None:
            self.board_frame.create_text(x, y, text=str(number), fill="black", font=("Helvetica", 14, "bold"))

    def build_settlement(self):
        player = self.game.players[self.game.current_turn]
        if player.can_build_settlement():
            location = self.get_location()
            if location and self.game.board.place_settlement(player, location):
                player.build_settlement(location)
                self.display_board()
            else:
                messagebox.showerror("Error", "Invalid location or not enough resources")

    def build_road(self):
        player = self.game.players[self.game.current_turn]
        if player.can_build_road():
            location = self.get_location()
            if location and self.game.board.place_road(player, location):
                player.build_road(location)
                self.display_board()
            else:
                messagebox.showerror("Error", "Invalid location or not enough resources")

    def build_city(self):
        player = self.game.players[self.game.current_turn]
        if player.can_build_city():
            location = self.get_location()
            if location in player.settlements:
                player.build_city(location)
                self.display_board()
            else:
                messagebox.showerror("Error", "Invalid location or not enough resources")

    def buy_development_card(self):
        player = self.game.players[self.game.current_turn]
        if player.can_buy_development_card():
            card = self.game.draw_development_card()
            if card:
                player.buy_development_card(card)
                self.display_board()
            else:
                messagebox.showerror("Error", "No more development cards available")

    def play_development_card(self):
        player = self.game.players[self.game.current_turn]
        if player.development_cards:
            card = player.development_cards.pop()
            self.game.play_development_card(player, card)
            player.played_development_cards.append(card)
            self.display_board()
        else:
            messagebox.showerror("Error", "No development cards to play")

    def get_location(self):
        # For simplicity, we use a fixed location (0, 0) in this example
        return (0, 0)

    def next_turn(self):
        self.game.next_turn()
        messagebox.showinfo("Next Turn", f"Player {self.game.current_turn + 1}'s turn")
