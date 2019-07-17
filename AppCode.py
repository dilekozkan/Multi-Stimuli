import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

if "name" == __main__:
  application = QApplication(sys.argv)
  window = QWidget()
  Wİndow.setWindowTitle("Record EEG and Display")
  Window.show()
  sys.exit(application.exec())
