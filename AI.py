import random

class AI:
    def __init__(self):
        return

    def move(self, board):
        # lists to save simple and capture moves
        movable = []
        capture = []

        # Loop through each piece
        for position, piece in board.items():
            # Check the piece can move and is controlled by the AI
            if piece.moves(position[0], position[1], board) and piece.side:
                # Save piece as a movable piece
                movable.append(position)
                # Loop through all moves of piece
                for target in piece.moves(position[0], position[1], board):
                    # Check to see if the move goes to a blank location
                    if target not in board:
                        pass
                    # Check to see if the move is a capture move
                    elif board[target].side != piece.side:
                        # Save piece as a capture piece
                        capture.append((position, target))

        # Select a random move in the movable list
        choice = random.choice(movable)

        # return the piece and the move to the game
        return (choice, random.choice(board[choice].moves(choice[0], choice[1], board))) if not capture else random.choice(capture)