from Data.Pieces import *

BLACK = "Black"
WHITE = "White"

class Game:
    def __init__(self):
        # Turn variable (True = White | False = Black)
        self.turn = True
        self.message = "Movement:"
        self.board = {}
        # Populate the board
        self.placePieces()
        print("Enter moves using grid coordinates separated by a space")
        self.main()

    #Game loop
    def main(self):
        while True:
            # Create board
            self.printBoard()
            # Display Info
            print(self.message)
            # Reset message
            self.message = ""
            # Grab a segmented input
            startpos, endpos = self.parseInput()

            #Attempt to find piece to move
            try: target = self.board[startpos]
            except:
                self.message = "could not find piece; index probably out of range"
                target = None

            if target:
                #Display piece found
                print("found " + str(target))

                #Check piece is correct side
                if target.side != self.turn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue

                #Check piece can move
                if target.isValid(startpos, endpos, self.board):
                    # Tell player the piece can move
                    self.message = "that is a valid move"

                    # Check to see if the king is in check
                    self.isCheck(target, endpos)
                    # trigger for if a king has been captured
                    endgame = True if endpos in self.board and self.board[endpos] == King else False

                    #Move piece to position
                    self.board[endpos] = self.board[startpos]
                    #Remove the piece from its previous position
                    del self.board[startpos]

                    # reset the game and state the winner
                    if endgame:
                        print("White" if target.side else "Black" + " wins the game!\n\n")
                        break
                    #Switch turn
                    self.turn = not self.turn

                # Warn player the specified move is not available
                else:
                    self.message = "invalid move" + str(target.moves(startpos[0], startpos[1], self.board))
                    print(target.moves(startpos[0], startpos[1], self.board))

            # Tell the player that there is no piecce at the location
            else:
                self.message = "there is no piece in that space"

    # Board populator <-- Todo convert to GUI interface
    def placePieces(self):
        # List of back row pieces
        classes = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        #Loop to populate both sides' pawns
        for i in range(0, 8):
            self.board[(1, i)] = Pawn(True, icons[WHITE][Pawn], 1)
            self.board[(6, i)] = Pawn(False, icons[BLACK][Pawn], -1)

        #Loop to populate both sides' back row pieces
        for i in range(0, 8):
            self.board[(0, (7 - i))] = classes[i](True, icons[WHITE][classes[i]])
            self.board[(7, i)] = classes[i](False, icons[BLACK][classes[i]])

    # Print the console based board <-- Todo replace with GUI interface
    def printBoard(self):
        # Print Letter grid
        print(" | A  | B |  C |  D | E  | F  | G |  H |")
        # Loop through x grid
        for i in range(0, 8):
            # Print row breakers
            print("⚊" * 26)
            # Print number grid
            print(i + 1, end="| ")
            # Loop through y grid
            for j in range(0, 8):
                # Print piece at board location
                print(str(self.board.get((i, j), "⛆")) + ' |', end=" ")
            # Place row breakers below grid
            print()
        # End Row breakers
        print("⚊" * 26)

    # Splits and converts the input to index locations <-- Todo convert to GUI interface
    def parseInput(self):
        # Prevent improper input from crashing the program
        try:
            # Seperate the input into two variables (by space)
            a, b = input().split()
            # Convert varaiables to a 2D matrix index
            a = (int(a[1].lower()) - 1, ord(a[0]) - 97)
            b = (int(b[1].lower()) - 1, ord(b[0]) - 97)
            # Tell The player the location
            print(a, b)
            # return the index
            return a, b
        except:
            # Tell the player the input was incorrect
            print("error decoding input. please try again")
            # Return an invalid location
            return (-1, -1), (-1, -1)

    #Checks to see if either king is in check
    def isCheck(self, threat, position):
        # loop through each piece in board
        for check, king in self.board.items():
            #check if moved piece threatens the opposing King
            if threat.isValid(position, check, self.board) and type(king) == King:
                # Return check status of kings after
                return print("White" if king.side else "Black" + " is in check!")

# Dictionary of the icons to display to console
icons = {BLACK: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
         WHITE: {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}}
Game()