import random
from math import inf as infinity

boxes = [
    "TopLeft",
    "TopMiddle",
    "TopRight",
    "MiddleLeft",
    "Middle",
    "MiddleRight",
    "BottomLeft",
    "BottomMiddle",
    "BottomRight"
]
COMP = +1
HUMAN = -1
nodecount = 0

# NO Pruning
# 59704
# 934
# 46
# Alpha-Beta Pruning
# 2337
# 74
# 16


def getbestplay(board):
    global nodecount
    nodecount = 0
    depth = len(emptyspaces(board))
    if depth == 0 or gameover(board):
        return "none"

    if depth == 9:
        return getrandomplay(board)
    else:
        move = minimax(board, depth, COMP, -infinity, infinity)
        box = move[0]
    print(nodecount)
    return box


def minimax(board, depth, player, alpha, beta):
    global nodecount
    if player == COMP:
        best = ["", -infinity]
    else:
        best = ["", +infinity]

    if depth == 0 or gameover(board):
        score = evaluate(board)
        return ["", score]

    for space in emptyspaces(board):
        box = space
        board[box] = player
        score = minimax(board, depth - 1, -player, alpha, beta)
        board[box] = ""
        score[0] = box
        nodecount += 1

        if player == COMP:
            if score[1] > best[1]:
                best = score
                alpha = max(alpha, best[1])

                if beta <= alpha:
                    break
        else:
            if score[1] < best[1]:
                best = score
                beta = min(beta, best[1])

                if beta <= alpha:
                    break

    return best


def minimaxNOAB(board, depth, player):
    global nodecount
    if player == COMP:
        best = ["", -infinity]
    else:
        best = ["", +infinity]

    if depth == 0 or gameover(board):
        score = evaluate(board)
        return ["", score]

    for space in emptyspaces(board):
        box = space
        board[box] = player
        score = minimaxNOAB(board, depth - 1, -player)
        board[box] = ""
        score[0] = box
        nodecount += 1

        if player == COMP:
            if score[1] > best[1]:
                best = score

        else:
            if score[1] < best[1]:
                best = score

    return best

def evaluate(board):
    if wins(board, COMP):
        score = +1
    elif wins(board, HUMAN):
        score = -1
    else:
        score = 0

    return score


def gameover(board):
    return wins(board, HUMAN) or wins(board, COMP)


def emptyspaces(board):
    empty = []
    for space in board:
        if board[space] == "":
            empty.append(space)

    return empty


def wins(board, player):
    # "TopLeft" "TopMiddle" "TopRight" "MiddleLeft" "Middle" "MiddleRight" "BottomLeft"
    # "BottomMiddle" "BottomRight"
    winner = False
    # horizontal wins
    if board["TopLeft"] == player and board["TopMiddle"] == board["TopLeft"] and \
            board["TopRight"] == board["TopLeft"]:
        winner = True
    if board["MiddleLeft"] == player and board["Middle"] == board["MiddleLeft"] and \
            board["MiddleRight"] == board["MiddleLeft"]:
        winner = True
    if board["BottomLeft"] == player and board["BottomMiddle"] == board["BottomLeft"] and \
            board["BottomRight"] == board["BottomLeft"]:
        winner = True

    # vertical wins
    if board["TopLeft"] == player and board["MiddleLeft"] == board["TopLeft"] and \
            board["BottomLeft"] == board["TopLeft"]:
        winner = True
    if board["TopMiddle"] == player and board["Middle"] == board["TopMiddle"] and \
            board["BottomMiddle"] == board["TopMiddle"]:
        winner = True
    if board["TopRight"] == player and board["MiddleRight"] == board["TopRight"] and \
            board["BottomRight"] == board["TopRight"]:
        winner = True

    # diagonal wins
    if board["TopLeft"] == player and board["Middle"] == board["TopLeft"] and \
            board["BottomRight"] == board["TopLeft"]:
        winner = True
    if board["TopRight"] == player and board["Middle"] == board["TopRight"] and \
            board["BottomLeft"] == board["TopRight"]:
        winner = True

    return winner


def getrandomplay(board):
    rand = random.randint(0, 8)
    while not board[boxes[rand]] == "":
        rand = random.randint(0, 8)
    box = boxes[rand]
    return box
