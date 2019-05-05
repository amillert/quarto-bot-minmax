import random
from itertools import combinations

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
empty_board = [[[""]*4]*4]
possible_pawns = ["{0:04b}".format(x) for x in range(16)]

possible_positions = possible_positions[-10:]
possible_pawns = possible_pawns[-10:]

board = empty_board.copy()
pawns = possible_pawns.copy()

dic = {}
pos = random.choice(possible_positions)
paw = random.choice(possible_pawns)

new_possible_pawns = [x for x in possible_pawns if x != paw]
new_possible_positions = [x for x in possible_positions if x != pos]
dic[Node(paw, pos, new_possible_pawns, new_possible_positions)] = {}
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
    return dic

new_dic = {}
it = 0
while new_dic != dic:
    new_dic = foo(dic.copy())

# foo(dic)
# print(1)
# foo(dic)
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


# print(dic)


def bar(dic):
    for k, v in dic.items():
        if not v:
            print(f"pawn: {k.pawn}")
            print(f"position: {k.position}")
        else:
            bar(dic[k])
        print()

bar(dic)