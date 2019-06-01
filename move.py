class Move:
    def __init__(self, board, rest_positions, rest_pawns, level=0):
        self.board = board.copy()
        self.rest_positions = rest_positions
        self.rest_pawns = rest_pawns
        self.moves = []
        self.level = level
    
    def add_move(self, move):
        assert isinstance(move, Move), f"Single move must be of type `Move`, passed type: {type(move)}"
        self.moves.append(move)
