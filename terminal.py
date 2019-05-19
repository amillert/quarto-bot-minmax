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
xdd = []
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
    
    @staticmethod
    def transpose(board):
        return [[x] for x in zip(*board)]

    # @staticmethod
    # def flip_along_x_axis(board):
    #     return board[::-1]

    @staticmethod
    def is_flatten_empty(list):
        return [x for sub in list for x in sub if not x]

    @staticmethod
    def is_horizontally_winning(board):
        for row in board:
            for i in range(len(row[0])):
                if len(set([x[i] for x in row])) == 1:
                    return True
        return False

    def is_vertically_winning(self, board):
        self.is_horizontally_winning(self.transpose(board))

    @staticmethod
    def is_na_szage_winning(board):
        length = len(board[0])
        diagonal1 = [board[i][i] for i in range(length)]
        diagonal2 = [board[length-i-1][i] for i in [x for x in range(length)]]

        for diagonal in [diagonal1, diagonal2]:
            for i in range(len(diagonal[0])):  # it's same as length, but these two mean sth else
                if len(set([x[i] for x in diagonal])) == 1:
                    return True
        return False

    def check_if_winning(self, board):
        if self.is_vertically_winning or self.is_horizontally_winning or self.is_na_szage_winning:
            return True
        return False

    def minmax(self, root):
        if root.moves:
            if not self.is_flatten_empty(root.board):
                print("weszlo")
                print(root.board)
                winning = self.check_if_winning(root.board)
                if winning:
                    print("Board")
                    print(board)
                    print("IS WINNING!")
                    print()
                    exit(14)
            for move in root.moves:
                self.minmax(move)
        return
    
    def traverse_moves(self, root, level):
        import hashlib
        if root.moves:
            if root.level == level:
                # Checking if all the boards on the same level are the same
                # Seem like they're not, which is what we wanted to prove
                print(root.level, len(root.moves))
                six_digits_hash = hashlib.sha1(str(sorted([x.board for x in root.moves])).encode()).hexdigest()[-6:]
                print(six_digits_hash)
                xdd.append(six_digits_hash)
            for move in root.moves:
                self.traverse_moves(move, level)
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
# root.traverse_moves(root, 3)
# print(xdd)
# print(len(xdd))  # 3600
# print(len(list(set(xdd))))  # 600
# which i assume means, we can remove 5/6 of all the branches at this level, since they're symmetirc
root.minmax(root)