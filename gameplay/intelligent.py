import copy
import random

from move import Move
import utils.functions as f


def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    print(f"QUARTO-BOT has been given {pawn_picked_for_bot} pawn.")
    root = Move(copy.deepcopy(board), copy.deepcopy(possible_positions), copy.deepcopy(possible_pawns))
    f.recursive_combinations(copy.deepcopy(possible_positions), copy.deepcopy(possible_pawns), board, root)
    # finding first good move
    steps = f.minmax(root, None)
    if steps:
        bot_picked_position = [x[0] for x in steps if x[1] == pawn_picked_for_bot][0]
        steps = steps[:-1]
        pawn_picked_for_player = steps[0][1]
    else:
        bot_picked_position = random.choice(possible_positions)
        pawn_picked_for_player = random.choice(possible_pawns)
    print(f"And picked the position {bot_picked_position} for it.")
    possible_positions = [x for x in possible_positions if x != bot_picked_position]
    i, j = [int(x) for x in bot_picked_position]
    board[i][j] = pawn_picked_for_bot
    print("The board looks like so:")
    f.print_board(board)
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_player]
    return possible_positions, possible_pawns, pawn_picked_for_player, board, bot_picked_position


def user_move(possible_positions, possible_pawns, pawn_picked_for_player, board):
    print(f"PLAYER has been given {pawn_picked_for_player} pawn.")
    print(f"There are {possible_positions} possible positions to place it.")
    print("Where do You wish to place the pawn? ")
    player_picked_position = input()
    assert len(str(player_picked_position)) == 2, "You must pass positions on the board"
    possible_positions = [x for x in possible_positions if x != str(player_picked_position)]
    i, j = [int(x) for x in player_picked_position]
    board[i][j] = pawn_picked_for_player
    print("The board looks like so:")
    f.print_board(board)
    print(f"There are {possible_pawns} possible pawns to choose from.")
    print("Which one do You wish to pick for the bot? ")
    pawn_picked_for_bot = input()
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
