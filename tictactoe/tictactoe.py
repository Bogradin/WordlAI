"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for i in range (2):
        for j in range (2):
            if board[i][j] == X:
                x_count = x_count + 1
            if board[i][j] == O:
                o_count = o_count + 1
    
    if x_count > o_count:
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range (2):
        for j in range (2):
            if (board[i][j] == EMPTY):
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    row, col = action
    board_copy[row][col] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    playerx = X
    playero = O

    if (rowChecker(board, playerx) == True):
        return X
    if (rowChecker(board, playero) == True):
        return O
    if (colChecker(board, playerx) == True):
        return X
    if (colChecker(board, playero) == True):
        return O
    if (diagChecker(board, playerx) == True):
        return X
    if (diagChecker(board, playero) == True):
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    count = 0

    if (winner(board) == X or winner(board) == O):
        return True

    for i in range (2):
        for j in range (2):
            if board[i][j] == EMPTY:
                count = count + 1
    
    if (count > 0):
        return False
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

def colChecker(board, player):
    """
    Checks if player won in any col.
    """
    for i in range (2):
        if (board[i][0] and board[i][1] and board[i][2] == player):
            return True
    else:
        return False

def rowChecker(board, player):
    """
    Checks if player won in any row.
    """
    for i in range (2):
        if (board[0][i] and board[1][i] and board[2][i] == player):
            return True
    else:
        return False

def diagChecker(board, player):
    """
    Checks if player won in any diag.
    """
    if (board[0][0] and board[1][1] and board[2][2] == player):
        return True
    elif (board[2][0] and board[1][1] and board[0][2] == player):
        return True
    else:
        return False