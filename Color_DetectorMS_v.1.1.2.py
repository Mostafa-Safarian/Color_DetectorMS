#import the librarys
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw
import pyautogui as pg
import sys
from PyQt5.QtWidgets import QFileDialog
import sqlite3
import webbrowser
import tkinter as tk
from tkinter import ttk
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar


#login window
class LogInPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_EA = QtWidgets.QLabel(self.centralwidget)
        self.label_EA.setGeometry(QtCore.QRect(90, 160, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Sultan Adan 2Line")
        font.setPointSize(12)
        font.setBold(True)
        self.label_EA.setFont(font)
        self.label_EA.setObjectName("label_EA")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(93, 200, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Sultan Adan 2Line")
        font.setPointSize(12)
        font.setBold(True)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")
        self.lineEdit_EA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_EA.setGeometry(QtCore.QRect(230, 160, 241, 21))
        self.lineEdit_EA.setObjectName("lineEdit_EA")
        self.lineEdit_Pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Pass.setGeometry(QtCore.QRect(230, 200, 241, 21))
        self.lineEdit_Pass.setObjectName("lineEdit_Pass")
        self.label_LO = QtWidgets.QLabel(self.centralwidget)
        self.label_LO.setGeometry(QtCore.QRect(280, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Sultan Adan 2Line")
        font.setPointSize(12)
        font.setBold(True)
        self.label_LO.setFont(font)
        self.label_LO.setObjectName("label_LO")
        self.pushButton_LinkSigninPaga = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LinkSigninPaga.setGeometry(QtCore.QRect(30, 320, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_LinkSigninPaga.setFont(font)
        self.pushButton_LinkSigninPaga.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LinkSigninPaga.setStyleSheet("color:rgb(67, 158, 255)")
        self.pushButton_LinkSigninPaga.setFlat(True)
        self.pushButton_LinkSigninPaga.setObjectName("pushButton_LinkSigninPaga")
        self.pushButton_LinkSigninPaga.clicked.connect(self.SignIn)
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setGeometry(QtCore.QRect(270, 260, 75, 24))
        self.pushButton_Login.clicked.connect(self.check_password)
        font = QtGui.QFont()
        font.setFamily("Sultan Adan 2Line")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Login.setObjectName("pushButton_Login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_EA.setText(_translate("MainWindow", "Username:"))
        self.label_pass.setText(_translate("MainWindow", "Password:"))
        self.label_LO.setText(_translate("MainWindow", "Login "))
        self.pushButton_LinkSigninPaga.setText(_translate("MainWindow", "Create an account"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))

    #checking password and username funtion
    def check_password(self):
        self.db_connection = sqlite3.connect('C:/Color_DetectorMS/data/CDMSData')
        password = self.lineEdit_Pass.text()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT UserPassword FROM UserData")
        stored_password = cursor.fetchone()[0]
        self.db_connection = sqlite3.connect('C:/Color_DetectorMS/data/CDMSData')
        UserName = self.lineEdit_EA.text()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT UserName FROM UserData")
        stored_UserName = cursor.fetchone()[0]      
        if UserName == stored_UserName and password == stored_password:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                pg.alert("Welcome!")
        else:
            pg.alert("Error! Username or Password is false","Login")
    
    #close the databace funtion
    def closeEvent(self, event):
        self.db_connection.close()

    #open the Signin page funtion
    def SignIn(self):
           self.window = QtWidgets.QMainWindow()
           self.ui = SignInPage()
           self.ui.setupUi(self.window)
           self.window.show()




#Sigin window
class SignInPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_UserNameSignIN = QtWidgets.QLabel(self.centralwidget)
        self.label_UserNameSignIN.setGeometry(QtCore.QRect(80, 150, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_UserNameSignIN.setFont(font)
        self.label_UserNameSignIN.setObjectName("label_UserNameSignIN")
        self.label_PasswordSignIn = QtWidgets.QLabel(self.centralwidget)
        self.label_PasswordSignIn.setGeometry(QtCore.QRect(80, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_PasswordSignIn.setFont(font)
        self.label_PasswordSignIn.setObjectName("label_PasswordSignIn")
        self.lineEdit_UserNameSignIn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_UserNameSignIn.setGeometry(QtCore.QRect(180, 150, 191, 22))
        self.lineEdit_UserNameSignIn.setObjectName("lineEdit_UserNameSignIn")
        self.lineEdit_PasswordSignIn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PasswordSignIn.setGeometry(QtCore.QRect(180, 190, 191, 22))
        self.lineEdit_PasswordSignIn.setObjectName("lineEdit_PasswordSignIn")
        self.pushButton_SignIn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SignIn.setGeometry(QtCore.QRect(240, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_SignIn.setFont(font)
        self.pushButton_SignIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_SignIn.setObjectName("pushButton_SignIn")
        self.pushButton_SignIn.clicked.connect(self.SignInAdd)
        self.label_SignIn = QtWidgets.QLabel(self.centralwidget)
        self.label_SignIn.setGeometry(QtCore.QRect(250, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_SignIn.setFont(font)
        self.label_SignIn.setObjectName("label_SignIn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign In"))
        self.label_UserNameSignIN.setText(_translate("MainWindow", "Username:"))
        self.label_PasswordSignIn.setText(_translate("MainWindow", "Password:"))
        self.pushButton_SignIn.setText(_translate("MainWindow", "Sign in"))
        self.label_SignIn.setText(_translate("MainWindow", "Sign in"))

#add username and password to the databace(Sigin) funtion
    def SignInAdd(self):
        try:
           con=sqlite3.connect("C:\Color_DetectorMS\data\CDMSData")
           UserName=self.lineEdit_UserNameSignIn.text()
           UserPassword=self.lineEdit_PasswordSignIn.text()
           data=[UserPassword,UserName]
           result=con.execute("insert into UserData(UserPassword,UserName) values(?,?)",data)
           con.commit()
           self.lineEdit_UserNameSignIn.clear()
           self.lineEdit_PasswordSignIn.clear()
           self.window = QtWidgets.QMainWindow()
           self.ui = Ui_MainWindow()
           self.ui.setupUi(self.window)
           self.window.show()
           pg.alert("Welcome!","Sign in")
           
        except:
            pg.alert("Error","Sign in")
        con.close()


#orginal app window
class ProgressDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ProgressDialog, self).__init__(parent)
        self.setWindowTitle("Progress")
        self.setFixedSize(300, 100)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 240, 17)
        self.progressBar.setMaximum(100)  # Maximum value for the progress bar
        self.setModal(True)  # This makes the dialog modal

    def updateProgress(self, value):
        self.progressBar.setValue(value)

class Worker(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)  # Signal for progress updates
    finished = QtCore.pyqtSignal()  # Signal when work is done

    def __init__(self, file_name):
        super(Worker, self).__init__()
        self.file_name = file_name

    def run(self):
        image = Image.open(self.file_name)
        image = image.convert("RGB")
        border_image = Image.new("RGB", image.size)
        draw = ImageDraw.Draw(border_image)
        pixels = image.load()

        total_pixels = image.width * image.height
        pixel_count = 0

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                if (
                    x > 0 and x < image.width - 1 and y > 0 and y < image.height - 1
                    and (
                        pixels[x-1, y] != (r, g, b)
                        or pixels[x+1, y] != (r, g, b)
                        or pixels[x, y-1] != (r, g, b)
                        or pixels[x, y+1] != (r, g, b)
                    )
                ):
                    draw.line([(x-2, y-2), (x+2, y-2), (x+2, y+2), (x-2, y+2), (x-2, y-2)], fill=(0, 255, 0), width=4)

                pixel_count += 1
                # Update progress at every 1% change
                if pixel_count % (total_pixels // 100) == 0:
                    self.progress.emit(int((pixel_count / total_pixels) * 100))

        border_image.save(self.file_name)  # Save the processed image
        self.finished.emit()  # Emit finished signal when done
        image.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-2, 0, 1151, 651))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image.jpg"))
        self.label.setObjectName("label")
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(1070, 620, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(12)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.designer_label = QtWidgets.QLabel(self.centralwidget)
        self.designer_label.setGeometry(QtCore.QRect(10, 620, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(11)
        self.designer_label.setFont(font)
        self.designer_label.setObjectName("designer_label")
        self.guid_btn = QtWidgets.QPushButton(self.centralwidget)
        self.guid_btn.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.guid_btn.setFont(font)
        self.guid_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guid_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.guid_btn.setObjectName("guid_btn")
        self.guid_btn.clicked.connect(self.guide)
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setGeometry(QtCore.QRect(150, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.select_btn.setFont(font)
        self.select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.select_btn.setObjectName("select_btn")
        self.select_btn.clicked.connect(self.select_file)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 320, 291, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(310, 370, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(440, 370, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cu_btn.setGeometry(QtCore.QRect(120, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.cu_btn.setFont(font)
        self.cu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cu_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.cu_btn.setObjectName("cu_btn")
        self.cu_btn.clicked.connect(self.cu)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(20, 580, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit)
        self.cfu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cfu_btn.setGeometry(QtCore.QRect(920, 620, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.cfu_btn.setFont(font)
        self.cfu_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cfu_btn.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgb(0, 0, 0);")
        self.cfu_btn.setObjectName("cfu_btn")
        self.cfu_btn.clicked.connect(self.CheckForUpdates)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color_DetectorMS_v.1.1.2"))
        self.version_label.setText(_translate("MainWindow", "v.1.1.2"))
        self.designer_label.setText(_translate("MainWindow", "Designed by Mostafa Saffarian"))
        self.guid_btn.setText(_translate("MainWindow", "Guide"))
        self.select_btn.setText(_translate("MainWindow", "Select file"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.cu_btn.setText(_translate("MainWindow", "Contact us"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.cfu_btn.setText(_translate("MainWindow", "Check for updates"))

    # Exit button function
    def exit(self):
        QtWidgets.QApplication.quit()

    # "Update checking" button function
    def CheckForUpdates(self):
        pg.alert("No updates are available!")

    # Detect the color function
    def start(self):
        fileName = self.lineEdit.text()

        # Create and show the progress dialog
        self.progress_dialog = ProgressDialog()
        self.progress_dialog.show()

        # Start the worker thread
        self.worker = Worker(fileName)
        self.worker.progress.connect(self.progress_dialog.updateProgress)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self):
        self.progress_dialog.close()  # Close the dialog at the end
        pg.alert("Processing done!")

    # Select the file function
    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter('Images (*.png *.jpg)')
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.lineEdit.setText(file_path)

    # Cancel the app process
    def cancel(self):
        self.lineEdit.clear()

    # The function of having contact with us
    def cu(self):
        pg.alert("Ready to receive any criticism and suggestions", "Contact us")
        recipient_email = "saffarianmostafa@gmail.com"
        gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={recipient_email}"
        webbrowser.open(gmail_url)


    #the funtion of opening the guid window
    def guide(self):
    
        self.window = QtWidgets.QMainWindow()
        self.ui = guide_class()
        self.ui.setupUi2(self.window)
        self.window.show()

#guid window
class guide_class(object):
    def setupUi2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.guide_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.guide_label_1.setGeometry(QtCore.QRect(20, 20, 441, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.guide_label_1.setFont(font)
        self.guide_label_1.setObjectName("guide_label_1")
        self.guide1 = QtWidgets.QLabel(self.centralwidget)
        self.guide1.setGeometry(QtCore.QRect(30, 60, 541, 321))
        self.guide1.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgbrgb(208, 242, 255);")
        self.guide1.setText("")
        self.guide1.setPixmap(QtGui.QPixmap("guid1.png"))
        self.guide1.setObjectName("guide1")
        self.guide_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.guide_label_2.setGeometry(QtCore.QRect(640, 20, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.guide_label_2.setFont(font)
        self.guide_label_2.setObjectName("guide_label_2")
        self.guide2 = QtWidgets.QLabel(self.centralwidget)
        self.guide2.setGeometry(QtCore.QRect(650, 60, 541, 321))
        self.guide2.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgbrgb(208, 242, 255);")
        self.guide2.setText("")
        self.guide2.setPixmap(QtGui.QPixmap("guid3.png"))
        self.guide2.setObjectName("guide2")
        self.guide_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.guide_label_3.setGeometry(QtCore.QRect(320, 410, 431, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.guide_label_3.setFont(font)
        self.guide_label_3.setObjectName("guide_label_3")
        self.guide3 = QtWidgets.QLabel(self.centralwidget)
        self.guide3.setGeometry(QtCore.QRect(330, 450, 541, 321))
        self.guide3.setStyleSheet("background-color:rgb(110, 137, 255);\n"
"border-style: outset;\n"
"border-color:rgb(30, 79, 255);\n"
"border-width: 4px;\n"
"color:rgbrgb(208, 242, 255);")
        self.guide3.setText("")
        self.guide3.setPixmap(QtGui.QPixmap("guid2.png"))
        self.guide3.setObjectName("guide3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Guide", "Guide"))
        self.guide_label_1.setText(_translate("MainWindow", "1.Press the select file button to select the desired file."))
        self.guide_label_2.setText(_translate("MainWindow", "2.Select the desired file and then press open."))
        self.guide_label_3.setText(_translate("MainWindow", "3.Press the start button to start the operation."))         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LogInPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    
