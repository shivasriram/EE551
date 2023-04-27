'''
Author: Shiva Sriram

Description: Tic Tac Toe game using python
'''
# Library imports
import random

# Tic Tac Toe class
class TicTacToe:
    # Constructor initializes the board
    def __init__(self):
        self.board = []
    
    # Create 3x3 board
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(' ') 
            self.board.append(row)

    # Choose random player to start the game
    def choose_player(self):
        return random.randint(0, 1) # 0 for player 1 and 1 for player 2
    
    # Check if move is valid
    def check_valid(self, r, c):
        # Check if row and column are within the board
        if r < 0 or r > 2 or c < 0 or c > 2:
            return False
        
        # Check if position is empty
        if self.board[r][c] != ' ': 
            return False
        
        # Valid move
        return True   
    
    # Move made by player
    def move(self, player, r, c):
        if not self.check_valid(r, c):
            raise ValueError("Invalid move")
        self.board[r][c] = player  


    # Check win condition
    def check_win(self, player):
        win = None # No win condition

        n = len(self.board)

        # Check rows
        for r in range(n):  
            win = True
            for c in range(n):
                if self.board[r][c] != player:
                    win = False
                    break   
            if win: return win

        # Check columns
        for c in range(n):
            win = True
            for r in range(n):
                if self.board[c][r] != player:
                    win = False
                    break   
            if win: return win

        # Check diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win: return win

        # Check reverse diagonals
        win = True
        for i in range(n):  
            if self.board[i][n-i-1] != player:
                win = False
                break   
        if win: return win

        # No win condition
        return False
    
    # Check if board is full
    def check_full(self):
        for r in self.board:
            for v in r:
                if v == ' ':
                    return False
        return True
    
    # Switch player
    def switch_player(self, player):
        return 'X' if player == 'O' else 'O'
    
    # Print board
    def print_board(self):
        for r in self.board:
            for v in r:
                print(v, end=' ')
            print()

    # Undo move
    def undo_move(self, r, c):
        self.board[r][c] = ' '
    
    # Play game
    def play(self):
        # Initialize board to a 3x3 matrix
        self.create_board()

        # Choose random player to start the game
        player = "X" if self.choose_player() == 0 else "O"
        
        # Play game while there is no win or draw
        while True:
            # Print player turn
            print("Player ", player, " turn")

            # Print board
            self.print_board()

            # Get player move
            r,c = map(int, input("Enter row and column: ").split())

            # Make move
            self.move(player, r-1, c-1)

            # Check win condition   
            if self.check_win(player):
                print("Player ", player, " wins")
                break

            # Check draw condition
            if self.check_full():   
                print("Draw")
                break
            
            # Switch player
            player = self.switch_player(player)
        
        self.print_board()

# Main function
tic_tac_toe = TicTacToe()
tic_tac_toe.play()


    