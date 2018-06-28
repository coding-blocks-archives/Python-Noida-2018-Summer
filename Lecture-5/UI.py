from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

dia = QtWidgets.QDialog()

layout = QtWidgets.QVBoxLayout()

name = QtWidgets.QLabel("Poison")
age = QtWidgets.QLabel("Not for 18 and under")
b = QtWidgets.QPushButton("Don't click me")
l = QtWidgets.QLineEdit("What is in your mind")
d = QtWidgets.QDateEdit()

layout.addWidget(name)
layout.addWidget(b)
layout.addWidget(age)
layout.addWidget(l)
layout.addWidget(d)

dia.setLayout(layout)


dia.show()

app.exec_()





