import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ana_pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.window=QWidget()
        self.window.setWindowTitle("DENEMELER")
        self.window.setGeometry(200,200,400,400)
        self.layout = QVBoxLayout()
        self.l1 = QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.l1)
        self.sp = QSpinBox()
        self.sp.setValue(20)
        self.etiket = QLabel("")


        self.layout.addWidget(self.sp)
        self.layout.addWidget(self.etiket)

        self.sp.valueChanged.connect(self.valuechange)
        self.window.setLayout(self.layout)
        self.window.show()

    def valuechange(self):
        self.etiket.setText(str(self.sp.value()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    gelsin=ana_pencere()
    sys.exit(app.exec())

