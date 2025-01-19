import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from volScreen import Ui_VolMainWindow
from PyQt5.QtWidgets import QMessageBox


class VOL(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_VolMainWindow()
        self.ui.setupUi(self)

        self.ui.Search_btn.clicked.connect(self.search_click)
        self.ui.Delete_btn.clicked.connect(self.delete_click)
        self.ui.Add_btn.clicked.connect(self.add_click)

        self.Origine_input = self.ui.Origine_input
        self.Destination_input = self.ui.Destination_input
        self.Date_input = self.ui.Date_input
        self.Duree_input = self.ui.Duree_input
        self.numDavion_input = self.ui.numDavion_input

    def add_click(self):

        with open("volData.txt", "a") as file_data:
            file_data.writelines(self.Origine_input.text() +
                                 ',' + self.Destination_input.text() + ',' + self.Date_input.text() + ',' + self.Duree_input.text() + ',' + self.numDavion_input.text() + '\n')

    def search_click(self):
        User_dejafound = False

        with open("volData.txt", "r") as file_data:
            file_data = file_data.readlines()

            for i in range(len(file_data)):
                if file_data[i] == (self.Origine_input.text() +
                                 ',' + self.Destination_input.text() + ',' + self.Date_input.text() + ',' + self.Duree_input.text() + ',' + self.numDavion_input.text() + '\n'):
                    User_dejafound = True

            if User_dejafound == True:
                print("Found")
            else:
                print("Not Found")

    def delete_click(self):
        with open("volData.txt", "r") as file_data:
            lines = file_data.readlines()

        if (self.Origine_input.text() +
                                 ',' + self.Destination_input.text() + ',' + self.Date_input.text() + ',' + self.Duree_input.text() + ',' + self.numDavion_input.text() + '\n') in lines:
            lines.remove(self.Origine_input.text() +
                                 ',' + self.Destination_input.text() + ',' + self.Date_input.text() + ',' + self.Duree_input.text() + ',' + self.numDavion_input.text() + '\n')

        with open("volData.txt", "w") as file_data:
            for line in lines:
                file_data.write(line)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    choose = VOL()
    choose.show()
    sys.exit(app.exec_())
