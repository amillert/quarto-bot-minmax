from utils.setup import pos, pawn_picked_for_player, pawns, board, move, last_picked_pawn
import utils.functions as f
import gameplay.intelligent as intelligent
import gameplay.dummy as dummy


if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("This is the initial part of the game, where the bot is choosing moves randomly.")
    print("User can be either in the automatic, randomized mode or can be played by the human.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    # odd number - bot move after `while`
    while move < 11:
        if not move % 2:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"It is now a turn numero {move+1} and the PLAYER's move.")
            # pos, pawns, pawn_picked_for_bot, board = dummy.user_move(
            #     pos, pawns, pawn_picked_for_player, board)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            pos, pawns, pawn_picked_for_bot, board = intelligent.user_move(
                pos, pawns, pawn_picked_for_player, board)
            if f.check_if_winning(board):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("It is a winning board:")
                f.print_board(board)
                print("The game has been won by the PLAYER!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                exit(1)
            last_picked_pawn = pawn_picked_for_bot
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(
                f"It is now a turn numero {move+1} and the QUARTO-BOT's move.")
            pos, pawns, pawn_picked_for_player, board, bot_picked_position = dummy.bot_move(
                pos, pawns, pawn_picked_for_bot, board)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Bot picked position")
            print(bot_picked_position)
            if f.check_if_winning(board):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("It is a winning board:")
                f.print_board(board)
                print("The game has been won by the QUARTO-BOT!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                exit(2)
            last_picked_pawn = pawn_picked_for_player
        move += 1

    pawns.append(last_picked_pawn)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The initial random part has ended.")
    print("There are still {possible_pawns} left in the game.")
    print("And still free positions: {possible_positions}.")
    print("The board:")
    f.print_board(board)
    print("And it is a QUARTO-BOT's move now.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    import time
    time.sleep(4)

    while move < 16:
        if not move % 2:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"It is now a turn numero {move+1} and the PLAYER's move.")
            # pos, pawns, pawn_picked_for_bot, board = dummy.user_move(
                # pos, pawns, pawn_picked_for_player, board)
            pos, pawns, pawn_picked_for_bot = intelligent.user_move(
                pos, pawns, pawn_picked_for_player, board)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            if f.check_if_winning(board):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("It is a winning board:")
                f.print_board(board)
                print("The game has been won by the PLAYER!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                exit(3)
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(
                f"It is now a turn numero {move+1} and the QUARTO-BOT's move.")
            pos, pawns, pawn_picked_for_player, board = intelligent.bot_move(
                pos, pawns, pawn_picked_for_bot, board)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            if f.check_if_winning(board):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("It is a winning board:")
                f.print_board(board)
                print("The game has been won by the QUARTO-BOT!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                exit(4)
        move += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The game has ended and it is a DRAW.")
    print("Nobody won this time.")
    print("The full board:")
    f.print_board(board)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
