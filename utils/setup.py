import random

pos = [f"{i}{j}" for i in range(4) for j in range(4)]
pawns = ["{0:04b}".format(x) for x in range(16)]
pawn_picked_for_player = random.choice(pawns)
pawns = [x for x in pawns if x != pawn_picked_for_player]
board = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
move = 0
last_picked_pawn = None
LOOSING = -1
DRAW = 0
WINNING = 1
IDLE = 2