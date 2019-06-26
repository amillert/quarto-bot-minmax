import utils.functions as f

board=[["1111","1111","1111","1111"],["1111","1111"," "," "],["1111"," ","1111"," "],["1111"," "," ","1111"]]

print(f.is_horizontally_winning(board))
print(f.is_vertically_winning(f.transpose(board)))
print(f.is_diagonally_winning(board))