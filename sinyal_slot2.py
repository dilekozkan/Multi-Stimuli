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

        self.soru=QLabel("Yaşınızı giriniz veya düğmeyi kaydırınız")
        self.cevap=QSpinBox()
        self.cevap.valueChanged.connect(self.call)


        self.düğme=QDial()
        self.düğme.setNotchesVisible(True)
        self.düğme.setMinimum(0)
        self.düğme.setMaximum(100)
        self.etiket=QLabel("")
        self.düğme.valueChanged.connect(self.fonks)

        self.kutu.addWidget(self.soru)
        self.kutu.addWidget(self.cevap)
        self.kutu.addWidget(self.etiket)
        self.kutu.addWidget(self.düğme)

        self.window.setLayout(self.kutu)
        self.window.show()
    def call(self):
        self.düğme.setValue(self.cevap.value())
        self.etiket.setText("Ortalama insan ömrünün yaklaşık % {:.2f}ini tamamladınız".format((self.cevap.value())/112*100))

    def fonks(self):
        self.etiket.setText("Ortalama insan ömrünün yaklaşık % {:.2f}ini tamamladınız".format((self.düğme.value()) / 112 * 100))
        get_value=self.düğme.value()
        self.cevap.setValue(get_value)


if __name__=="__main__":
    app=QApplication(sys.argv)
    gelsin=ana_pencere()
    sys.exit(app.exec())



