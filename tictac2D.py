import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Initialize game state
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.game_over = False

        # Initialize UI
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[tk.Button(self.root, text=" ", width=10, height=3,
            command=lambda row=row, col=col: self.on_click(row, col))
            for col in range(3)] for row in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

        self.reset_button = tk.Button(self.root, text="Reset Game",
            command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def check_winner(self, player):
        """
        Check if the given player has won the game.
        Returns True if the player has won, False otherwise.
        """
        # Check rows and columns
        if any(all([self.board[i][j] == player for j in range(3)]) for i in range(3)):
            return True

        if any(all([self.board[j][i] == player for j in range(3)]) for i in range(3)):
            return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or \
            all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_board_full(self):
        """
        Check if the game board is full.
        Returns True if the board is full, False otherwise.
        """
        return all(" " not in row for row in self.board)

    def on_click(self, row, col):
        """
        Handle a button click event.
        """
        if self.game_over:
            return

        if self.board[row][col] == " ":
            self.board[row][col] = self.players[self.current_player]
            self.buttons[row][col].config(text=self.players[self.current_player],
                state="disabled")

            if self.check_winner(self.players[self.current_player]):
                messagebox.showinfo("Tic Tac Toe",
                    f"Player {self.players[self.current_player]} wins!")
                self.game_over = True
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = (self.current_player + 1) % 2

    def reset_game(self):
        """
        Reset the game state and UI.
        """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0
        self.game_over = False

        for row in self.buttons:
            for button in row:
                button.config(text=" ", state="normal")

    def run(self):
        """
        Run the game.
        """
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
