import utils.functions as f
import random
import copy

#zwraca liste pionkow ktore po ruchu gracza na pewno nie dadza zwyciestwa graczowi w pierwszym ruchu
def select_possible_pawns_for_player( possible_pawns,board):
    possible_pawns_heurestic=copy.deepcopy(possible_pawns)
    for pionek_sprawdzany in possible_pawns:
        for index in range(4):
            for index2 in range(4):
                board2=copy.deepcopy(board)
                if len(board[index][index2])<=1:
                    board2[index][index2]=pionek_sprawdzany
                    if(f.check_if_winning(board2)):
                        if pionek_sprawdzany in possible_pawns_heurestic: possible_pawns_heurestic.remove(pionek_sprawdzany)                      
    return possible_pawns_heurestic
    
#wybor pionka z posrod mozliwych pionkow, ktore nie powinny dac zwycieskiego ruchu
def chosse_pawn_for_player_heuristic( possible_pawns, board):
    possible_pawns_heurestic=select_possible_pawns_for_player(possible_pawns,board)    
    if(len(possible_pawns_heurestic)<=0):

        print("o")
        print(possible_pawns_heurestic)
        return random.choice(possible_pawns)
    else:
        print("o")
        print(possible_pawns_heurestic)
        return random.choice(possible_pawns_heurestic)


def check_if_three_same_features_in_column():
     return 0

