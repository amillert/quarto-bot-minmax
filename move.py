class Move:
    def __init__(self, board, rest_positions, rest_pawns, parent=None, level=0):
        import utils.functions as f
        self.board = board
        self.rest_positions = rest_positions
        self.rest_pawns = rest_pawns
        self.moves = []
        self.parent = parent
        self.level = level
        self.winning = f.check_board_result(self.board)
    
    def add_move(self, move):
        assert isinstance(move, Move), f"Single move must be of type `Move`, passed type: `{type(move)}`"
        self.moves.append(move)
