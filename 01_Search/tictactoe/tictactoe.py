"""
Tic Tac Toe Player
"""

from math import inf
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        count_x += row.count("X")
        count_o += row.count("O")

    if count_x > count_o:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    new_board = copy.deepcopy(board)
    current_player = player(board)
    i, j = action
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    for row in board:
        if len(set(row)) == 1 and row[0] is not EMPTY:
            return row[0]
    # Coluums
    for j in range(3):
        columm = [board[i][j] for i in range(3)]
        if len(set(columm)) == 1 and columm[0] is not EMPTY:
            return columm[0]

    # Diagonals
    diag1 = [board[i][i] for i in range(3)]
    if len(set(diag1)) == 1 and diag1[0] is not EMPTY:
        return diag1[0]

    diag2 = [board[i][2 - i] for i in range(3)]
    if len(set(diag2)) == 1 and diag2[0] is not EMPTY:
        return diag2[0]
    # No Winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    final_winner = winner(board)
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actual_player = player(board)
    if actual_player == X:
        best_value = float("-inf")
        best_move = None
        for action in actions(board):
            action_value = min_value(result(board, action), float("-inf"), float("inf"))
            if action_value > best_value:
                best_value = action_value
                best_move = action
        return best_move

    if actual_player == O:
        best_value = float("inf")
        best_move = None
        for action in actions(board):
            action_value = max_value(result(board, action), float("-inf"), float("inf"))
            if action_value < best_value:
                best_value = action_value
                best_move = action
        return best_move


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float("-inf")

    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float("inf")

    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v
