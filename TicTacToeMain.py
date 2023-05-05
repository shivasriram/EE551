# Library imports
import tkinter as tk
from tkinter import messagebox
from TicTacToeMaster import TicTacToe


# Tic Tac Toe GUI Class
class TicTacToeGUI:
    # Initialize game state and UI
    def __init__(self, master):
        # Use class from TicTacToeMaster.py
        self.tic_tac_toe = TicTacToe()
        # Initialize master window for GUI
        self.master = master
        # Set window title
        self.master.title("Tic Tac Toe")
        # Set player to X
        self.player = "X"
        # Initialize buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        # Create empty buttons for game board
        for r in range(3):
            for c in range(3):
                # Create button and bind click event
                self.buttons[r][c] = tk.Button(self.master, text=" ", width=10, height=3, command=lambda row=r, col=c: self.on_click(row, col))
                # Place button in grid
                self.buttons[r][c].grid(row=r, column=c)

        # Create scoreboard
        self.scoreboard = tk.Label(self.master, text=self.get_scoreboard_text())
        self.scoreboard.grid(row=3, columnspan=3)

    # Handle a button click event
    def on_click(self, r, c):
        if self.tic_tac_toe.board[r][c] == ' ':
            # Get move from player
            self.tic_tac_toe.move(self.player, r, c)
            # Update button text to player move
            self.buttons[r][c].config(text=self.player)
            # Check if game is over
            if self.tic_tac_toe.check_win(self.player):
                # Display winner popup
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                # Reset board for playing again
                self.reset_board()
            # Check if board is full (draw)
            elif self.tic_tac_toe.check_full():
                # Display draw popup
                messagebox.showinfo("Game Over", "It's a draw!")
                # Reset board for playing again
                self.reset_board()
            # Switch player
            else:
                self.player = self.tic_tac_toe.switch_player(self.player)
            # Update scoreboard
            self.update_scoreboard()

    # Reset game board
    def reset_board(self):
        # Clear board
        self.tic_tac_toe.clear_board()
        # Reset button text to empty
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ")
    
    # Update scoreboard
    def update_scoreboard(self):
        self.scoreboard.config(text=self.get_scoreboard_text())

    # Get scoreboard text   
    def get_scoreboard_text(self):
        return f"Player X wins: {self.tic_tac_toe.player1_wins}\nPlayer O wins: {self.tic_tac_toe.player2_wins}"


# Main function
if __name__ == "__main__":
    # Create root window    
    root = tk.Tk()
    # Create Tic Tac Toe GUI
    gui = TicTacToeGUI(root)
    # Start GUI and run main loop
    root.mainloop()
