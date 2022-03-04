# minmax func
#import copy

blank = ' '

def minmax(board, player, opp, curr, depth):
    if game_over(board, player, opp) or depth < 0:
        score = evaluate(board, player, opp)
        return score, None

    moves = possible_moves(board, curr)
    move_to_return = None

    alpha = -float('inf')
    beta = float('inf')

    for move in moves:
        ns = next_status(board, curr, move[0], move[1])
        score, _ = minmax(ns, player, opp, curr=opp if curr == player else player, depth=depth - 1)

        if curr == player:
            if score > alpha:
                alpha = score
                move_to_return = move
        elif score < beta:
            beta = score
            move_to_return = move

    return alpha if curr == player else beta, move_to_return


def negmax(board, player, opp, curr, depth, neg):
    if game_over(board, player, opp) or depth < 0:
        score = evaluate(board, player, opp)
        return neg * score, None

    moves = possible_moves(board, curr)
    move_to_return = None

    alpha = -float('inf')
    for move in moves:
        ns = next_status(board, curr, move[0], move[1])
        score, _ = minmax(ns, player, opp, curr=opp if curr == player else player, depth=depth - 1)
        if score < alpha:
            alpha = -score
            move_to_return = move
    return alpha, move_to_return


def ab_minmax(board, player, opp, curr, depth, alpha, beta):
    if game_over(board, player, opp) or depth < 0:
        score = evaluate(board, player, opp)
        return score, None

    moves = possible_moves(board, curr)
    move_to_return = None
    for move in moves:
        ns = next_status(board, curr, move[0], move[1])
        score, _ = ab_minmax(ns, player, opp, curr=opp if curr == player else player, depth=depth - 1, alpha=alpha, beta=beta)
        if curr == player:
            if score > alpha:
                alpha = score
                move_to_return = move
            if alpha >= beta:
                break
        elif score < beta:
            beta = score
        elif alpha >= beta:
            break
    if curr == player:
        return alpha, move_to_return
    else:
        return beta, None
    
def print_board(board):
    for i in range(len(board[0])):
        row = [board[j][i] for j in range(len(board))]
        row = map(str, row)
        print('|'.join(row))

def make_board(width):
    return [[blank] * width for _ in range(width)]

def possible_moves(board, curr):
    d = len(board)
    return [(y, x) for y in range(d) for x in range(d) if board[y][x] == blank]


def next_status(old, player, col, row):
    new = [i[:] for i in old]
    new[col][row] = player
    return new


def game_over(board, player, opp):
    pass

def evaluate(board, player, opp):
    pass