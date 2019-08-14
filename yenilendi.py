import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import RPi.GPIO as GPIO
import time



class thread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        pass


class Ana_pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()

        self.main_widget.setGeometry(450, 100, 950, 800)
        self.main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
        self.main_widget.setFont((QFont("Amble", 11)))
        self.main_widget.setFixedSize(900, 600)
        # self.main_widget.setMinimumSize(900, 600)
        # self.main_widget.setMaximumSize(900, 600)

        self.stimodour1 = QCheckBox()
        self.stimodour2 = QCheckBox()
        self.stim2 = QCheckBox()
        self.stim3 = QCheckBox()
        self.stim4 = QCheckBox()

        self.stimodour1.toggled.connect(self.odour1experiment)  # DİKKAT!!!
        self.stimodour2.toggled.connect(self.odour2experiment)
        self.stim2.toggled.connect(self.experiment2)
        self.stim3.toggled.connect(self.experiment3)
        self.stim4.toggled.connect(self.experiment4)

        self.kutu1 = QHBoxLayout()

        self.bos = QLabel("")
        self.tipler = QLabel("       Types of Stimulations")  # alignment'la ayarlanacak

        self.tipler.setFont(QFont("Amble", 11, QFont.Bold))
        self.tipler.setAlignment(Qt.AlignLeft)
        self.frekans = QLabel("Frequency (Hz)")  # move yapınca pencereyi küçültürsen kayboluyor, yani hizalamıyor
        self.frekans.setFont(QFont("Amble", 11, QFont.Bold))
        self.frekans.setAlignment(Qt.AlignHCenter)
        self.pattern = QLabel("Pattern")
        self.pattern.setFont(QFont("Amble", 11, QFont.Bold))
        self.pattern.setAlignment(Qt.AlignCenter)
        self.initialise = QLabel("Start Time of Experiment ")
        self.initialise.setFont(QFont("Amble", 11, QFont.Bold))
        self.initialise.setAlignment(Qt.AlignRight)

        self.kutu1.addWidget(self.tipler)
        self.kutu1.addWidget(self.frekans)
        self.kutu1.addWidget(self.pattern)
        self.kutu1.addWidget(self.initialise)

        self.kutu2 = QHBoxLayout()
        self.yenikutu = QHBoxLayout()
        self.yenikutu2 = QHBoxLayout()

        self.odour1 = QLabel("   Odour 1")
        self.odour1.setFont(QFont("Amble", 11))
        self.odour2 = QLabel("   Odour 2")
        self.odour2.setFont(QFont("Amble", 11))
        self.odour1buton1 = QDoubleSpinBox()
        self.odour1buton2 = QComboBox()
        self.odour1buton3 = QDoubleSpinBox()
        self.startodour1 = self.odour1buton3.value()

        self.odour2buton1 = QDoubleSpinBox()
        self.odour2buton2 = QComboBox()
        self.odour2buton3 = QDoubleSpinBox()
        self.startodour2 = self.odour2buton3.value()

        self.yenikutu.addWidget(self.odour1)
        self.yenikutu.addWidget(self.odour1buton1)
        self.yenikutu.addWidget(self.odour1buton2)
        self.yenikutu.addWidget(self.odour1buton3)

        self.yenikutu2.addWidget(self.odour2)
        self.yenikutu2.addWidget(self.odour2buton1)
        self.yenikutu2.addWidget(self.odour2buton2)
        self.yenikutu2.addWidget(self.odour2buton3)

        self.kutu3 = QHBoxLayout()
        self.label2 = QLabel("   Whisker")
        self.label2.setFont(QFont("Amble", 11))
        self.buton2 = QDoubleSpinBox()
        self.buton6 = QComboBox()
        self.buton9 = QDoubleSpinBox()
        self.start_whisker = self.buton9.value()
        self.kutu3.addWidget(self.label2)
        self.kutu3.addWidget(self.buton2)
        self.kutu3.addWidget(self.buton6)
        self.kutu3.addWidget(self.buton9)


        self.kutu4 = QHBoxLayout()
        self.label3 = QLabel("   Visual")
        self.label3.setFont(QFont("Amble", 11))
        self.buton3 = QDoubleSpinBox()
        self.buton7 = QComboBox()
        self.buton10 = QDoubleSpinBox()
        self.start_visual = self.buton10.value()
        self.kutu4.addWidget(self.label3)
        self.kutu4.addWidget(self.buton3)
        self.kutu4.addWidget(self.buton7)
        self.kutu4.addWidget(self.buton10)

        self.kutu5 = QHBoxLayout()
        self.label4 = QLabel("   Auditory")
        self.label4.setFont(QFont("Amble", 11))
        self.buton4 = QDoubleSpinBox()
        self.buton8 = QComboBox()
        self.buton11 = QDoubleSpinBox()
        self.start_auditive = self.buton11.value()
        self.kutu5.addWidget(self.label4)
        self.kutu5.addWidget(self.buton4)
        self.kutu5.addWidget(self.buton8)
        self.kutu5.addWidget(self.buton11)

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

        self.information1 = QHBoxLayout()
        self.time_label = QLabel("        Time of Experiment (sec)")
        self.time_label.setFont(QFont("Amble", 11))
        self.time_label.setAlignment(Qt.AlignLeft)
        self.time_choose = QSpinBox()
        self.time_choose.setFixedSize(100, 25)
        self.time_choose.setValue(23)
        self.time_choose.setAlignment(Qt.AlignHCenter)
        self.information2 = QHBoxLayout()
        self.frequency_label = QLabel("        Number of Experiment : ")
        self.frequency_label.setFont(QFont("Amble", 11))
        self.frequency_label.setAlignment(Qt.AlignLeft)
        self.frequency_experiment = QSpinBox()
        self.frequency_experiment.setAlignment(Qt.AlignHCenter)
        self.frequency_experiment.setFixedSize(100, 25)
        self.numberofexperiment = 1
        self.frequency_experiment.setValue(self.numberofexperiment)

        self.information1.addWidget(self.time_label)
        self.information1.addWidget(self.time_choose)
        self.information2.addWidget(self.frequency_label)
        self.information2.addWidget(self.frequency_experiment)
        self.boxofcontrol = QHBoxLayout()
        self.boxofcontrol.setAlignment(Qt.AlignRight)

        self.start = QPushButton("START")
        self.start.setFixedSize(100, 28)
        self.cancel = QPushButton("CANCEL")
        self.cancel.setFixedSize(100, 28)
        self.cancel.clicked.connect(self.function_cancel)
        self.start.clicked.connect(self.function_start)
        self.boxofcontrol.addWidget(self.start)
        self.boxofcontrol.addWidget(self.cancel)

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
        self.form.addRow(self.bosluk)
        self.form.addRow(self.information1)
        self.form.addRow(self.information2)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.bosluk)
        self.form.addRow(self.boxofcontrol)

        self.main_widget.setLayout(self.form)
        self.main_widget.show()


        self.thread = thread()







        """self.ttl_out = 16  # TTL Output
        GPIO.setup(self.ttl_out, GPIO.IN)
        self.var1 = GPIO.input(self.ttl_out)"""
        self.valve1 = 3  # VALVE 1
        self.valve3 = 5  # VALVE 3
        self.valve2 = 7  # VALVE 2
        self.valve4 = 11  # VALVE 4
        self.valve5 = 13  # VALVE 5
        self.valve6 = 15  # VALVE 6
        self.input1 = 29
        self.input2 = 31  # şu an kullanılmıyor
        self.input3 = 33
        self.input4 = 35
        self.input5 = 37


    def odour1experiment(self):  # bu kısımları deneyle entegre ettiğimde düzenleyeceğim
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.valve1, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve2, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve3, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve4, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve5, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve6, GPIO.OUT)  # PWM pin set as output

        GPIO.output(self.valve1, GPIO.LOW)
        GPIO.output(self.valve2, GPIO.LOW)
        GPIO.output(self.valve4, GPIO.LOW)
        GPIO.output(self.valve5, GPIO.LOW)
        GPIO.output(self.valve3, GPIO.HIGH)
        GPIO.output(self.valve6, GPIO.HIGH)
        self.airTime = 20;  # 29.75
        self.odorTime = 1;
        self.sleepTime3 = 5;
        self.delayTime = 2;


    def odour2experiment(self):  # bu kısımları deneyle entegre ettiğimde düzenleyeceğim
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.valve1, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve2, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve3, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve4, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve5, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve6, GPIO.OUT)  # PWM pin set as output

        GPIO.output(self.valve1, GPIO.LOW)
        GPIO.output(self.valve2, GPIO.LOW)
        GPIO.output(self.valve4, GPIO.LOW)
        GPIO.output(self.valve5, GPIO.LOW)
        GPIO.output(self.valve3, GPIO.HIGH)
        GPIO.output(self.valve6, GPIO.HIGH)
        self.airTime = 20;  # 29.75
        self.odorTime = 1;
        self.sleepTime3 = 5;
        self.delayTime = 2;
        self.liste.append(self.odour2experiment)

    def experiment2(self):
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)
        if self.stim2.isChecked():
            pass

    def experiment3(self):
        if self.stim3.isChecked():
            pass

    def experiment4(self):
        if self.stim4.isChecked():
            pass

    def frequency_odour1(self):
        self.frequency1 = self.odour1buton1.value()

    def frequency_odour2(self):
        self.frequency1 = self.odour2buton1.value()

    def frequency_stim2(self):
        self.frequency2 = self.buton2.value()

    def frequency_stim3(self):
        self.frequency3 = self.buton3.value()

    def frequency_stim4(self):
        self.frequency4 = self.buton4.value()

    def pattern_odour1(self):
        if self.odour1buton2.currentText() == "Binary":
            pass

    def pattern_odour2(self):
        if self.odour2buton2.currentText() == "Binary":
            pass

    def pattern_stim2(self):
        if self.buton6.currentText() == "Binary":
            pass
        elif self.buton6.currentText() == "Sinuzoidal":
            pass

    def pattern_stim3(self):
        if self.buton7.currentText() == "Binary":
            pass
        elif self.buton7.currentText() == "Sinuzoidal":
            pass

    def pattern_stim4(self):
        if self.buton8.currentText() == "Binary":
            pass
        elif self.buton8.currentText() == "Sinuzoidal":
            pass

    def frequency_experiment(self):
        self.numberofexperiment = self.frequency_experiment.value()

    def function_start(self):
        pass



    """
    for i in range(1, self.numberofexperiment+1)

    """

    def function_cancel(self):
        print("geldi")
        if not self.thread.isRunning():
            self.cancel.setEnabled(True)
            self.thread.start()

        """!! self.apply.running=False

        GPIO.output(self.valve2, GPIO.LOW)
        GPIO.output(self.valve4, GPIO.LOW)
        GPIO.output(self.valve5, GPIO.LOW)
        GPIO.output(self.valve3, GPIO.HIGH)
        GPIO.output(self.valve6, GPIO.HIGH)

        GPIO.cleanup()  # cleanup all GPIO
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    created = Ana_pencere()
    sys.exit(app.exec())
