import random

import utils.functions as f

def bot_move(possible_positions, possible_pawns, pawn_picked_for_bot, board):
    print(f"QUARTO-BOT has been given {pawn_picked_for_bot} pawn.")
    bot_picked_position = random.choice(possible_positions)
    print(f"And chose the position {bot_picked_position} for it.")
    possible_positions = [x for x in possible_positions if x != bot_picked_position]
    i, j = [int(x) for x in bot_picked_position]
    board[i][j] = pawn_picked_for_bot
    print("The board looks like so:")
    f.print_board(board)
    pawn_picked_for_player = random.choice(possible_pawns)
    print(f"The pawn chosen for the player is: {pawn_picked_for_player}")
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_player]
    return possible_positions, possible_pawns, pawn_picked_for_player, board


def user_move(possible_positions, possible_pawns, pawn_picked_for_player, board):
    print(f"The PLAYER has been given {pawn_picked_for_player} pawn.")
    player_picked_position = random.choice(possible_positions)
    print(f"And chose the position {player_picked_position} for it.")
    possible_positions = [x for x in possible_positions if x != str(player_picked_position)]
    i, j = [int(x) for x in player_picked_position]
    board[i][j] = pawn_picked_for_player
    print("The board looks like so:")
    f.print_board(board)
    pawn_picked_for_bot = random.choice(possible_pawns)
    print(f"The pawn chosen for the bot is: {pawn_picked_for_player}")
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    return possible_positions, possible_pawns, pawn_picked_for_bot, board
