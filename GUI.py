# Import random
#from random import randint
import tkinter
import tkinter.messagebox
import Chess

class GUI:
    def __init__(self):
        #Create the GUI window
        self.win = tkinter.Tk()
        #Set GUI title
        self.win.title('Chess')
        #Set GUI Icon
        self.win.iconbitmap(r'Chess-Game-grey.ico')
        #Set the GUI's minimum scale size
        self.win.wm_minsize(600, 600)

        #Button Single Player
        self.button_single = tkinter.Button(self.win, text='Single Player', command=self.play)
        self.button_single.pack()
        #Button Multiplayer
        self.button_multi = tkinter.Button(self.win, text='Multiplayer', command=self.play)
        self.button_multi.pack()
        #Button How to Play
        self.button_how = tkinter.Button(self.win, text='How to Play', command=self.instructions)
        self.button_how.pack()
        #Button Exit
        self.button_exit = tkinter.Button(self.win, text='Exit', command=self.win.destroy)
        self.button_exit.pack()
        #Board
        self.panel_board = tkinter.Canvas(width=572, height=572, bg='grey')
        #Load board image
        board = tkinter.PhotoImage(file='Data\\Board.png')
        self.panel_board.create_image(3, 3, image=board, anchor='nw')

        #Run tkinter GUI
        tkinter.mainloop()

    def addpiece(self, name, image, row=0, column=0):
        # Create image of piece
        self.panel_board.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        # Set position of image on canvas
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        # Save pieces position with given name
        self.pieces[name] = (row, column)
        # Set image of pieces position on canvas
        self.panel_board.coords(name, (column * self.size) + int(self.size / 2), (row * self.size) + int(self.size / 2))

    # ? Obselete
    def refresh(self, event):
        # Redraw the board for canvas change or resize
        self.size = min(int((event.width-1) / self.columns), int((event.height-1) / self.rows))
        # ?
        self.panel_board.delete("square")
        color = self.color2
        # Loop through x axis
        for row in range(self.rows):
            #set color of peice
            color = self.color1 if color == self.color2 else self.color2
            #
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.panel_board.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.panel_board.tag_raise("piece")
        self.panel_board.tag_lower("square")

    #Function to load the game
    def play(self):
        # Hide menu controls
        self.button_single.pack_forget()
        self.button_multi.pack_forget()
        self.button_how.pack_forget()
        self.button_exit.pack_forget()

        #show game board
        self.panel_board.pack()



    #Instructions of chess
    def instructions(self):
        tkinter.messagebox.showinfo('Rules of Chess', """The Pieces
    Pawns - move one square forwards. Have the option of moving one or two squares on their first move. Capture by
    moving one square diagonally forwards. Promoted to another piece if they reach the far end of the board.
    \nKnights - move in an L-shape - one square vertically and two squares horizontally, or one square horizontally and
    two squares vertically. Can jump over any pieces in its path.
    \nBishops - move any number of squares diagonally in a straight line. May not jump over other pieces.
    \nRooks - move any number of squares vertically or horizontally in a straight line. May not jump over other pieces.
    \nThe Queen - moves any number of squares vertically, horizontally, or diagonally in a straight line. May not jump
    over other pieces.
    \nThe King - moves one square in any direction. May not move onto a square threatened by an enemy piece.
\nCheck and Checkmate
    Check - if the king is threatened by an enemy piece, he is in 'check', and must escape from check. This can be
    done by moving the king, capturing the checking piece, or blocking the checking piece (so long as it isn't a knight).
    \nCheckmate - if the king is in check and can't get out of check, he is in checkmate and the game is lost.
\nCastling
    Castling - move the king two squares towards the rook, and jump the rook to the square on the other side of the
    king.
    \nYou cannot castle if...
        You have previously moved your king or rook.
        There are pieces between your king and rook.
        Your king in check.
        Your king would be in check at the end of the move.
        Your king would cross a square that is threatened by an enemy piece.
\nEn Passant
    En Passant - if you have a pawn on the fifth rank, and your opponent moves an adjacent pawn two squares, you
    can capture the pawn as if it had only moved one square.
    \nYou cannot capture en passant if...
        Your pawn is not on the fifth rank.
        The enemy pawn did not move two squares on the previous move.""")

#Create a GUI
gui = GUI()
