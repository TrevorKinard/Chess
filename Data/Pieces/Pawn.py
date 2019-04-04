from .Piece import Piece

class Pawn(Piece):
    # Pawn Identification variables
    def __init__(self, side, name, direction):
        self.name = name
        self.side = side
        self.direction = direction
        self.start = True

    # All Possible moves
    def moves(self, y, x, board):
        answers = []
        # Diagonal move 1
        if self.canCapture(board, y + self.direction, x + self.direction) and self.noConflict(board, self.side, y + self.direction, x + self.direction):
            answers.append((y + self.direction, x + self.direction))
        # Diagonal move 2
        if self.canCapture(board, y + self.direction, x - self.direction) and self.noConflict(board, self.side, y + self.direction, x - self.direction):
            answers.append((y + self.direction, x - self.direction))
        # Initial move
        if self.start and (y + self.direction, x) not in board and self.noConflict(board, self.side, y + self.direction * 2, x):
            answers.append((y + self.direction * 2, x))
            self.start = False
        # default move
        if self.noConflict(board, self.side, y + self.direction, x):
            answers.append((y + self.direction, x))

        #return list of available moves
        return answers

    #Makes sure the pawn can do a diagonal move to capture
    def canCapture(self, board, y, x):
        #Return boolean based on if a opposing piece is diagonal of direction of movement
        return True if (y, x) in board and board[(y, x)].side != self.side else False