import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, uic

dbfilename = 'assignment.dat'

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        d = ["Name", "Score", "Age"]

        Name = QLabel("Name: ")
        Age = QLabel("Age: ")
        Score = QLabel("Score: ")
        Amount = QLabel("Amount: ")
        Key = QLabel("Key: ")
        result = QLabel("Result: ")

        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()
        resultEdit = QTextEdit()
        Keybox = QComboBox()
        Keybox.addItems(d)

        addbutton = QPushButton("Add", self)
        delbutton = QPushButton("Del", self)
        findbutton = QPushButton("Find", self)
        incbutton = QPushButton("Inc", self)
        showbutton = QPushButton("show", self)

        addbutton.clicked.connect(self.add)
        delbutton.clicked.connect(self.delete)
        findbutton.clicked.connect(self.find)
        incbutton.clicked.connect(self.inc)
        showbutton.clicked.connect(self.showScoreDB)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(Name)
        hbox.addWidget(nameEdit)
        hbox.addWidget(Age)
        hbox.addWidget(ageEdit)
        hbox.addWidget(Score)
        hbox.addWidget(scoreEdit)
        hbox.addWidget(Amount)
        hbox.addWidget(amountEdit)
        hbox.addWidget(Key)
        hbox.addWidget(Keybox)

        hhbox = QHBoxLayout()
        hhbox.addWidget(addbutton)
        hhbox.addWidget(delbutton)
        hhbox.addWidget(findbutton)
        hhbox.addWidget(incbutton)
        hhbox.addWidget(showbutton)

        vbox.addLayout(hbox)
        vbox.addLayout(hhbox)

        vbox.addWidget(result)
        vbox.addWidget(resultEdit)

        self.setLayout(vbox)

        # self.c = Communicate()
        # self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return self.scoredb

        try:
            self.scoredb = pickle.load(fH)
        except:
            print("empty", dbfilename)
        else:
            print("open", dbfilename)
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        return self.scoredb

    def add(self, value):
        self.scoredb.append({'Name': value['name'], 'Age': int(value['age']), 'Score': int(value['score'])})
        print("aslkdjfa")
        return self.scoredb

    def delete(self, name):
        for i in range(len(self.scoredb)):
            for j in self.scoredb:
                if name == [i][name]:
                    self.scoredb.remove(j)
        return self.scoredb

    def find(self, name):
        res_list = []
        for i in range(len(self.scoredb)):
            if name == self.scoredb[i]['Name']:
                res_list.append(self.scoredb[i])

        return res_list

    def inc(self, name, amount):
        for i in range(len(self.scoredb)):
            if name == self.scoredb[i]['Name']:
                self.scoredb[i]['Score'] += int(amount)
        return self.scoredb


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





