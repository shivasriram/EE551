# Library Imports
import random
import sys

# Tic Tac Toe Game Class
class TicTacToe:
    # Constructor   
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Keep track of wins
        self.player1_wins = 0
        self.player2_wins = 0
    
    # Choose random player to start the game
    def choose_player(self):
        return random.randint(0, 1) # 0 for player 1 and 1 for player 2
    
    # Check if the input is an integer
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
        # Get user input
        try :
            r, c = input("Enter row and column (or type 'q q' or 'quit quit' to quit): ").split()
        except:
            print("Invalid input, try again")
            return self.get_move()
        
        # Check if user wants to quit
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
    
    # Quit game
    def quit_game(self):
        print("Game ended.")
        sys.exit()

    # Check win condition
    def check_win(self, player):
        # Check if any row or column has all the same values
        for i in range(3):
            if self.board[i] == [player] * 3:
                if player == 'X':
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
                return True
            if [self.board[j][i] for j in range(3)] == [player] * 3:
                if player == 'X':
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
                return True
        # Check if any diagonal has all the same values
        if [self.board[i][i] for i in range(3)] == [player] * 3:
            if player == 'X':
                self.player1_wins += 1
            else:
                self.player2_wins += 1
            return True
        # Check if reverse diagonal has all the same values
        if [self.board[i][2 - i] for i in range(3)] == [player] * 3:
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
        for r in self.board:
            print(' '.join(r))

    # Print scoreboard
    def print_scoreboard(self):
        print("Player X wins: ", self.player1_wins)
        print("Player O wins: ", self.player2_wins)
    
    # Undo move
    def undo_move(self, r, c):
        self.board[r][c] = ' '
    
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

# Main function
tic_tac_toe = TicTacToe()
tic_tac_toe.play()



# Generated by CodiumAI

import pytest

"""
Code Analysis

Main functionalities:
The TicTacToe class is a game that allows two players to play tic-tac-toe against each other. The game is played on a 3x3 board and the players take turns placing their symbol (X or O) on the board. The game ends when one player gets three of their symbols in a row (horizontally, vertically, or diagonally) or when the board is full and there is no winner.

Methods:
- __init__(self): Constructor that initializes the board and player wins.
- choose_player(self): Chooses a random player to start the game.
- check_int(value): Static method that checks if a value is an integer.
- check_valid(self, r, c): Checks if a move is valid (within the board and not already taken).
- move(self, player, r, c): Makes a move on the board.
- get_move(self): Gets the player's move input.
- quit_game(self): Quits the game.
- check_win(self, player): Checks if a player has won the game.
- check_full(self): Checks if the board is full.
- switch_player(self, player): Switches the player.
- print_board(self): Prints the current board.
- print_scoreboard(self): Prints the current scoreboard.
- undo_move(self, r, c): Undoes a move.
- clear_board(self): Clears the board.
- play(self): Plays the game.

Fields:
- board: A 3x3 list that represents the game board.
- player1_wins: The number of wins for player 1 (X).
- player2_wins: The number of wins for player 2 (O).
"""

class TestTicTacToe:
    # Tests that the player1_wins counter is incremented correctly when player 1 wins a game. 
    def test_player1_wins(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
        tic_tac_toe.check_win('X')
        assert tic_tac_toe.player1_wins == 1

    # Tests that the player2_wins counter is incremented correctly when player 2 wins a game. 
    def test_player2_wins(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = [['O', 'X', ' '], ['O', 'X', ' '], ['O', ' ', ' ']]
        tic_tac_toe.check_win('O')
        assert tic_tac_toe.player2_wins == 1

    # Tests that the program handles invalid input (non-integer values for row and column) correctly by prompting the user to enter valid input. 
    def test_invalid_input(self, monkeypatch, capsys):
        tic_tac_toe = TicTacToe()
        monkeypatch.setattr('builtins.input', lambda _: 'a b')
        tic_tac_toe.get_move()
        captured = capsys.readouterr()
        assert captured.out == "Invalid input, try again\n"

    # Tests that the program handles out-of-bounds input (values for row and column that are not between 1 and 3) correctly by prompting the user to enter valid input. 
    def test_out_of_bounds(self, monkeypatch, capsys):
        tic_tac_toe = TicTacToe()
        monkeypatch.setattr('builtins.input', lambda _: '4 5')
        tic_tac_toe.get_move()
        captured = capsys.readouterr()
        assert captured.out == "Invalid input, try again\n"

    # Tests that the program restarts the game correctly when the user chooses to play again. 
    def test_restart_game(self, monkeypatch, capsys):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
        monkeypatch.setattr('builtins.input', lambda _: 'y')
        tic_tac_toe.play()
        captured = capsys.readouterr()
        assert captured.out == "Enter row and column (or type 'q q' or 'quit quit' to quit): \nPlayer X turn\nX O  \nX O  \nX    \nPlayer X  wins\nPlayer X wins:  1\nPlayer O wins:  0\nPlay again? (y/n): \nEnter row and column (or type 'q q' or 'quit quit' to quit): \n"

    # Tests that the program handles input for a cell that has already been played correctly by prompting the user to enter valid input. 
    def test_already_played(self, monkeypatch, capsys):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = [['X', 'O', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        monkeypatch.setattr('builtins.input', lambda _: '1 1')
        tic_tac_toe.get_move()
        captured = capsys.readouterr()
        assert captured.out == "Invalid move, try again\n"
def codium_tests_results(method=None):
    import contextlib
    import json
    import os

    import pytest

    class ResultsCollector:
        def __init__(self):
            self.reports = {}

        @pytest.hookimpl(hookwrapper=True)
        def pytest_runtest_makereport(self):
            outcome = yield
            report = outcome.get_result()
            if report.when == 'call':
                self.reports[report.head_line.split(".")[-1]] = {"passed": report.passed,
                                                                 "message": report.longreprtext}

    results = None
    try:
        test_results = ResultsCollector()
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                if method:
                    pytest.main(
                        [__file__, "-q", "--disable-warnings", "--no-header", "-vv", "--showlocals", "-k", method],
                        plugins=[test_results])
                else:
                    pytest.main([__file__, "-q", "--disable-warnings", "--no-header", "-vv", "--showlocals"],
                                plugins=[test_results])
        results = json.dumps(test_results.reports)
    except Exception as e:
        results = json.dumps({"codium_tests_results_error": str(e)})
    if results is not None:
        print("=== Codium Tests Results ===")
        print(results)
        print("=== End Codium Tests Results ===")
