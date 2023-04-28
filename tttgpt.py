import random
import sys

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
    def create_board(self):
        pass
    
    def choose_player(self):
        return random.randint(0, 1) # 0 for player 1 and 1 for player 2
    
    @staticmethod
    def check_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def check_valid(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == ' '
    
    def move(self, player, r, c):
        if not self.check_valid(r, c):
            print("Invalid move, try again")
            r, c = self.get_move()
        self.board[r][c] = player 
        
    def get_move(self):
        try :
            r, c = input("Enter row and column (or type 'q q' or 'quit quit' to quit): ").split()
        except:
            print("Invalid input, try again")
            return self.get_move()
        
        if r.lower() == "q" or c.lower() == "q" or r.lower() == "quit" or c.lower() == "quit":
            self.quit_game()
        try:
            r, c = int(r), int(c)
            if not self.check_valid(r - 1, c - 1):
                raise ValueError
            return r - 1, c - 1
        except:
            print("Invalid input, try again")
            return self.get_move()
            
    def quit_game(self):
        print("Game ended.")
        sys.exit()

    def check_win(self, player):
        for i in range(3):
            if self.board[i] == [player] * 3:
                return True
            if [self.board[j][i] for j in range(3)] == [player] * 3:
                return True
        if [self.board[i][i] for i in range(3)] == [player] * 3:
            return True
        if [self.board[i][2 - i] for i in range(3)] == [player] * 3:
            return True
        return False
    
    def check_full(self):
        return all(v != ' ' for r in self.board for v in r)
    
    def switch_player(self, player):
        return 'X' if player == 'O' else 'O'
    
    def print_board(self):
        for r in self.board:
            print(' '.join(r))
    
    def undo_move(self, r, c):
        self.board[r][c] = ' '
    
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
            #r,c = map(int, input("Enter row and column: ").split())
            r,c = self.get_move()



            # Make move
            self.move(player, r, c)

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


tic_tac_toe = TicTacToe()
tic_tac_toe.play()
