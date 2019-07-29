import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ana_pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.window=QWidget()
        self.window.setWindowTitle("DENEMELER")
        self.window.setGeometry(200,200,400,400)

        self.kutu=QVBoxLayout()

        self.soru=QLabel("Bir sayı seçiniz:")

        self.buton1=QPushButton("60")
        self.buton2=QPushButton("70")
        self.slider = QSlider()
        self.isaret=QLabel(" Şu an %0 ")

        self.kutu.addWidget(self.soru)
        self.kutu.addWidget(self.buton1)
        self.kutu.addWidget(self.buton2)
        self.kutu.addWidget(self.slider)
        self.kutu.addWidget(self.isaret)

        self.buton1.clicked.connect(self.secim1)
        self.buton2.clicked.connect(self.secim2)


        self.window.setLayout(self.kutu)
        self.window.show()


    def secim1(self):

        self.isaret.setText("Yeni sayi: %60")
        self.slider.setValue(60)

    def secim2(self):
        self.slider.setValue(70)
        self.isaret.setText("Yeni sayi: %70")


if __name__=="__main__":
    app=QApplication(sys.argv)
    gelsin=ana_pencere()
    sys.exit(app.exec())



