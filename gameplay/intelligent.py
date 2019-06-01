import copy
import random

from move import Move
import utils.functions as f


def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    # current situation
    root = Move(copy.deepcopy(board), copy.deepcopy(possible_positions), copy.deepcopy(possible_pawns))
    # generating moves
    f.recursive_combinations(copy.deepcopy(possible_positions), copy.deepcopy(possible_pawns), board, root)
    # finding first good move
    steps = f.minmax(root, None)
    print(steps)
    if steps:
        print("from minmax")
        bot_chosen_position = [x[0] for x in steps if x[1] == pawn_picked_for_bot][0]
        steps = steps[:-1]
        pawn_chosen_for_player = steps[0][1]
    else:
        print("from random")
        bot_chosen_position = random.choice(possible_positions)
        pawn_chosen_for_player = random.choice(possible_pawns)
    print(bot_chosen_position)
    possible_positions = [x for x in possible_positions if x != bot_chosen_position]
    i, j = [int(x) for x in bot_chosen_position]
    board[i][j] = pawn_picked_for_bot
    possible_pawns = [x for x in possible_pawns if x != pawn_chosen_for_player]
    return possible_positions, possible_pawns, pawn_chosen_for_player, board


def user_move(possible_positions, possible_pawns, pawn_chosen_for_player, board):
    print(f"Pawn chosen for you is: {pawn_chosen_for_player}")
    print("Possible positions are: ", possible_positions)
    print("Where do You wish to place Your pawn? ")
    user_picked_position = input()
    assert len(str(user_picked_position)) == 2, "You must pass positions on the board"
    possible_positions = [x for x in possible_positions if x != str(user_picked_position)]
    # possible_pawns = [x for x in possible_pawns if x != pawn_chosen_for_player]
    print("Possible pawns are: ", possible_pawns)
    print("What pawn do You wish to choose for the bot? ")
    pawn_picked_for_bot = input()
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    i, j = [int(x) for x in user_picked_position]
    board[i][j] = pawn_picked_for_bot
    f.print_board(board)
    print()
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
