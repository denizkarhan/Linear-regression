from PyQt5 import QtWidgets
from _mainWin import Ui_MainWindow
from _graphWin import Ui_MainWindow1
from summaryWin import Ui_MainWindow2
import sys
from PyQt5.QtWidgets import * 

glbPath = ''
glbSameTh = 0
glbScoreTh = 0

class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

class Second2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browseFile)
        self.ui.sendEnd.clicked.connect(self.sendEnd)  
        Window.setStyleSheet(self,"background-image: url(Background.png);")
        title = "Text Summarization with Graph"
        Window.setWindowTitle(self, title)  
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui5.setupUi(self.window)
        self.window.show()

    def browseFile(self):
        print("pressed")
        self.open_dialog_box()
    
    def showSummary(self, summary):
        self.ui.summary.setText(self, summary)

    def open_dialog_box(self):
        global glbPath
        filename = QFileDialog.getOpenFileName()        
        path = filename[0] # path of selected file
        glbPath = path
        print(glbPath)
        self.ui.textPath.setPlainText(path) # show the path to user on main window 
        self.ui.warningLabel.setText("")
    def sendEnd (self):
        if (not (glbPath and len(glbPath))):
            return
        glbScoreTh = self.ui.scoreTh.toPlainText()
        glbSameTh = self.ui.sameTh.toPlainText()
        # if(self.ui.WordE.isChecked()):
            # summary = start.start(glbPath, glbSameTh, glbScoreTh, "WordE")
        # elif(self.ui.Bert.isChecked()):
            # summary = start.start(glbPath, glbSameTh, glbScoreTh)
        # if(self.ui.textPath.toPlainText==""):
            # self.ui.warningLabel.setText("please choose a file")
        # file = open("Summary.txt", "w")
        # file.write(summary.strip(" \r\t"))
        # rougeItems = calculate_rouge(summary.strip(" \r\t"), "The messages will be \"unwrapped\" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs.A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery.It is the 17th year that the gallery has invited an artist to dress their Christmas tree.The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate.His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades.")
        # score = ""
        # for key, value in rougeItems.items():
            # val = str(value)[:4] if len(str(value)) > 4 else str(value)
            # score += str(key) + ": " + val + "\n"
        self.ui.summary.setText(summary + "\n\n" + score)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
