def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([s == player for s in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_turn = 0

    while True:
        print_board(board)
        print(f"Player {players[current_turn]}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = players[current_turn]
            if check_winner(board, players[current_turn]):
                print_board(board)
                print(f"Player {players[current_turn]} wins!")
                break
            current_turn = (current_turn + 1) % 2
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    game()