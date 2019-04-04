from .Piece import Piece

class King(Piece):
    # All Possible moves
    def moves(self, y, x, board):
        return [(yy, xx) for yy, xx in self.moveList(y, x) if self.noConflict(board, self.side, yy, xx)]

    # List of king moves
    def moveList(self, y, x):
        return [(y + 1, x), (y + 1, x + 1), (y + 1, x - 1), (y, x + 1), (y, x - 1), (y - 1, x), (y - 1, x + 1),
                (y - 1, x - 1)]