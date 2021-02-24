from PyQt5 import QtCore, QtGui, QtWidgets
import os
import re
import shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 334)
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.969849, y1:0.029, x2:1, y2:0.716, stop:0.00502513 rgba(0, 81, 117, 237));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 461, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Button_fichier = QtWidgets.QPushButton(self.frame_2)
        self.Button_fichier.setGeometry(QtCore.QRect(210, 40, 131, 23))
        self.Button_fichier.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Times New Roman\";")
        self.Button_fichier.setObjectName("Button_fichier")
        
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 185, 19))
        self.label.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit_nom_resultat_conversion = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nom_resultat_conversion.setGeometry(QtCore.QRect(10, 70, 441, 25))
        self.lineEdit_nom_resultat_conversion.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 76, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_nom_resultat_conversion.setReadOnly(True)
        self.lineEdit_nom_resultat_conversion.setObjectName("lineEdit_nom_resultat_conversion")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 62, 19))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QtCore.QRect(0, 120, 461, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 271, 41))
        self.label_6.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_nom_resultat_conversion_saisi = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_nom_resultat_conversion_saisi.setGeometry(QtCore.QRect(280, 30, 181, 25))
        self.lineEdit_nom_resultat_conversion_saisi.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 81, 117);\n"
"background-color: rgb(0, 81, 117);")
        self.lineEdit_nom_resultat_conversion_saisi.setObjectName("lineEdit_nom_resultat_conversion_saisi")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 62, 19))
        self.label_5.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_vallidation = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_vallidation.setGeometry(QtCore.QRect(280, 60, 181, 31))
        self.pushButton_vallidation.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Times New Roman\";")
        self.pushButton_vallidation.setObjectName("pushButton_vallidation")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setEnabled(True)
        self.frame_7.setGeometry(QtCore.QRect(0, 230, 461, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_ouvrir_fichier_converti = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_ouvrir_fichier_converti.setGeometry(QtCore.QRect(280, 5, 181, 31))
        self.pushButton_ouvrir_fichier_converti.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Times New Roman\";")
        self.pushButton_ouvrir_fichier_converti.setObjectName("pushButton_ouvrir_fichier_converti")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 141, 41))
        self.label_7.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Button_fichier.clicked.connect(self.select_fichier)
        self.pushButton_vallidation.clicked.connect(self.conversion_file)
        self.pushButton_ouvrir_fichier_converti.clicked.connect(self.ouvrir_fichier)
        self.frame_7.hide()



    def select_fichier(self):
        fileName= QtWidgets.QFileDialog.getOpenFileName(MainWindow,'Fichier à convertir','',"UI files (*.ui)")
        
        self.pathsource = str(fileName[0])
        
        print('1ere ----------------------------22222------------------------------------------')
        
        self.nom_fichier_sans_extention = os.path.splitext(os.path.basename(fileName[0]))[0]
        self.nom_fichier =str(os.path.basename(fileName[0]))
        self.extentionn = str(os.path.splitext(os.path.basename(fileName[0]))[1])
        #ici on prend le nom du fichier source avec ca extention et on applique un changement on changeon lextention de .ui a .py
        #pour pouvoir utilisé ce nom plus bas dans la fonction de la conversion
        replace = '.py'
        self.nouveau_nom_fichier = re.sub(self.extentionn, replace, self.nom_fichier)
        self.lineEdit_nom_resultat_conversion_saisi.setText(self.nouveau_nom_fichier)
        self.nom_resultat_conversion = fileName[0]
        print(self.nom_resultat_conversion,' ',self.nouveau_nom_fichier)

        if self.nom_resultat_conversion != "":
                self.lineEdit_nom_resultat_conversion.setText(fileName[0])
      
        
        #ici avec os.path.dirname(fileName[0]) on peu recupéré le chemin du fichier source copié
        #print(os.path.dirname(fileName[0]))
        
        #pour avoir le repertoire ou se trouve le fichier python de laplication en cours dexecution on utlise la commande suivante
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(self.BASE_DIR)
        
        self.target = os.path.dirname(fileName[0])+'/result_fichier'

      
        #os.getcwd() donne le repertoir ou le scrypte actuel est executé
        #avec la ligne suivante on crie un nouveau repertoire qui va contenir les fichiers de la conversion
        self.pathh=os.path.join(os.getcwd(), 'result_fichier')
        #avec os.mkdir(path) on crie le repertoire
        try:
                os.mkdir(self.pathh)
        except FileExistsError:
                print("Directory already exists")
        
        print('6eme ----------------------------------------------------------------------')
        print('1-self.target-------->', self.target)
        print('2-path=os.path.join(os.getcwd(), ''result_fichier'')---------->', self.pathh)
        print("3-self.nom_fichier------>",self.nom_fichier)
        print('4-repertoir source-------> ',fileName[0])
        print('5-self.pathsource = str(fileName[0])------->',str(fileName[0]))
        print("6-os.path.splitext(os.path.basename(fileName[0]))[0] ----->",os.path.splitext(os.path.basename(fileName[0]))[0])

        #dans la commande suivante on fait une copie du fichier a convertir par mesur de securité en sachan quon peu modifier le nom du fichier resultant de la conversion
        if shutil.copyfile(
                fileName[0],
                os.path.join(os.getcwd(), 'result_fichier', f'{self.nom_fichier_sans_extention}{self.extentionn}')):
                        copie_fichier = True 
        else:
                copie_fichier = False
        
        #on peu utilisé la variable copie_fichier comme control si loperation a reussi ou pas pour declencer dautre fonction par exemple 
        print(copie_fichier)
        
        
        #on peu verifier lexistance dun repertoire si on veux comme ceux ci
        #print('repertoire existe ou pas ? ',os.path.isdir('result_fichier'))



    def conversion_file(self):
            try:
                os.system('cmd /C "cd '+self.BASE_DIR+' & cd result_fichier & pyuic5 -x '+self.nom_fichier+' -o '+self.choix_nom_nouveau_fichier()+'')
                self.frame_7.show()
            except:
                print("erreur de conversion")
        

    def choix_nom_nouveau_fichier(self):
            if self.nouveau_nom_fichier == self.lineEdit_nom_resultat_conversion_saisi.text():
                return self.nouveau_nom_fichier
            else:
                self.nouveau_nom_fichier = self.lineEdit_nom_resultat_conversion_saisi.text()
                return self.lineEdit_nom_resultat_conversion_saisi.text()


    def ouvrir_fichier(self):
            try:
                os.system('cmd /C "cd '+self.BASE_DIR+' & cd result_fichier & '+self.nouveau_nom_fichier+'')
            except:
                print("erreur d'ouverture")












    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convertion UI à PY"))
        self.Button_fichier.setText(_translate("MainWindow", "Parcourir le fichier .ui"))
        self.label.setText(_translate("MainWindow", "Parcourir le fichier a convertir :"))
        self.label_2.setText(_translate("MainWindow", "Etape 01 :"))
        self.label_6.setText(_translate("MainWindow", "Vous pouvez changer le nom par défaut  ici :"))
        self.label_5.setText(_translate("MainWindow", "Etape 02 :"))
        self.pushButton_vallidation.setText(_translate("MainWindow", "Vallidez la conversion"))
        self.pushButton_ouvrir_fichier_converti.setText(_translate("MainWindow", "Ouvrir le Fichier Convertis"))
        self.label_7.setText(_translate("MainWindow", "Le fichier est converti :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
