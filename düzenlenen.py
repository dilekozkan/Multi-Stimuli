import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGridLayout

app=QApplication(sys.argv)
main_widget=QWidget()

main_widget.setGeometry(450, 100, 900, 650)
main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
main_widget.setMinimumSize(900, 600)

""""

#Burda yapmaya çalıştığım; altalta labeller yazacaktı,
solunda da radiobutonlar olacaktı, butonların başlığı olmayacaktı, onun yerine böyle yazayım demiştim

stimulation_types=QVBoxLayout()
label1=QLabel("Whisker")
label2=QLabel("Auditive")
label3=QLabel("Odour")
label4=QLabel("Visual")


stimulation_types.addWidget(label1)
stimulation_types.addWidget(label2)
stimulation_types.addWidget(label3)
stimulation_types.addWidget(label4)

#Burda horizontal bir şekilde alttaki seçimin başlığı olan labeller olacaktı

secim_turleri=QHBoxLayout()

frekans=QLabel("Frequency(Hz)")         #
pattern=QLabel("Pattern")
stim=QLabel("Types of Stimulation")

secim_turleri.addWidget(stim)
secim_turleri.addWidget(frekans)
secim_turleri.addWidget(pattern)
"""


stim_butonları=QVBoxLayout()    #üstte yoruma aldıklarım dizaynı bozunca ben de sayıyı eşitlemek için böyle yaptım


stim_tipleri=QLabel("Types of Stimulation")
stim1=QRadioButton("WHISKER")
stim2=QRadioButton("ODOUR")
stim3=QRadioButton("VISUAL")
stim4=QRadioButton("AUDUTIVE")

stim_butonları.addWidget(stim_tipleri)
stim_butonları.addWidget(stim1)
stim_butonları.addWidget(stim2)
stim_butonları.addWidget(stim3)
stim_butonları.addWidget(stim4)



frekans_butonlari=QVBoxLayout()              #üstte yoruma aldıklarım dizaynı bozunca ben de sayıyı eşitlemek için böyle yaptım

frekans=QLabel("FREQUENCY(Hz)")
buton1=QSpinBox()
buton2=QSpinBox()
buton3=QSpinBox()
buton4=QSpinBox()

frekans_butonlari.addWidget(frekans)
frekans_butonlari.addWidget(buton1)
frekans_butonlari.addWidget(buton2)
frekans_butonlari.addWidget(buton3)
frekans_butonlari.addWidget(buton4)

pattern_butonlari=QVBoxLayout()

pattern=QLabel("PATTERN")                    #üstte yoruma aldıklarım dizaynı bozunca ben de sayıyı eşitlemek için böyle yaptım
buton5=QComboBox()
buton6=QComboBox()
buton7=QComboBox()
buton8=QComboBox()

pattern_butonlari.addWidget(pattern)
pattern_butonlari.addWidget(buton5)
pattern_butonlari.addWidget(buton6)
pattern_butonlari.addWidget(buton7)
pattern_butonlari.addWidget(buton8)

yatay=QHBoxLayout()                    #gride mi yerleştirsem yoksa böyle tasalamaya mı çalışsam bilmiyorum ama ili türlü de olmuyor

#yatay.addLayout(secim_turleri)
yatay.addLayout(stim_butonları)
#yatay.addLayout(stimulation_types)
yatay.addLayout(frekans_butonlari)
yatay.addLayout(pattern_butonlari)


"""komple=QGridLayout()  # type: QGridLayout

#komple.addLayout(secim_turleri, ?,?)
komple.addLayout(stim_butonları, 1,1)
#komple.addLayout(stimulation_types, 1,2)
komple.addLayout(pattern_butonlari, 1,3)
komple.addLayout(frekans_butonlari, 1,4)"""


main_widget.setLayout(yatay)
main_widget.show()
sys.exit(app.exec())