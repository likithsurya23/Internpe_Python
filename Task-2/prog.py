# Tic-Tac-Toe Game in Python

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)] # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Function to handle a player's move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}'s turn (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    for turn in range(9):
        player = 'X' if turn % 2 == 0 else 'O'
        make_move(player)
        print_board()

        if check_winner(player):
            print(f"Player {player} wins!")
            return

        if check_draw():
            print("It's a draw!")
            return

    print("It's a draw!")


if __name__ == "__main__":
    play_game()
