class Piece:
    def __init__(self, side, name):
        # piece ID
        self.name = name
        # Color of the piece
        self.side = side
        # straight movement directions
        self.chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # diagonal movement directions
        self.chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    # Check to see if piece can move
    def isValid(self, startpos, endpos, board):
        # Return boolean if target coordinates is a move the piece can make
        return True if (endpos in self.moves(startpos[0], startpos[1], board)) else False

    # Default response for moves
    def moves(self, y, x, board):
        print("ERROR: no movement for base class")

    # Provide moves in each direction provided until a piece is found
    def collision(self, y, x, board, side, intervals):
        answers = []
        # Go through each possible direction
        for yint, xint in intervals:
            # increment one in current direction
            ytemp, xtemp = y + yint, x + xint
            # increment coordinate in current direction while still on the board
            while self.isInBounds(ytemp, xtemp):
                # select whatever is at those board coordinates
                target = board.get((ytemp, xtemp), None)
                # Check to see if there is a peace at position
                if target is None:
                    # Add as a possible move
                    answers.append((ytemp, xtemp))
                # Check to see if the piece found can be captured
                elif target.side != side:
                    # Add as a possible move
                    answers.append((ytemp, xtemp))
                    # stop creating moves in direction
                    break
                # Error catch
                else:
                    break

                # increment coordinate by one in current direction
                ytemp, xtemp = ytemp + yint, xtemp + xint
        # return all possible moves found
        return answers

    # Makes sure the piece is in the confines of the board
    def isInBounds(self, y, x):
        # Return boolean if coordinates are within a 8x8 grid
        return True if (0 <= y < 8) and (0 <= x < 8) else False

    # Check to see piece can move
    def noConflict(self, board, initSide, y, x):
        # Return bool if destination is in bounds of board and no allied piece is in the way
        return True if self.isInBounds(y, x) and (((y, x) not in board) or board[(y, x)].side != initSide) else False