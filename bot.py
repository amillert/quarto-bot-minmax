import random
from itertools import combinations
import numpy as np

class Node:
    def __init__(self, pawn, position, rest_pawns, rest_positions):
        self.pawn = pawn
        self.position = position
        self.rest_pawns = rest_pawns
        self.rest_positions = rest_positions
    def __hash__(self):
        return hash((self.pawn, self.position, ''.join(self.rest_pawns), ''.join(self.rest_positions)))
    def __eq__(self, other):
        return (self.pawn, self.position, self.rest_pawns, self.rest_positions) == (other.pawn, other.position, other.rest_pawns, other.rest_positions)
    def __ne__(self, other):
        return not(self == other)

possible_positions = [f"{i}{j}" for i in range(4) for j in range(4)]
possible_pawns = ["{0:04b}".format(x) for x in range(16)]
possible_positions = random.choices(possible_positions, k=10)
possible_pawns = random.choices(possible_pawns, k=10)
empty_board = [["    "]*4]*4

sample_board = np.array(empty_board.copy())
positions = possible_positions.copy()
pawns = possible_pawns.copy()
for _ in range(len(positions)):
    rand_pos = random.choice(positions)
    rand_pos_i, rand_pos_j = [int(x) for x in rand_pos]
    positions.remove(rand_pos)
    rand_pawn = random.choice(pawns)
    pawns.remove(rand_pawn)
    sample_board[rand_pos_i][rand_pos_j] = rand_pawn

for row in sample_board:
    print(row)

board = empty_board.copy()
pawns = possible_pawns.copy()

dic = {}
position = random.choice(possible_positions)
pawn = random.choice(possible_pawns)

new_possible_pawns = [x for x in possible_pawns if x != pawn]
new_possible_positions = [x for x in possible_positions if x != position]
dic[Node(pawn, position, new_possible_pawns, new_possible_positions)] = {}
# print(list(dic.keys())[0].position, list(dic.keys())[0].pawn)

rest_pawns = list(dic.keys())[0].rest_pawns.copy()
rest_pos = list(dic.keys())[0].rest_positions.copy()

combs = [i for sub in [x for x in combinations(zip(rest_pawns, rest_pos), 2)] for i in sub]

dic[list(dic.keys())[0]] = {Node(pa, po, [x for x in rest_pawns if x != pa], [x for x in rest_pos if x != po]): {} for pa, po in combs}
# print([(x.pawn, x.position) for x in list([x for x in list(dic.values())][0].keys())])

def foo(dic):
    for k, v in dic.items():
        if not v:
            ancestor = k
            ancestors_possible_pawns = ancestor.rest_pawns.copy()
            ancestors_possible_positions = ancestor.rest_positions.copy()
            combs = [i for sub in [x for x in combinations(zip(ancestors_possible_pawns, ancestors_possible_positions), 2)] for i in sub]
            dic[k] = {Node(pa, po, [x for x in ancestors_possible_pawns if x != pa], [x for x in ancestors_possible_positions if x != po]): {} for pa, po in combs}
        else:
            foo(dic[k])


foo(dic)
print(1)
foo(dic)
# print(2)
# foo(dic)
# print(3)
# foo(dic)
# print(4)
# foo(dic)
# print(5)
# foo(dic)
# print(6)
# foo(dic)
# print(7)
# foo(dic)
# print(8)
# foo(dic)
# print(9)
# foo(dic)
# print(10)
# foo(dic)
# print(11)
# foo(dic)
# print(12)


# print(dic)


def bar(dic):
    for k, v in dic.items():
        if not v:
            print(f"pawn: {k.pawn}")
            print(f"position: {k.position}")
            print()
        else:
            bar(dic[k])

bar(dic)
