from .Piece import Piece

class Queen(Piece):
    # All Possible moves
    def moves(self, y, x, board):
        return self.collision(y, x, board, self.side, self.chessCardinals + self.chessDiagonals)