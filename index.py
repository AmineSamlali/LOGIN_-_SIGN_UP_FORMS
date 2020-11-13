from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
import source_rc
from os import path
import datetime
import sqlite3
import random

"""
Program programmer : "Amine Samlali"
mail : samlaliamine2@gmail.com
number phone = '212 619135651'
Donation On PayPal : https://paypal.me/AmineSamlali
"""
ui_sys,_ = loadUiType('system.ui')
ui,_ = loadUiType('Main.ui')
ui_Login,_ = loadUiType('Login.ui')



class MainAppLogin(QMainWindow , ui_Login):
    def __init__(self , parent=None):
        super(MainAppLogin , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Connection()
    def Login_app(self):
        try:
            username = self.lineEdit.text()
            password = self.lineEdit_3.text()
            conn = sqlite3.connect('Elec.db')
            c = conn.cursor()
            c.execute(f'''SELECT * FROM accounts WHERE username="{username}" ''')
            login_db = list(c.fetchone())
            if len(username)  == 0 or len(password)  == 0:
                QMessageBox.warning(self, 'Error', "Please Enter True Values")
            elif username == 'username':
                pass
            elif username != 'username':
                if login_db[1]  == username and password == login_db[3]:
                    QMessageBox.information(self , 'Error' ,  f'WELCOME BACK {username}')
                else:
                    QMessageBox.warning(self,'Error' , 'username Or Password Incorrect')

        except Exception:
            QMessageBox.warning( self , 'Error', "Please Enter True Values")

    def Connection(self):
            # handle Connetion sys

            self.pushButton.clicked.connect(self.Login_app)


class MainApp(QMainWindow , ui ):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connection()

    def send_code(self):
        global code
        code  = random.randrange(1000,2000)
        print(f'The Verification Code is : {code} ')
    def signUp(self):
        global code
        conn = sqlite3.connect('Elec.db')
        c = conn.cursor()
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password1 = self.lineEdit_3.text()
        password2 = self.lineEdit_4.text()
        check_box = self.checkBox.isChecked()
        code_very = self.lineEdit_5.text()

        c.execute('''CREATE TABLE  IF NOT EXISTS accounts
                     (user_id INTEGER NOT NULL PRIMARY KEY,username text, email text, password text)''')

        if len(username) == 0 or len(email) == 0 or len(password1) == 0 or len(password2) == 0 or  len(code_very) == 0:
            QMessageBox.warning(self,"Error" ,  'Please Don\'t Enter  Empty information\'s')
        else:
            if '@' in email:
                if len(username) >= 8:
                    if len(password1) >= 8:
                        if password1 == password2:
                            if password1 != username or password2 != username:
                                if str(code) == str(code_very):
                                    if check_box:
                                        emty_list = []
                                        for i  in c.execute(''' SELECT username FROM accounts'''):
                                            username_db  = i[0]
                                            emty_list.append(username_db)
                                        if username in emty_list:
                                            QMessageBox.warning(self , 'Error' ,  'This username is Already Taken')
                                        else:
                                            c.execute(f''' INSERT INTO accounts (  username ,email , password ) values(  "{username}"  , "{email}"  , "{password1}")''')
                                            conn.commit()
                                            QMessageBox.information(self , 'Done'  , 'Your Account is been registered  ')
                                            self.lineEdit.setText('')
                                            self.lineEdit_2.setText('')
                                            self.lineEdit_3.setText('')
                                            self.lineEdit_4.setText('')
                                            self.checkBox.setChecked(False)
                                            self.lineEdit_5.setText('')
                                            code = random.random()


                                    else:

                                        QMessageBox.warning(self, 'Error', 'Please Confirm Check Box ')
                                else:
                                    QMessageBox.warning(self, 'Error', 'Please Confirm The code ')
                            else:
                                QMessageBox.warning(self,  'Error' , 'The username very similar to password Please Try Agin ! ')
                        else:
                            QMessageBox.warning(self, 'Error', 'Enter The Same Password ')
                    else:
                        QMessageBox.warning(self, 'Error', 'Password Must Contain At Least 8 Characters ')
                else:
                    QMessageBox.warning(self , 'Error' ,  'Username Must Contain At Least 8 Characters ')

                #  Handel other Information's
            else:
                QMessageBox.warning(self , 'Error', 'Please Enter True Email')



        conn.close()

    def connection(self):
        self.pushButton.clicked.connect(self.signUp)
        self.pushButton_2.clicked.connect(self.send_code)


def main_login():
    app = QApplication(sys.argv)
    window = MainAppLogin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main_login()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
