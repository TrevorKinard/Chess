import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
import PyQt5.QtCore as QtCore
import PyQt5
import Chess

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Chess-Game-grey.ico'))
        self.setWindowTitle('Chess')
        self.setMinimumSize(640, 400)
        self.resize(640, 400)

        # Center window
        window = self.frameGeometry()
        window.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(window.topLeft())

        self.game = Chess.Game()

        self.initUI()

    def initUI(self):
        # Menu Bar
        # Create menu bar
        self.mainMenu = self.menuBar()
        # Create exit Menu Item
        self.exititem = QAction('Exit', self)
        self.mainMenu.addAction(self.exititem)
        self.exititem.triggered.connect(self.close)

        # Create rules Menu Item
        self.rulesitem = QAction('Rules', self)
        self.mainMenu.addAction(self.rulesitem)
        self.rulesitem.triggered.connect(lambda: self.createDialog(title="Rules", message='Rules'))

        # Create how to Menu Item
        self.helpitem = QAction('How to Play', self)
        self.mainMenu.addAction(self.helpitem)
        self.helpitem.triggered.connect(lambda: self.createDialog(title="How to Play", message='How to Play'))

        sqr = (self.height() - 8) if self.height() + 19 > self.width() else (self.width() - 8)

        # Create text based chess canvas
        self.chessBoard = QLabel(self)
        self.chessBoard.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.chessBoard.setText(self.game.play())
        self.chessBoard.setGeometry(self.width() / 2 - sqr / 2, self.height() / 2 - sqr / 2, sqr, sqr)

        # Create text input bar
        self.inputBar = QLineEdit(self)
        self.inputBar.setGeometry(self.chessBoard.x(), self.chessBoard.height() + 8, self.chessBoard.width(), 15)

    # Resize Gui elements during GUI resizing events
    def resizeEvent(self, *args, **kwargs):
        sqr = (self.width() - 50) if self.height() + 19 > self.width() else (self.height() - 50)

        self.chessBoard.setFont(QFont("Times", .035 * sqr, QFont.Bold))
        self.chessBoard.setGeometry(self.width() / 2 - sqr / 2, 23, sqr, sqr)

        self.inputBar.setGeometry(self.chessBoard.x(), self.chessBoard.y() + self.chessBoard.height() + 4, self.chessBoard.width(), 20)

    # Grab enter key event to update the game
    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.chessBoard.setText(self.game.play(self.inputBar.text()))
            self.inputBar.setText("")

    # Create a message dialog box
    def createDialog(self, title="", message=""):
        dialog = ScrollMessageBox()
        dialog.setText(open('Data/' + message).read())
        dialog.setWindowTitle(title)

        dialog.exec_()

# Custom message dialog
class ScrollMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        # Load in parent clss
        QMessageBox.__init__(self, *args, **kwargs)

        # Add scroll area
        scroll = QScrollArea(self)
        # Set scroll area resizable
        scroll.setWidgetResizable(True)

        # Widget to hold the content
        self.content = QWidget()
        # Set widget to scroll area
        scroll.setWidget(self.content)
        # create layout for content
        self.grid = QVBoxLayout(self.content)

        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:300 px; min-height: 300px}")

    def setText(self, p_str):
        label = QLabel(p_str, self)
        label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.grid.addWidget(label)


if __name__ == '__main__':
    # Multi-Resolution Support
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    # Set the style of the entire GUI
    app.setStyleSheet(open('Data/CSS.cfg').read())
    # Create GUI
    win = GUI()
    win.show()
    sys.exit(app.exec_())
