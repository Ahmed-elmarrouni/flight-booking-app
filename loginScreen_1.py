import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from loginScreen import Ui_LoginMainWindow

from voyogeurScreen import Ui_VoyageurMainWindow

from volScreen import Ui_VolMainWindow


class Login(QtWidgets.QMainWindow, Ui_LoginMainWindow):

    def openWindowA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VoyageurMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VolMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginMainWindow()
        self.ui.setupUi(self)

        self.ui.Vol_btn.clicked.connect(self.vol_click)
        self.ui.Voyageur_btn.clicked.connect(self.Voyageur_click)
        self.ui.New_btn.clicked.connect(self.new_click)


        self.Email_input = self.ui.Email_input
        self.Password_input = self.ui.Password_input

    def new_click(self):
         
        with open("UserandPassword.txt", "a") as file_data:
            file_data.writelines(self.Email_input.text(
            ) + "," + self.Password_input.text() + "\n")


    def vol_click(self):
        User_dejafound = False

        with open("UserandPassword.txt", "r") as file_data:
            file_data = file_data.readlines()

            for i in range(len(file_data)):
                if file_data[i] == (self.Email_input.text()+"," + self.Password_input.text()+"\n"):
                    User_dejafound = True

            if User_dejafound == True:
                self.openWindowB()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Attention")
                msg.setText("Account Not Found")
                msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                msg.setIcon(QMessageBox.Warning)
                a = msg.exec_()

  
    def Voyageur_click(self):
        User_dejafound = False

        with open("UserandPassword.txt", "r") as file_data:
            file_data = file_data.readlines()

            for i in range(len(file_data)):
                if file_data[i] == (self.Email_input.text()+"," + self.Password_input.text()+"\n"):
                    User_dejafound = True

            if User_dejafound == True:
                self.openWindowA()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Attention")
                msg.setText("Account Not Found")
                msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                msg.setIcon(QMessageBox.Warning)
                b = msg.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    choose = Login()
    choose.show()
    sys.exit(app.exec_())
