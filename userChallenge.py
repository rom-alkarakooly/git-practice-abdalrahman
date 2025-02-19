def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if (all(board[i][j] == player for j in range(3)) or 
            all(board[j][i] == player for j in range(3))):
            return True
    
    # Check diagonals
    if (all(board[i][i] == player for i in range(3)) or 
        all(board[i][2-i] == player for i in range(3))):
        return True
    
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    # Initialize game
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    
    print("Tic-Tac-Toe Game")
    print_board(board)
    
    # Main game loop
    for turn in range(9):
        current_player = players[turn % 2]
        
        # Get valid move from player
        while True:
            try:
                row, col = map(
                    int,
                    input(f"Player {current_player}, enter row col (0-2): ").split()
                )
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Position already taken. Try again.")
            except:
                print("Invalid input. Please enter numbers 0-2.")
        
        print_board(board)
        
        # Check game ending conditions
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        
        if is_board_full(board):
            print("Draw!")
            return
    
    print("Draw!")


if __name__ == "__main__":
    play_game() 