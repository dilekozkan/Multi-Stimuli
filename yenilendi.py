import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ana_pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()

        self.main_widget.setGeometry(450, 100, 900, 600)
        self.main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
        self.main_widget.setMinimumSize(900, 600)
        self.main_widget.setMaximumSize(900,600)

        self.stimodour1 = QCheckBox()
        self.stimodour2 = QCheckBox()
        self.stim2 = QCheckBox()
        self.stim3 = QCheckBox()
        self.stim4 = QCheckBox()
        
    
        self.stimodour1.toggled.connect(self.odour1experiment)
        self.stimodour2.toggled.connect(self.odour2experiment)
        self.stim2.toggled.connect(self.experiment2)
        self.stim3.toggled.connect(self.experiment3)
        self.stim4.toggled.connect(self.experiment4)
        
        

        self.apply=QPushButton("APPLY")
        self.apply.setFixedSize(100,28)
        self.cancel=QPushButton("CANCEL")
        self.cancel.setFixedSize(100, 28)


        self.apply.move(100,500)
        self.cancel.clicked.connect(self.def_cancel)


        self.kutu1 = QHBoxLayout()

        self.bos = QLabel("")
        self.tipler = QLabel("       Types of Stimulations")  # alignment'la ayarlanacak
        self.frekans = QLabel("   Frequency (Hz)")  # move yapınca pencereyi küçültürsen kayboluyor, yani hizalamıyor
        self.pattern = QLabel("  Pattern")

        self.kutu1.addWidget(self.tipler)
        self.kutu1.addWidget(self.frekans)
        self.kutu1.addWidget(self.pattern)

        self.kutu2 = QHBoxLayout()
        self.yenikutu=QHBoxLayout()
        self.yenikutu2= QHBoxLayout()

        self.label1 = QLabel("        Odours")
        #self.label1.move(800,500)
        self.odour1=QLabel("   Odour 1")
        self.odour2 = QLabel("   Odour 2")
        self.odour1buton1 = QDoubleSpinBox()

        self.odour1buton2 = QComboBox()


        self.odour2buton1 = QDoubleSpinBox()
        self.odour2buton2 = QComboBox()
        self.kutu2.addWidget(self.label1)
        self.yenikutu.addWidget(self.odour1)
        self.yenikutu.addWidget(self.odour1buton1)
        self.yenikutu.addWidget(self.odour1buton2)
        self.yenikutu2.addWidget(self.odour2)
        self.yenikutu2.addWidget(self.odour2buton1)
        self.yenikutu2.addWidget(self.odour2buton2)


        self.kutu3 = QHBoxLayout()
        self.label2 = QLabel("   Auditive")
        self.buton2 = QDoubleSpinBox()
        self.buton6 = QComboBox()
        self.kutu3.addWidget(self.label2)
        self.kutu3.addWidget(self.buton2)
        self.kutu3.addWidget(self.buton6)

        self.kutu4 = QHBoxLayout()
        self.label3 = QLabel("   Visual")
        self.buton3 = QDoubleSpinBox()
        self.buton7 = QComboBox()

        self.kutu4.addWidget(self.label3)
        self.kutu4.addWidget(self.buton3)
        self.kutu4.addWidget(self.buton7)

        self.kutu5 = QHBoxLayout()
        self.label4 = QLabel("   Whisker")
        self.buton4 = QDoubleSpinBox()
        self.buton8 = QComboBox()
        self.kutu5.addWidget(self.label4)
        self.kutu5.addWidget(self.buton4)
        self.kutu5.addWidget(self.buton8)

        self.odour1buton2.addItem(" ")
        self.odour1buton2.addItem("Binary")
        self.odour2buton2.addItem(" ")
        self.odour2buton2.addItem("Binary")
        self.buton6.addItem(" ")
        self.buton6.addItem("Binary")
        self.buton6.addItem("Sinuzoidal")
        self.buton7.addItem(" ")
        self.buton7.addItem("Binary")
        self.buton7.addItem("Sinuzoidal")
        self.buton8.addItem(" ")
        self.buton8.addItem("Binary")
        self.buton8.addItem("Sinuzoidal")
        self.bosluk = QLabel("")

        self.odour1buton1.valueChanged.connect(self.frequency_odour1)
        self.odour2buton1.valueChanged.connect(self.frequency_odour2)

        self.buton2.valueChanged.connect(self.frequency_stim2)
        self.buton3.valueChanged.connect(self.frequency_stim3)
        self.buton4.valueChanged.connect(self.frequency_stim4)


        self.odour1buton2.currentIndexChanged.connect(self.pattern_odour1)
        self.odour2buton2.currentIndexChanged.connect(self.pattern_odour2)
        self.buton6.currentIndexChanged.connect(self.pattern_stim2)
        self.buton7.currentIndexChanged.connect(self.pattern_stim3)
        self.buton8.currentIndexChanged.connect(self.pattern_stim4)

        self.information = QHBoxLayout()
        self.time_label = QLabel("       Time of Experiment(sec) = 20 ")
        self.frequency_label = QLabel("                          Number of Experiment ")
        self.frequency_experiment = QSpinBox()
        self.frequency_experiment.setFixedSize(100, 28)
        self.information.addWidget(self.time_label)
        self.information.addWidget(self.frequency_label)
        self.information.addWidget(self.frequency_experiment)



        self.form = QFormLayout()
        self.form.addRow(self.bosluk)
        self.form.addRow(self.kutu1)
        self.form.addRow(self.bosluk)

        self.form.addRow(self.bosluk)
        self.form.addRow(self.stimodour1, self.yenikutu)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.stimodour2, self.yenikutu2)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.stim2, self.kutu3)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.stim3, self.kutu4)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.stim4, self.kutu5)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.information)
        self.form.addRow(self.bosluk)



        self.main_widget.setLayout(self.form)

        self.main_widget.show()

    def odour1experiment(self):                            #bu kısımları deneyle entegre ettiğimde düzenleyeceğim
        if self.stimodour1.isChecked():
            pass
    def odour2experiment(self):                            #bu kısımları deneyle entegre ettiğimde düzenleyeceğim
        if self.stimodour2.isChecked():
            pass
    def experiment2(self):
        if self.stim2.isChecked():
            pass
    def experiment3(self):
        if self.stim3.isChecked():
            pass
    def experiment4(self):
        if self.stim4.isChecked():
            pass

    def frequency_odour1(self):
        frequency1=self.odour1buton1.value()

    def frequency_odour2(self):
        frequency1 = self.odour2buton1.value()

    def frequency_stim2(self):
        frequency2 = self.buton2.value()

    def frequency_stim3(self):
        frequency3 = self.buton3.value()

    def frequency_stim4(self):
        frequency4 = self.buton4.value()

    def pattern_odour1(self):
        if self.odour1buton2.currentText()=="Binary":
            pass

    def pattern_odour2(self):
        if self.odour2buton2.currentText() == "Binary":
            pass

    def pattern_stim2(self):
        if self.buton6.currentText()=="Binary":
            pass
        elif self.buton6.currentText()=="Sinuzoidal":
            pass

    def pattern_stim3(self):
        if self.buton7.currentText()=="Binary":
            pass
        elif self.buton7.currentText()=="Sinuzoidal":
            pass

    def pattern_stim4(self):
        if self.buton8.currentText()=="Binary":
            pass
        elif self.buton8.currentText()=="Sinuzoidal":
            pass

    def def_apply(self):
        pass
    def def_cancel(self):
        sys.exit(app.exec())


if __name__=="__main__":
    app=QApplication(sys.argv)
    created=Ana_pencere()
    sys.exit(app.exec())