# Initialize the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Define players
PLAYER_X = 'X'
PLAYER_O = 'O'

def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_move = None
    best_eval = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def ai_move(board):
    best_move = None
    best_eval = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    current_player = PLAYER_O
    while True:
        display_board(board)
        if current_player == PLAYER_O:
            row, col = map(int, input("Enter your move (row and column, e.g., '0 0'): ").split())
        else:
            row, col = ai_move(board)
            print(f"AI's move: {row} {col}")
        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                display_board(board)
                print(f"{current_player} wins!")
                break
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
