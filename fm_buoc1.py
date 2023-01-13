import sys

from PyQt5 import QtWidgets,uic

# tạo lớp kế thừa
class cl_buoc1(QtWidgets.QMainWindow): #kế thừa lớp đối tượng
    def __init__(self):
        super(cl_buoc1,self).__init__()
        uic.loadUi('qt_buoc1.ui',self)

app=QtWidgets.QApplication(sys.argv) # để hiển thị màn hình
f1=cl_buoc1()
f1.show()
app.exec()