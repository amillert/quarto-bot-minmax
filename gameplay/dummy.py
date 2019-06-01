import random


def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    bot_chosen_position = random.choice(possible_positions)
    possible_positions = [x for x in possible_positions if x != bot_chosen_position]
    i, j = [int(x) for x in bot_chosen_position]
    board[i][j] = pawn_picked_for_bot
    # print("Bot randomly picked position: ", bot_chosen_position)
    # print_board()
    # print()
    pawn_chosen_for_player = random.choice(possible_pawns)
    possible_pawns = [x for x in possible_pawns if x != pawn_chosen_for_player]
    print("Bot randomly picked pawn: ", pawn_chosen_for_player)
    print("BOOOOOOT:")
    print(len(possible_pawns), possible_pawns)
    print(len(possible_positions), possible_positions)
    print()
    return possible_positions, possible_pawns, pawn_chosen_for_player, board


def user_move(possible_positions, possible_pawns, pawn_chosen_for_player, board):
    picked_pos = random.choice(possible_positions)
    possible_positions = [x for x in possible_positions if x != str(picked_pos)]
    i, j = [int(x) for x in picked_pos]
    board[i][j] = pawn_chosen_for_player
    pawn_picked_for_bot = random.choice(possible_pawns)
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    print("USSSSSSSRRRR")
    print(len(possible_pawns), possible_pawns)
    print(len(possible_positions), possible_positions)
    print()
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
