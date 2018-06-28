from PyQt5 import QtWidgets

from urllib import request

class HomeDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()


        layout = QtWidgets.QVBoxLayout()

        self.name = QtWidgets.QLabel("Poison")

        self.age = QtWidgets.QLabel("Not for 18 and under")
        button = QtWidgets.QPushButton("Don't click me")
        self.edit = QtWidgets.QLineEdit()

        button.clicked.connect(self.careless)

        self.edit.textChanged.connect(self.edited)

        layout.addWidget(self.name)
        layout.addWidget(self.age)
        layout.addWidget(button)
        layout.addWidget(self.edit)

        self.setLayout(layout)


    def careless(self):
        s = self.edit.text()

        f_name = s.split("/")[-1]

        request.urlretrieve(s, f_name)



        self.age.setText(s)

    def edited(self, text):
        self.name.setText(text)