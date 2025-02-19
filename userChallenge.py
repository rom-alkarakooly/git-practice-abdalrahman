def print_board(board):
    """
    Print the current state of the tic-tac-toe board.
    
    Args:
        board (list): 3x3 list representing the game board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 10)


def check_winner(board, player):
    """
    Check if the specified player has won the game.
    
    Args:
        board (list): 3x3 list representing the game board
        player (str): The player symbol ('X' or 'O') to check for winning
    
    Returns:
        bool: True if the player has won, False otherwise
    """
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
    """
    Check if the board is completely filled.
    
    Args:
        board (list): 3x3 list representing the game board
    
    Returns:
        bool: True if the board is full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)


def get_player_move(board, current_player):
    """
    Get and validate a move from the current player.
    
    Args:
        board (list): 3x3 list representing the game board
        current_player (str): The current player's symbol ('X' or 'O')
    
    Returns:
        tuple: A tuple of (row, col) representing the valid move position
    """
    while True:
        try:
            row, col = map(
                int,
                input(f"Player {current_player}, enter row col (0-2): ").split()
            )
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid position. Numbers must be between 0 and 2.")
                continue
                
            if board[row][col] == " ":
                return row, col
            else:
                print("Position already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers 0-2 separated by space.")


def initialize_board():
    """
    Create and initialize an empty 3x3 tic-tac-toe board.
    
    Returns:
        list: A 3x3 list with empty spaces represented by ' '
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def play_game():
    """
    Main game loop for the tic-tac-toe game.
    
    Manages the game flow including:
    - Board initialization
    - Player turns
    - Move validation
    - Win/draw detection
    - Game termination
    """
    board = initialize_board()
    players = ["X", "O"]
    
    print("Tic-Tac-Toe Game")
    print_board(board)
    
    # Main game loop
    for turn in range(9):
        current_player = players[turn % 2]
        
        # Get valid move from player
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
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