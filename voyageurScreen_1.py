import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from voyogeurScreen import Ui_VoyageurMainWindow


class VOYAGEUR(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_VoyageurMainWindow()
        self.ui.setupUi(self)

        self.ui.Search_btn.clicked.connect(self.search_click)
        self.ui.Delete_btn.clicked.connect(self.delete_click)
        self.ui.Add_btn.clicked.connect(self.add_click)

        self.Numero_input = self.ui.Numero_input
        self.Passeport_input = self.ui.Passeport_input
        self.Nom_input = self.ui.Nom_input
        self.prenom_input = self.ui.prenom_input
        self.tel_input = self.ui.tel_input
        self.Adresse_input = self.ui.Adresse_input
        self.Email_input = self.ui.Email_input
        self.numVol_input = self.ui.numVol_input

    def add_click(self):

        with open("voyageurData.txt", "a") as file_data:
            file_data.writelines(self.Numero_input.text() + "," + self.Passeport_input.text() + "," + self.Nom_input.text() + "," + self.prenom_input.text(
            ) + "," + self.tel_input.text() + "," + self.Adresse_input.text() + "," + self.Email_input.text() + "," + self.numVol_input.text() + "\n")

    def search_click(self):
        User_dejafound = False

        with open("voyageurData.txt", "r") as file_data:
            file_data = file_data.readlines()

            for i in range(len(file_data)):
                if file_data[i] == (self.Numero_input.text() + "," + self.Passeport_input.text() + "," + self.Nom_input.text() + "," + self.prenom_input.text(
                ) + "," + self.tel_input.text() + "," + self.Adresse_input.text() + "," + self.Email_input.text() + "," + self.numVol_input.text() + "\n"):
                    User_dejafound = True

            if User_dejafound == True:
                print("Found")
            else:
                print("Not Found")


    def delete_click(self):
        with open("voyageurData.txt", "r") as file_data:
            lines = file_data.readlines()
        
        if (self.Numero_input.text() + "," + self.Passeport_input.text() + "," + self.Nom_input.text() + "," + self.prenom_input.text(
                ) + "," + self.tel_input.text() + "," + self.Adresse_input.text() + "," + self.Email_input.text() + "," + self.numVol_input.text() + "\n") in lines:
            lines.remove(self.Numero_input.text() + "," + self.Passeport_input.text() + "," + self.Nom_input.text() + "," + self.prenom_input.text(
                ) + "," + self.tel_input.text() + "," + self.Adresse_input.text() + "," + self.Email_input.text() + "," + self.numVol_input.text() + "\n")
      
        with open("voyageurData.txt", "w") as file_data:
            for line in lines:
                file_data.write(line)
           
            




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    choose = VOYAGEUR()
    choose.show()
    sys.exit(app.exec_())
