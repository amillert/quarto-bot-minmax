from utils.setup import pos, pawn_picked_for_player, pawns, board, move, last_picked_pawn
import utils.functions as f
import gameplay.intelligent as intelligent
import gameplay.dummy as dummy


if __name__ == "__main__":
    # odd number - bot move after `while`
    while move < 11:
        if not move % 2:
            pos, pawns, pawn_picked_for_bot, board = dummy.user_move(
                pos, pawns, pawn_picked_for_player, board)
            # pos, pawns, pawn_picked_for_bot = user_move(pos, pawns, pawn_picked_for_player)
            if f.check_if_winning(board):
                f.print_board(board)
                print("player wins")
                exit(1)
            last_picked_pawn = pawn_picked_for_bot
        else:
            pos, pawns, pawn_chosen_for_player, board = dummy.bot_move(
                pos, pawns, pawn_picked_for_bot, board)
            if f.check_if_winning(board):
                f.print_board(board)
                print("bot wins")
                exit(2)
            last_picked_pawn = pawn_picked_for_player
        move += 1

    pawns.append(last_picked_pawn)
    print("outside loop")
    print("possible pawns: ", pawns)
    print("possible positions: ", pos)
    print("last chosen pawn: ", last_picked_pawn)
    print()
    print("It's time for bot's move")

    f.print_board(board)
    print()
    print()
    print()
    print()
    print()

    while move < 16:
        if not move % 2:
            pos, pawns, pawn_picked_for_bot, board = dummy.user_move(
                pos, pawns, pawn_picked_for_player, board)
            # pos, pawns, pawn_picked_for_bot =
            # intelligent.user_move(pos, pawns, pawn_picked_for_player)
            if f.check_if_winning(board):
                f.print_board(board)
                print("player wins")
                exit(3)
        else:
            pos, pawns, pawn_picked_for_player, board = intelligent.bot_move(
                pos, pawns, pawn_picked_for_bot, board)
            if f.check_if_winning(board):
                f.print_board(board)
                print("bot wins")
                exit(4)
        move += 1
    print("it's a draw")
