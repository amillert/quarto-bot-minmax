import copy
import random

from move import Move
import utils.functions as f


def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    print(len(possible_pawns), len(possible_positions))
    print(f"QUARTO-BOT has been given {pawn_picked_for_bot} pawn.")
    root = Move(board, possible_positions, possible_pawns)
    f.recursive_combinations(root, pawn_picked_for_bot, len(root.rest_pawns))
    print(possible_positions)
    print(possible_pawns)
    print(pawn_picked_for_bot)
    print("moves: ", len(root.moves))
    print()
    print()
    print()
    # exit(500)
    # f.recursive_combinations(root, pawn_picked_for_bot, 0)
    # print("len: ", len(root.moves))
    # finding first good move
    # exit(12)

    # get only winning
    all_paths = f.get_shortened_paths(root)
    print("all paths: ", len(all_paths))
    most_common_path = f.get_most_common_path(all_paths)
    # print(len(most_common_path))
    # exit(12)
    # print([f.check_board_result(path[-1].board) for path in most_common_path])
    # print(f.check_board_result(most_common_path[-1]))
    i, j, bot_picked_pawn = f.find_difference_between_boards(most_common_path[1], most_common_path[0])
    bot_picked_position = str(i) + str(j)
    if bot_picked_pawn != pawn_picked_for_bot:
        bot_picked_position = random.choice(possible_positions)
    # print(f"And picked the position {bot_picked_position} for it.")
    possible_positions = [x for x in possible_positions if x != bot_picked_position]
    # i, j = [int(x) for x in bot_picked_position]
    board[i][j] = pawn_picked_for_bot
    # res = f.check_board_result(board)
    
    # tu może być wygrana już i trzeba przerwać
    if f.check_if_winning(board):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("It is a winning board:")
        f.print_board(board)
        print("The game has been won by the QUARTO-BOT!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        exit(5)

    ## possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    # print("The board looks like so:")
    # f.print_board(board)
    i, j, pawn_picked_for_player = f.find_difference_between_boards(most_common_path[2], most_common_path[1])
    f.print_board(board)
    print(pawn_picked_for_player)
    # exit(99)
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_player]
    # print(len(possible_pawns), len(possible_positions))
    return possible_positions, possible_pawns, pawn_picked_for_player, board


def user_move(possible_positions, possible_pawns, pawn_picked_for_player, board):
    # print(len(possible_pawns), len(possible_positions))
    # print(f"PLAYER has been given {pawn_picked_for_player} pawn.")
    # print(f"There are {possible_positions} possible positions to place it.")
    # print("Where do You wish to place the pawn? ")
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

    # print("The board looks like so:")
    # f.print_board(board)
    # print(f"There are {possible_pawns} possible pawns to choose from.")
    # print("Which one do You wish to pick for the bot? ")
    pawn_picked_for_bot = input()
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    # print(len(possible_pawns), len(possible_positions))
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
