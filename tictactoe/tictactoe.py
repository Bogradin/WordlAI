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
    i = sum(x is not None for x in board[0]) + sum(x is not None for x in board[1]) + sum(x is not None for x in board[2])

    if (i % 2 == 0):
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setMoves = set()

    for i in range(3):
        for j in range(3):
            if(board[i][j] is None):
                setMoves.add((i, j))
    if len(setMoves) == 0:
        return None
    return setMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedBoard = copy.deepcopy(board)
    playerTurn = player(board)
    
    i = action[0]
    j = action[1]

    copiedBoard[i][j] = playerTurn

    return copiedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = {X, O}

    for player in players:
        for row in range(3):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                return player
    
        for col in range(3):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                return player
        
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
            
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            return player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == O) or (winner(board) == X):
        return True
    for row in range(3):
        for col in range(3):
            if(board[row][col] is None):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerGame = winner(board)
    if (winnerGame is X):
        return 1
    elif (winnerGame is O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
