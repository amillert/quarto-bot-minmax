import copy

from utils.setup import LOOSING, DRAW, WINNING, IDLE
from move import Move


def print_board(board):
    print("Showing board:")
    for row in board:
        print(row)
    print()


def transpose(board):
    return [list(x) for x in zip(*board)]


# @staticmethod
# def flip_along_x_axis(board):
#     return board[::-1]


def has_empty_spot(list):
    return [x for sub in list for x in sub if x == " "]


def is_horizontally_winning(board):
    for row in board:
        for i in range(len(board)):
            tmp = set([x[i] if x != " " else x for x in row])
            if len(tmp) == 1 and tmp != {" "}:
                return True
    return False


def is_vertically_winning(board):
    return is_horizontally_winning(transpose(board))


def is_diagonally_winning(board):
    length = len(board[0])
    diagonal1 = [board[i][i] for i in range(length)]
    diagonal2 = [board[length-i-1][i] for i in [x for x in range(length)]]
    for diagonal in [diagonal1, diagonal2]:
        for i in range(len(diagonal[0])):  # it's same as length, but these two mean sth else
            tmp = set([x[i] if x != " " else x for x in diagonal])
            if len(tmp) == 1 and tmp != {" "}:
                return True
    return False


def check_if_winning(board):
    if is_vertically_winning(board) or is_horizontally_winning(board) or is_diagonally_winning(board):
        return True
    return False


def find_difference_between_boards(board_x, board_y):
    for i in range(len(board_y)):
        for j in range(len(board_x[i])):
            if board_x[i][j] != board_y[i][j]:
                # position 0 due to the fact less empty board is being passed first
                return i, j, [x for x in [board_x[i][j], board_y[i][j]] if x][0]


def check_board_result(board):
    #  this one to be checked if not reversed statement
    multi = -1 if len([x for sublist in board for x in sublist if x != " "]) % 2 else 1
    # full board
    if check_if_winning(board):
        # win depends on whose move it was
        return multi * WINNING
    elif not has_empty_spot(board):
        return DRAW
    else:
        return IDLE
    

def recursive_combinations(root, last_picked_pawn, thresh):
    if 15 >= thresh > 12:
        thresh = 3
    elif 12 >= thresh > 8:
        thresh = 4
    elif 8 >= thresh > 6:
        thresh = 5
    
    if root.level > thresh:
        return
    
    local_positions = root.rest_positions
    local_pawns = root.rest_pawns
    combinations = [[pos, pawn] 
                     for pos in local_positions 
                     for pawn in local_pawns 
                     if (last_picked_pawn and pawn == last_picked_pawn) or not last_picked_pawn]
    # print(len(combinations), root.level, thresh)
    # print()
    for combination in combinations:
        position, pawn = combination
        i, j = [int(x) for x in position]
        positions_left = [x for x in local_positions if x != position]
        pawns_left = [x for x in local_pawns if x != pawn]
        board_cpy = copy.deepcopy(root.board)
        board_cpy[i][j] = pawn
        move = Move(copy.deepcopy(board_cpy), positions_left, pawns_left, root, root.level+1)
        root.add_move(move)
        recursive_combinations(move, None, thresh)
        if move.level == thresh:
            return
        # recursive_combinations(move, depth-1)

def generate_paths(root):
    if not root.moves: return [[root]]
    paths = []
    for move in root.moves:
        for path in generate_paths(move):
            paths.append([root] + path)
    return paths

def shorten_paths(path, wins_only=True):
    for i, node in enumerate(path):
        board_result = check_board_result(node.board)
        if board_result == 1:
            return i + 1
        # if board_result == -1:
        #     return 0
    if wins_only:
        return 0
    else:
        return len(path)

def get_shortened_paths(root):
    generated_paths = generate_paths(root)
    print("genrated: ", len(generated_paths))
    paths = [path[:shorten_paths(path, True)] for path in generated_paths]
    if not paths:
        paths = [path[:shorten_paths(path, False)] for path in generated_paths]
    less_paths = [path for path in paths if path]
    if not less_paths:
        less_paths = generated_paths
    return less_paths

def get_most_common_path(all_paths):
    min_path_len = min([len(path) for path in all_paths])
    print("min_path_len:", min_path_len)
    chosen_paths = [path for path in all_paths if len(path) == min_path_len and check_board_result(path[-1].board) == 1]
    if not chosen_paths:
        chosen_paths = all_paths
    print("chosen_paths: ", len(chosen_paths))
    # if not chosen_paths:
    #     chosen_paths = [path for path in all_paths if len(path) == min_path_len and check_board_result(path[-1].board) == 0]
    # if not chosen_paths:
    #     chosen_paths = [path for path in all_paths if len(path) == min_path_len and check_board_result(path[-1].board) == 2]
    # if not chosen_paths:
    #     chosen_paths = [path for path in all_paths if len(path) == min_path_len and check_board_result(path[-1].board) == -1]
    # elements in board with .
    # rows in board with *
    # bords in path with ~
    chosen_paths_stringified = ["~".join(["*".join([".".join(row) for row in node.board]) for node in path]) for path in chosen_paths]
    print("chosen_paths_stringified: ", len(chosen_paths_stringified))
    distinct_paths_stringified = list(set(chosen_paths_stringified))
    print("distinct_paths_stringified: ", len(distinct_paths_stringified))
    print()
    most_common_path_stringified = sorted([[k, v] for k, v in {path: chosen_paths_stringified.count(path) for path in distinct_paths_stringified}.items()], key=lambda x: int(x[1]))[0]
    # print()
    # print()
    # print()
    # print(len([[row.split(".") for row in board.split("*")] for board in most_common_path_stringified[0].split("~")]))
    # print([[row.split(".") for row in board.split("*")] for board in most_common_path_stringified[0].split("~")])
    # exit(13)
    return [[row.split(".") for row in board.split("*")] for board in most_common_path_stringified[0].split("~")]

# all_paths = get_shortened_paths(root)
# most_common_path = get_most_common_path(all_paths)
