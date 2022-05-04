import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from main_window import Ui_MainWindow

from naoqi import ALProxy


class Logic:
    def __init__(self,win):

        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.connections()

    def connections(self):

        self.ui.noButton.clicked.connect(self.on_noButton_clicked)
        self.ui.yesButton.clicked.connect(self.on_yesButton_clicked)

        self.ui.speakButton.clicked.connect(self.on_speakButton_clicked)
        self.ui.phraseEdit.returnPressed.connect(self.on_phraseEdit_returnPressed)

    def say_something(self,shost):

        tts = ALProxy("ALTextToSpeech", "192.168.12.103", 9559)
        tts.say(str(shost))

    def on_noButton_clicked(self):
        self.say_something("no")

    def on_yesButton_clicked(self):
        self.say_something("yes")


    def on_speakButton_clicked(self):
        shost = self.ui.phraseEdit.text()

        self.say_something(shost)


    def on_phraseEdit_returnPressed(self):

        shost = self.ui.phraseEdit.text()

        self.say_something(shost)



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    logic = Logic(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
