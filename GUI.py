# Import random
#from random import randint
import tkinter
import tkinter.messagebox

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
        board = tkinter.PhotoImage(file='Board.png')
        self.panel_board.create_image(3, 3, image=board, anchor='nw')

        # Pawn Black 1
        self.panel_pawnB1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black Pawn image
        pawnB = tkinter.PhotoImage(file='pawnB.png')
        self.panel_pawnB1.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 2
        self.panel_pawnB2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB2.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 3
        self.panel_pawnB3 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB3.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 4
        self.panel_pawnB4 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB4.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 5
        self.panel_pawnB5 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB5.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 6
        self.panel_pawnB6 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB6.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 7
        self.panel_pawnB7 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB7.create_image(3, 3, image=pawnB, anchor='nw')
        # Pawn Black 8
        self.panel_pawnB8 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnB8.create_image(3, 3, image=pawnB, anchor='nw')
        # Rook Black 1
        self.panel_rookB1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black rook image
        rookB = tkinter.PhotoImage(file='rookB.png')
        self.panel_rookB1.create_image(3, 3, image=rookB, anchor='nw')
        # Rook Black 2
        self.panel_rookB2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_rookB2.create_image(3, 3, image=rookB, anchor='nw')
        # Knight Black 1
        self.panel_knightB1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black knight image
        knightB = tkinter.PhotoImage(file='knightB.png')
        self.panel_knightB1.create_image(3, 3, image=knightB, anchor='nw')
        # Knight Black 2
        self.panel_knightB2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_knightB2.create_image(3, 3, image=knightB, anchor='nw')
        # Bishop Black 1
        self.panel_bishopB1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black bishop image
        bishopB = tkinter.PhotoImage(file='bishopB.png')
        self.panel_bishopB1.create_image(3, 3, image=bishopB, anchor='nw')
        # Bishop Black 2
        self.panel_bishopB2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_bishopB2.create_image(3, 3, image=bishopB, anchor='nw')
        # Queen Black
        self.panel_queenB = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black queen image
        queenB = tkinter.PhotoImage(file='queenB.png')
        self.panel_queenB.create_image(3, 3, image=queenB, anchor='nw')
        # King Black
        self.panel_kingB = tkinter.Canvas(width=70, height=70, bg='grey')
        #load black king image
        kingB = tkinter.PhotoImage(file='kingB.png')
        self.panel_kingB.create_image(3, 3, image=kingB, anchor='nw')

        # Pawn White 1
        self.panel_pawnW1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white pawn image
        pawnW = tkinter.PhotoImage(file='pawnB.png')
        self.panel_pawnW1.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 2
        self.panel_pawnW2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW2.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 3
        self.panel_pawnW3 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW3.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 4
        self.panel_pawnW4 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW4.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 5
        self.panel_pawnW5 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW5.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 6
        self.panel_pawnW6 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW6.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 7
        self.panel_pawnW7 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW7.create_image(3, 3, image=pawnW, anchor='nw')
        # Pawn White 8
        self.panel_pawnW8 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_pawnW8.create_image(3, 3, image=pawnW, anchor='nw')
        # Rook White 1
        self.panel_rookW1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white rook image
        rookW = tkinter.PhotoImage(file='rookB.png')
        self.panel_rookW1.create_image(3, 3, image=rookW, anchor='nw')
        # Rook White 2
        self.panel_rookW2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_rookW2.create_image(3, 3, image=rookW, anchor='nw')
        # Knight White 1
        self.panel_knightW1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white knight image
        knightW = tkinter.PhotoImage(file='knightB.png')
        self.panel_knightW1.create_image(3, 3, image=knightW, anchor='nw')
        # Knight White 2
        self.panel_knightW2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_knightW2.create_image(3, 3, image=knightW, anchor='nw')
        # Bishop White 1
        self.panel_bishopW1 = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white bishop image
        bishopW = tkinter.PhotoImage(file='bishopB.png')
        self.panel_bishopW1.create_image(3, 3, image=bishopW, anchor='nw')
        # Bishop White 2
        self.panel_bishopW2 = tkinter.Canvas(width=70, height=70, bg='grey')
        self.panel_bishopW2.create_image(3, 3, image=bishopW, anchor='nw')
        # Queen White
        self.panel_queenW = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white queen image
        queenW = tkinter.PhotoImage(file='queenW.png')
        self.panel_queenW.create_image(3, 3, image=queenW, anchor='nw')
        # King White
        self.panel_kingW = tkinter.Canvas(width=70, height=70, bg='grey')
        #load white king image
        kingW = tkinter.PhotoImage(file='kingW.png')
        self.panel_kingW.create_image(3, 3, image=kingW, anchor='nw')

        #Run tkinter GUI
        tkinter.mainloop()

    #Function to load the game
    def play(self):
        # Hide menu controls
        self.button_single.pack_forget()
        self.button_multi.pack_forget()
        self.button_how.pack_forget()
        self.button_exit.pack_forget()

        #show game board
        self.panel_board.pack()

        #show black bishop piece
        self.panel_bishopB1.pack()
        #show black bishop piece
        self.panel_bishopB2.pack()
        # show white bishop piece
        self.panel_bishopW1.pack()
        # show white bishop piece
        self.panel_bishopW2.pack()

        #show black king piece
        self.panel_kingB
        #show white king piece
        self.panel_kingW

        #show black knight piece
        self.panel_knightB1
        #show black knight piece
        self.panel_knightB2
        #show white knight piece
        self.panel_knightW1
        #show white knight piece
        self.panel_knightW2

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

#pawn piece object
class pawn:
    def __init__(self):

#Bishop piece object
class bishop:
    def __init__(self):

#Rook piece object
class rook:
    def __init__(self):

#Knight piece object
class knight:
    def __init__(self):

#Queen piece object
class queen:
    def __init__(self):


#King piece object
class king:
    def __init__(self):



#Create a GUI
gui = GUI()
