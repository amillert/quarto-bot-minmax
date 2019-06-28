import copy
import random

from move import Move
import utils.functions as f


def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    print(f"QUARTO-BOT has been given {pawn_picked_for_bot} pawn.")
    root = Move(board, possible_positions, possible_pawns)
    f.build_moves_tree(root, pawn_picked_for_bot, len(root.rest_pawns))
    # get only winning moves
    all_paths = f.get_shortened_paths(root)
    most_common_path = f.get_most_common_path(all_paths)
    i, j, bot_picked_pawn = f.find_difference_between_boards(most_common_path[1], most_common_path[0])
    bot_picked_position = str(i) + str(j)
    if bot_picked_pawn != pawn_picked_for_bot:
        bot_picked_position = random.choice(possible_positions)
    print(f"And picked the position {bot_picked_position} for it.")
    possible_positions = [x for x in possible_positions if x != bot_picked_position]
    board[i][j] = pawn_picked_for_bot

    # game could have been won at this point and therefore it's best to check
    if f.check_if_winning(board):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("It is a winning board:")
        f.print_board(board)
        print("The game has been won by the QUARTO-BOT!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        exit(5)

    print("The board looks like so:")
    f.print_board(board)
    i, j, pawn_picked_for_player = f.find_difference_between_boards(most_common_path[2], most_common_path[1])
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_player]
    print(len(possible_pawns), len(possible_positions))
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

    print()
    if f.check_if_winning(board):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("It is a winning board:")
        f.print_board(board)
        print("The game has been won by the QUARTO-BOT!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        exit(4)

    print("The board looks like so:")
    f.print_board(board)
    print(f"There are {possible_pawns} possible pawns to choose from.")
    print("Which one do You wish to pick for the bot? ")
    pawn_picked_for_bot = input()
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    print(len(possible_pawns), len(possible_positions))
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
