import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGridLayout

app=QApplication(sys.argv)
main_widget=QWidget()

main_widget.setGeometry(450, 100, 900, 650)
main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
main_widget.setMinimumSize(900, 600)



stim1=QRadioButton()
stim2=QRadioButton()
stim3=QRadioButton()
stim4=QRadioButton()


kutu1=QHBoxLayout()

bos=QLabel("")
tipler=QLabel("    Types of Stimulations")
frekans=QLabel("   Frequency(Hz)")
pattern=QLabel("  Pattern")


kutu1.addWidget(tipler)
kutu1.addWidget(frekans)
kutu1.addWidget(pattern)


kutu2=QHBoxLayout()

label1=QLabel("Whisker")
buton1=QSpinBox()
buton5=QComboBox()
kutu2.addWidget(label1)
kutu2.addWidget(buton1)
kutu2.addWidget(buton5)

kutu3=QHBoxLayout()
label2=QLabel("Auditive")
buton2=QSpinBox()
buton6=QComboBox()
kutu3.addWidget(label2)
kutu3.addWidget(buton2)
kutu3.addWidget(buton6)

kutu4=QHBoxLayout()
label3=QLabel("Visual")
buton3=QSpinBox()
buton7=QComboBox()
kutu4.addWidget(label3)
kutu4.addWidget(buton3)
kutu4.addWidget(buton7)

kutu5=QHBoxLayout()
label4=QLabel("Odour")
buton4=QSpinBox()
buton8=QComboBox()
kutu5.addWidget(label4)
kutu5.addWidget(buton4)
kutu5.addWidget(buton8)




form=QFormLayout()

form.addRow(kutu1)
form.addRow(stim1, kutu2)
form.addRow(stim2, kutu3)
form.addRow(stim3, kutu4)
form.addRow(stim4, kutu5)





main_widget.setLayout(form)
main_widget.show()
sys.exit(app.exec())