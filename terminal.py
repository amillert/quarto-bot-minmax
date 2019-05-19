import copy
import random
import numpy as np
from collections import OrderedDict

pos = [f"{i}{j}" for i in range(4) for j in range(4)]
poss = pos[:9]
pos = pos[9:]
pawns = ["{0:04b}".format(x) for x in range(16)]
pawnss = pawns[:9]
pawns = pawns[9:]
board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
moves_dict = OrderedDict()

def print_board():
    print("Showing board:")
    for row in board:
        print(row)
    print()

def bot_random_move(possible_positions, possible_pawns, pawn_picked_for_bot):
    bot_chosen_position = random.choice(possible_positions)
    print("Bot randomly picked position: ", bot_chosen_position)
    possible_positions = [x for x in possible_positions if x != bot_chosen_position]
    pawn_chosen_for_player = random.choice(possible_pawns)
    possible_pawns = [x for x in possible_pawns if x != pawn_picked_for_bot]
    print("Bot randomly picked pawn: ", pawn_chosen_for_player)
    moves_dict[bot_chosen_position] = pawn_chosen_for_player
    i, j = [int(x) for x in bot_chosen_position]
    board[i][j] = pawn_chosen_for_player
    print_board()
    print()
    return possible_positions, possible_pawns, pawn_chosen_for_player

def user_move(possible_positions, possible_pawns, pawn_chosen_for_player):
    print(f"Pawn chosen for you is: {pawn_chosen_for_player}")
    print("Possible positions are: ", possible_positions)
    print("Where do You wish to place Your pawn? ")
    user_picked_position = input()
    assert len(str(user_picked_position)) == 2, "You must pass positions on the board"
    possible_positions = [x for x in possible_positions if x != str(user_picked_position)]
    possible_pawns = [x for x in possible_pawns if x != pawn_chosen_for_player]
    print("Possible pawns are: ", possible_pawns)
    print("What pawn do You wish to choose for the bot? ")
    pawn_picked_for_bot = input()
    moves_dict[user_picked_position] = pawn_picked_for_bot
    i, j = [int(x) for x in user_picked_position]
    board[i][j] = pawn_picked_for_bot
    print_board()
    print()
    return possible_positions, possible_pawns, pawn_picked_for_bot

move = 0

pawn_chosen_for_player = random.choice(pawns)
pawns = [x for x in pawns if x != pawn_chosen_for_player]

while move < 2:
    if not move % 2:
        pos, pawns, pawn_picked_for_bot = user_move(pos, pawns, pawn_chosen_for_player)
    else:
        pos, pawns, pawn_chosen_for_player = bot_random_move(pos, pawns, pawn_picked_for_bot)
    move += 1

print("outside loop")
print("possible pawns: ", pawns)
print("possible positions: ", pos)

print("Time for bots' move")

print(moves_dict)
print(board)

class Move:
    def __init__(self, board, rest_positions, rest_pawns, level=0):
        self.board = board.copy()
        self.rest_positions = rest_positions
        self.rest_pawns = rest_pawns
        self.moves = []
        self.level = level
    
    def add_move(self, move):
        assert isinstance(move, Move), f"Single move must be of type `Move`, passed type: {type(move)}"
        print(type(self.moves))
        print(self.moves)
        print("ADD move moves: ", len(self.moves))
        self.moves.append(move)

    def traverse_moves(self, root):
        import hashlib
        if root.moves:
            if root.level == 3:
                # Checking if all the boards on the same level are the same
                # Seem like they're not, which is what we wanted to prove
                print(root.level, len(root.moves))
                print(hashlib.sha1(str([x.board for x in root.moves]).encode()).hexdigest())
            for move in root.moves:
                self.traverse_moves(move)
        return

def recursive_combinations(pos, pawns, board, root):
    # import time
    # time.sleep(0.5)
    if pawns:
        combs = [[x, y] for x in pos for y in pawns]
        print(len(combs))
        # exit(12)
        print(len(pos), len(pawns))
        for comb in combs:
            pos_comb, pawn_comb = comb
            board_cpy = copy.deepcopy(board)
            i, j = [int(x) for x in pos_comb]
            board_cpy[i][j] = pawn_comb
            rest_pos = [x for x in pos if x != pos_comb]
            rest_pawns = [x for x in pawns if x != pawn_comb]
            node = Move(copy.deepcopy(board_cpy), copy.deepcopy(rest_pos), copy.deepcopy(rest_pawns), root.level+1)
            root.add_move(node)
            recursive_combinations(copy.deepcopy(rest_pos), copy.deepcopy(rest_pawns), copy.deepcopy(board_cpy), node)
    else:
        print("END of branch")
        # return root

# this part is only to ommit making moves in random while
for po, pa in zip(poss, pawnss):
    i, j = [int(x) for x in po]
    board[i][j] = pa
# print(board)
# exit(12)

root = Move(copy.deepcopy(board), copy.deepcopy(pos), copy.deepcopy(pawns))
recursive_combinations(copy.deepcopy(pos), copy.deepcopy(pawns), board, root)
root.traverse_moves(root) 
