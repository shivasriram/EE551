# Library Imports
import random
import sys
import time

#Global time_limit
time_limit = 10

# Tic Tac Toe Game Class
class TicTacToe:
    # Constructor   
    def __init__(self):
        # Initialize board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Initialize player wins
        self.player1_wins = 0
        self.player2_wins = 0
    
    # Choose random player to start the game
    def choose_player(self):
        return random.randint(0, 1) # 0 for player 1 and 1 for player 2
    
    # Check if the input is an integer using static method
    @staticmethod
    def check_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    # Check if the input is a valid move
    def check_valid(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == ' '
    
    # Make move on the board    
    def move(self, player, r, c):
        if not self.check_valid(r, c):
            print("Invalid move, try again")
            r, c = self.get_move()
        self.board[r][c] = player 
        
    # Get player move
    def get_move(self):
    # Get start time
    #start_time = time.time()
    #while True:
        # Get user input
        try :
            r, c = input("Enter row and column (or type 'q q' or 'quit quit' to quit): ").split()
            # Check if time limit is reached
            #if time.time() - start_time > time_limit:
                #print("game over")
                #self.clear_board()  
        except:
            print("Invalid input, try again")
            return self.get_move()
        
        # Check if user wants to quit
        if r.lower() == "q" or c.lower() == "q" or r.lower() == "quit" or c.lower() == "quit":
            self.quit_game()
        try:
            # Convert input to integers
            r, c = int(r), int(c)
            # Check if input is valid
            if not self.check_valid(r - 1, c - 1):
                raise ValueError
            return r - 1, c - 1
        except:
            print("Invalid input, try again")
            return self.get_move()
  
    # Quit game
    def quit_game(self):
        print("Game ended.")
        sys.exit()

    # Check win condition
    def check_win(self, player):
        # Check if any row or column has all the same values
        for i in range(3):
            if self.board[i] == [player] * 3:
                # Update scoreboard if player wins
                if player == 'X':
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
                return True
            if [self.board[j][i] for j in range(3)] == [player] * 3:
                # Update scoreboard if player wins
                if player == 'X':
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
                return True
        # Check if any diagonal has all the same values
        if [self.board[i][i] for i in range(3)] == [player] * 3:
            # Update scoreboard if player wins
            if player == 'X':
                self.player1_wins += 1
            else:
                self.player2_wins += 1
            return True
        # Check if reverse diagonal has all the same values
        if [self.board[i][2 - i] for i in range(3)] == [player] * 3:
            # Update scoreboard if player wins
            if player == 'X':
                self.player1_wins += 1
            else:
                self.player2_wins += 1
            return True
        return False
    
    # Check draw condition
    def check_full(self):
        return all(v != ' ' for r in self.board for v in r)
    
    # Switch player
    def switch_player(self, player):
        return 'X' if player == 'O' else 'O'
    
    # Print board
    def print_board(self):
        # Print pretty board
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)


    # Print scoreboard
    def print_scoreboard(self):
        print("Player X wins: ", self.player1_wins)
        print("Player O wins: ", self.player2_wins)
    
    # Undo move
    #def undo_move(self, r, c):
        #self.board[r][c] = ' '
    
    # Clear board
    def clear_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Play game
    def play(self):
        while True: 
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
                    self.print_scoreboard()
                    break

                # Check draw condition
                if self.check_full():   
                    print("Draw")
                    self.print_scoreboard()
                    break
                
                # Switch player
                player = self.switch_player(player)
            
            # Print final board
            self.print_board()

            # Prompt user to play again
            while True:
                replay = input("Play again? (y/n): ")
                if replay.lower() == 'y':
                    self.clear_board() # Clear board if they want to play again
                    break
                elif replay.lower() == 'n':
                    print("Thanks for playing!")
                    return
                else:
                    print("Invalid input, please enter 'y' or 'n'")

# Main function (commented for running GUI)
#tic_tac_toe = TicTacToe()
#tic_tac_toe.play()
