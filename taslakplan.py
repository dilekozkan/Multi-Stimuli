import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app=QApplication(sys.argv)
main_widget=QWidget()

main_widget.setGeometry(450, 100, 1100, 800)
main_widget.setWindowTitle("MULTI-STIMULI PROCESS")



stimulation_types=QVBoxLayout()
label1=QLabel("Whisker")
label2=QLabel("Auditive")
label3=QLabel("Odour")
label4=QLabel("Visual")

stimulation_types.addWidget(label1)
stimulation_types.addWidget(label2)
stimulation_types.addWidget(label3)
stimulation_types.addWidget(label4)

stim_butonları=QVBoxLayout

stim1=QRadioButton()
stim2=QRadioButton()
stim3=QRadioButton()
stim4=QRadioButton()


secim_turleri=QHBoxLayout()

frekans=QLabel("Frequency(Hz)")
pattern=QLabel("Pattern")

secim_turleri.addWidget(frekans)
secim_turleri.addWidget(pattern)



frekans_butonlari=QVBoxLayout()

buton1=QSpinBox
buton2=QSpinBox
buton3=QSpinBox
buton4=QSpinBox


frekans_butonlari.addWidget(buton1)
frekans_butonlari.addWidget(buton2)
frekans_butonlari.addWidget(buton3)
frekans_butonlari.addWidget(buton4)



pattern_butonlari=QVBoxLayout()

buton5=QComboBox
buton6=QComboBox
buton7=QComboBox
buton8=QComboBox

pattern_butonlari.addWidget(buton5)
pattern_butonlari.addWidget(buton6)
pattern_butonlari.addWidget(buton7)
pattern_butonlari.addWidget(buton8)

buton5.clicked.connect(def buton 5)
burası böyle devam edecek......


yesno=QHBoxLayout()
yes_button=QPushButton("<font size = 5 color='green'>Apply</font>")
no_button=QPushButton("<font size = 5 color='red'> Cancel</font>")
yesno.addwidget(yes_button)
yesno.addwidget(no_button)

yes_button.clicked.connect(??)
no_button.clicked.connect(??)



main_widget.setLayout(??)

main_widget.show()

sys.exit(app.exec())


def stim1():

    şu sisteme bağlan


def stim2():

şu  sisteme bağlan

def stim3():

şu  sisteme bağlan

def stim4():

şu  sisteme bağlan

def buton 5():
    if sinuzoidal se
        şu fonks çağır şeklinde python dan çekeceğim veya burda
    tanımlayacağım
    elif binary :
    ....
    else:
    print("bu alan boş bırakılamaz!")

def diğer 6, 7, 8 buton için de aynı

def yes():
def no():
