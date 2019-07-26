import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGridLayout

app=QApplication(sys.argv)
main_widget=QWidget()

main_widget.setGeometry(450, 100, 900, 600)
main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
main_widget.setMinimumSize(900, 600)



stim1=QRadioButton()
stim2=QRadioButton()
stim3=QRadioButton()
stim4=QRadioButton()


kutu1=QHBoxLayout()

bos=QLabel("")
tipler=QLabel("Types of Stimulations")
tipler.setAlignment(Qt.AlignLeft)
frekans=QLabel("   Frequency (Hz)")
pattern=QLabel("  Pattern")


kutu1.addWidget(tipler)
kutu1.addWidget(frekans)
kutu1.addWidget(pattern)


kutu2=QHBoxLayout()

label1=QLabel("   Whisker")
buton1=QDoubleSpinBox()
buton1.setFixedSize(200,25)
buton1.setAlignment(Qt.AlignLeft)
buton5=QComboBox()
buton5.setFixedSize(200,25)

kutu2.addWidget(label1)
kutu2.addWidget(buton1)
kutu2.addWidget(buton5)

kutu3=QHBoxLayout()
label2=QLabel("   Auditive")
buton2=QDoubleSpinBox()
buton6=QComboBox()
kutu3.addWidget(label2)
kutu3.addWidget(buton2)
kutu3.addWidget(buton6)

kutu4=QHBoxLayout()
label3=QLabel("   Visual")
buton3=QDoubleSpinBox()

buton7=QComboBox()



kutu4.addWidget(label3)
kutu4.addWidget(buton3)
kutu4.addWidget(buton7)

kutu5=QHBoxLayout()
label4=QLabel("   Odour")
buton4=QDoubleSpinBox()
buton8=QComboBox()
kutu5.addWidget(label4)
kutu5.addWidget(buton4)
kutu5.addWidget(buton8)

buton5.addItem(" ")
buton5.addItem("Binary")
buton5.addItem("Sinuzoidal")
buton6.addItem(" ")
buton6.addItem("Binary")
buton6.addItem("Sinuzoidal")
buton7.addItem(" ")
buton7.addItem("Binary")
buton7.addItem("Sinuzoidal")
buton8.addItem(" ")
buton8.addItem("Binary")
buton8.addItem("Sinuzoidal")

bosluk=QLabel("")

"""
sonra en alta eklenecek !


information=QHBoxLayout()
time_label=QLabel("       Time of Experiment(sec) = 20 ")
frequency_label=QLabel("                                Frequency of Experiment    ")
frequency_experiment=  QSpinBox()
frequency_experiment.setFixedSize(100,30)
information.addWidget(time_label)
information.addWidget(frequency_label)
information.addWidget(frequency_experiment)

"""




form=QFormLayout()
form.addRow(bosluk)
form.addRow(kutu1)
form.addRow(bosluk)
form.addRow(stim1, kutu2)
form.addRow(bosluk)
form.addRow(stim2, kutu3)
form.addRow(bosluk)
form.addRow(stim3, kutu4)
form.addRow(bosluk)
form.addRow(stim4, kutu5)
form.addRow(bosluk)
form.addRow(bosluk)



main_widget.setLayout(form)

main_widget.show()
sys.exit(app.exec())