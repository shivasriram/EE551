import tkinter as tk
from tkinter import messagebox
from tttgpt import TicTacToe

# Tic Tac Toe GUI Class
class TicTacToeGUI:
    def __init__(self, master):
        self.tic_tac_toe = TicTacToe()
        self.master = master
        self.master.title("Tic Tac Toe")
        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(self.master, text=" ", width=10, height=3,
                                                command=lambda row=r, col=c: self.on_click(row, col))
                self.buttons[r][c].grid(row=r, column=c)

    def on_click(self, r, c):
        if self.tic_tac_toe.board[r][c] == ' ':
            self.tic_tac_toe.move(self.player, r, c)
            self.buttons[r][c].config(text=self.player)

            if self.tic_tac_toe.check_win(self.player):
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset_board()
            elif self.tic_tac_toe.check_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.player = self.tic_tac_toe.switch_player(self.player)

    def reset_board(self):
        self.tic_tac_toe.clear_board()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ")

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()