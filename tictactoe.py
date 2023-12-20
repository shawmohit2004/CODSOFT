import time

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column win

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal win
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal win

    return None  # No winner

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")

    current_player = 'X'

    while True:
        print_board(board)

        player_name = player1 if current_player == 'X' else player2
        row = int(input(f"{player_name}, enter row (0, 1, or 2): "))
        col = int(input(f"{player_name}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎊{player_name} ({current_player}) wins!🎊")
            time.sleep(90)  # Display the winning message for 1 minute
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
