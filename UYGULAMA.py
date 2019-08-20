import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import RPi.GPIO as GPIO
import time

#THREAD CLASS  (PARALLEL PROGRAMMING)

class StimThread(QThread):
    def run(self):

        # Pin Definitons:
        self.valve1 = 3  # VALVE 1
        self.valve3 = 5  # VALVE 3
        self.valve2 = 7  # VALVE 2
        self.valve4 = 11  # VALVE 4
        self.valve5 = 13  # VALVE 5
        self.valve6 = 15  # VALVE 6
        self.pin_visual = 12
        self.pin_audio = 16
        self.pin_empty = 20  # DOES NOT EXIST NOW
        self.pin_whisker = 21

        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.valve1, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve2, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve3, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve4, GPIO.OUT)  # LED pin set as output
        GPIO.setup(self.valve5, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.valve6, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.pin_visual, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.pin_audio, GPIO.OUT)  # PWM pin set as output
        GPIO.setup(self.pin_whisker, GPIO.OUT)  # PWM pin set as output

        GPIO.output(self.valve1, GPIO.LOW)  # Default
        GPIO.output(self.valve2, GPIO.LOW)
        GPIO.output(self.valve4, GPIO.LOW)
        GPIO.output(self.valve5, GPIO.LOW)
        GPIO.output(self.valve3, GPIO.HIGH)
        GPIO.output(self.valve6, GPIO.HIGH)

        self.time_odour1 = 0   #timer of odour1 experiment's duration (second by second)
        self.time_odour2 = 0   #timer of odour2 experiment's duration (second by second)

        self.counter1 = 0  #counter of repetition odour1
        self.counter2 = 0  #counter of repetition odour2
        self.counter3 = 0  #counter of repetition whisker
        self.counter4 = 0  #counter of repetition auditory
        self.counter5 = 0  #counter of repetition visual

        #self.totaltime=delay+length+off (total time of one experiment)
        self.totaltime_odour1 = delay_odour1 + length_odour1 + offtime_odour1
        self.totaltime_odour2 = delay_odour2 + length_odour2 + offtime_odour2


        while mainWindow.running:
            if mainWindow.odour1_flag == 1 and self.counter1 < repetition_odour1:
                self.odour1()

            if mainWindow.odour2_flag == 1 and self.counter2 < repetition_odour2:
                self.odour2()

            time.sleep(1)
            if mainWindow.odour1_flag == 1 and repetition_odour1>0 and self.totaltime_odour1>0:
                self.time_odour1 += 1
            if mainWindow.odour2_flag == 1 and repetition_odour2>0 and self.totaltime_odour2>0:
                self.time_odour2 += 1

            if mainWindow.odour1_flag == 1 and self.time_odour1 == self.totaltime_odour1 and repetition_odour1>0 :
                self.counter1 += 1
                print("Time = ", self.time_odour1, "Odour1 Experiment Completed", self.counter1, "\n")
                self.time_odour1 = 0
                if self.counter1 == repetition_odour1:
                    mainWindow.odour1_flag = 0


            if mainWindow.odour2_flag == 1 and self.time_odour2 == self.totaltime_odour2 and repetition_odour2>0:
                self.counter2 += 1
                print("Time = ",self.time_odour2,"Odour2 Experiment Completed",self.counter2,"\n")
                self.time_odour2 = 0
                if self.counter2 == repetition_odour2:
                    mainWindow.odour2_flag = 0

            if mainWindow.odour1_flag == 0 and mainWindow.odour2_flag==0 and mainWindow.whisker_flag ==0 and mainWindow.auditory_flag==0 and mainWindow.visual_flag==0:
                mainWindow.function_cancel()
                GPIO.cleanup()    # cleanup all GPIO
                time.sleep(1)
                break



    def odour1(self):
        print("Duration of Odour1 Experiment: ", self.time_odour1, "\n")
        if 0 <= self.time_odour1 < delay_odour1:

            GPIO.output(self.valve1, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
            print("Time = ", self.time_odour1, " Odour1 in Delay\n")


        elif delay_odour1 <= self.time_odour1 < delay_odour1 + length_odour1:

            GPIO.output(self.valve1, GPIO.HIGH)  # Odour1 started
            GPIO.output(self.valve4, GPIO.HIGH)
            GPIO.output(self.valve5, GPIO.HIGH)
            GPIO.output(self.valve3, GPIO.LOW)
            GPIO.output(self.valve6, GPIO.LOW)
            print("Time =", self.time_odour1, " Odour1 in Stim\n")

        elif delay_odour1 + length_odour1 <= self.time_odour1 < self.totaltime_odour1:

            GPIO.output(self.valve1, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
            print("Time =", self.time_odour1, " Odour1 in OffTime\n")
    def odour2(self):
        print("Duration of Odour2 Experiment: ", self.time_odour2, "\n")
        if 0 <= self.time_odour2 < delay_odour2:

            GPIO.output(self.valve2, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
            print("Time= ", self.time_odour2, " Odour2 in Delay\n ")


        elif delay_odour2 <= self.time_odour2 < delay_odour2 + length_odour2:

            GPIO.output(self.valve2, GPIO.HIGH)  # Odour2 started
            GPIO.output(self.valve4, GPIO.HIGH)
            GPIO.output(self.valve5, GPIO.HIGH)
            GPIO.output(self.valve3, GPIO.LOW)
            GPIO.output(self.valve6, GPIO.LOW)

            print("Time= ", self.time_odour2, " Odour2 in Stim\n ")

        elif delay_odour2 + length_odour2 <= self.time_odour2 < self.totaltime_odour2:

            GPIO.output(self.valve2, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
            print("Time= ", self.time_odour2, " Odour2 in OffTime\n")

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()

        self.main_widget.setGeometry(450, 100, 950, 800)
        self.main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
        self.main_widget.setFont((QFont("Amble", 11)))
        self.main_widget.setFixedSize(1000, 650)
        #self.main_widget.setMinimumSize(900, 900)
        # self.main_widget.setMaximumSize(900, 600)

        # CREATING SELECTIONS...

        self.stimodour1 = QCheckBox()
        self.stimodour2 = QCheckBox()
        self.whisker = QCheckBox()
        self.auditory = QCheckBox()
        self.visual = QCheckBox()

        # CREATING GUI...

        self.titlebox = QHBoxLayout()
        self.gap = QLabel("")
        self.types = QLabel("Types of Stimulations")
        self.types.setFont(QFont("Amble", 11, QFont.Bold))
        self.types.setAlignment(Qt.AlignLeft)
        self.delay = QLabel("Delay")
        self.delay.setFont(QFont("Amble", 11, QFont.Bold))
        self.delay.setAlignment(Qt.AlignHCenter)
        self.stim_length = QLabel("Length of Stim")
        self.stim_length.setFont(QFont("Amble", 11, QFont.Bold))
        self.stim_length.setAlignment(Qt.AlignCenter)
        self.offtime=QLabel("Off Time")
        self.offtime.setFont(QFont("Amble", 11, QFont.Bold))
        self.offtime.setAlignment(Qt.AlignHCenter)
        self.frequency=QLabel("Frequency")
        self.frequency.setFont(QFont("Amble", 11, QFont.Bold))
        self.frequency.setAlignment(Qt.AlignHCenter)
        self.amplitude=QLabel("Amplitude")
        self.amplitude.setFont(QFont("Amble", 11, QFont.Bold))
        self.amplitude.setAlignment(Qt.AlignHCenter)
        self.repetition=QLabel("Repetition")
        self.repetition.setFont(QFont("Amble", 11, QFont.Bold))
        self.repetition.setAlignment(Qt.AlignHCenter)

        # CREATING GUI...

        self.titlebox.addWidget(self.types)
        self.titlebox.addWidget(self.delay)
        self.titlebox.addWidget(self.stim_length)
        self.titlebox.addWidget(self.offtime)
        self.titlebox.addWidget(self.frequency)
        self.titlebox.addWidget(self.amplitude)
        self.titlebox.addWidget(self.repetition)

        # CREATING GUI...

        self.boxodour1 = QHBoxLayout()
        self.odour1 = QLabel("   Odour 1")
        self.odour1.setFont(QFont("Amble", 11))
        self.odour2 = QLabel("   Odour 2")
        self.odour2.setFont(QFont("Amble", 11))
        self.odour1buton1 = QSpinBox()
        self.odour1buton2 = QSpinBox()
        self.odour1buton3 = QSpinBox()
        self.odour1buton4 = QSpinBox()
        self.odour1buton5 = QDoubleSpinBox()
        self.odour1buton6 = QSpinBox()
        self.odour1buton4.setEnabled(0)
        self.odour1buton5.setEnabled(0)

        self.boxodour1.addWidget(self.odour1)
        self.boxodour1.addWidget(self.odour1buton1)
        self.boxodour1.addWidget(self.odour1buton2)
        self.boxodour1.addWidget(self.odour1buton3)
        self.boxodour1.addWidget(self.odour1buton4)
        self.boxodour1.addWidget(self.odour1buton5)
        self.boxodour1.addWidget(self.odour1buton6)

        # CREATING GUI...

        self.odour2buton1 = QSpinBox()
        self.odour2buton2 = QSpinBox()
        self.odour2buton3 = QSpinBox()
        self.odour2buton4 = QSpinBox()
        self.odour2buton5 = QDoubleSpinBox()
        self.odour2buton6 = QSpinBox()
        self.odour2buton4.setEnabled(0)
        self.odour2buton5.setEnabled(0)


        self.boxodour2 = QHBoxLayout()
        self.boxodour2.addWidget(self.odour2)
        self.boxodour2.addWidget(self.odour2buton1)
        self.boxodour2.addWidget(self.odour2buton2)
        self.boxodour2.addWidget(self.odour2buton3)
        self.boxodour2.addWidget(self.odour2buton4)
        self.boxodour2.addWidget(self.odour2buton5)
        self.boxodour2.addWidget(self.odour2buton6)

        # CREATING GUI...

        self.boxwhisker = QHBoxLayout()
        self.label2 = QLabel("   Whisker")
        self.label2.setFont(QFont("Amble", 11))
        self.buton2 = QSpinBox()
        self.buton6 = QSpinBox()
        self.buton9 = QSpinBox()
        self.buton12 = QSpinBox()
        self.buton15 = QDoubleSpinBox()
        self.buton18= QSpinBox()


        self.boxwhisker.addWidget(self.label2)
        self.boxwhisker.addWidget(self.buton2)
        self.boxwhisker.addWidget(self.buton6)
        self.boxwhisker.addWidget(self.buton9)
        self.boxwhisker.addWidget(self.buton12)
        self.boxwhisker.addWidget(self.buton15)
        self.boxwhisker.addWidget(self.buton18)

        # CREATING GUI...

        self.box_auditory = QHBoxLayout()
        self.label3 = QLabel("   Auditory")
        self.label3.setFont(QFont("Amble", 11))
        self.buton3 = QSpinBox()
        self.buton7 = QSpinBox()
        self.buton10 = QSpinBox()
        self.buton13 = QSpinBox()
        self.buton16 = QDoubleSpinBox()
        self.buton19 = QSpinBox()


        self.box_auditory.addWidget(self.label3)
        self.box_auditory.addWidget(self.buton3)
        self.box_auditory.addWidget(self.buton7)
        self.box_auditory.addWidget(self.buton10)
        self.box_auditory.addWidget(self.buton13)
        self.box_auditory.addWidget(self.buton16)
        self.box_auditory.addWidget(self.buton19)

        # CREATING GUI...

        self.visual_box = QHBoxLayout()
        self.label4 = QLabel("   Visual")
        self.label4.setFont(QFont("Amble", 11))
        self.buton4 = QSpinBox()
        self.buton8 = QSpinBox()
        self.buton11 = QSpinBox()
        self.buton14 = QSpinBox()
        self.buton17 = QDoubleSpinBox()
        self.buton20 = QSpinBox()


        self.visual_box.addWidget(self.label4)
        self.visual_box.addWidget(self.buton4)
        self.visual_box.addWidget(self.buton8)
        self.visual_box.addWidget(self.buton11)
        self.visual_box.addWidget(self.buton14)
        self.visual_box.addWidget(self.buton17)
        self.visual_box.addWidget(self.buton20)

        # CREATING START-CANCEL BUTTONS

        self.boxofcontrol=QHBoxLayout()
        self.start = QPushButton("START")
        self.start.setFixedSize(100, 28)
        self.cancel = QPushButton("CANCEL")
        self.cancel.setFixedSize(100, 28)
        self.cancel.clicked.connect(self.function_cancel)
        self.start.clicked.connect(self.function_start)
        self.boxofcontrol.addWidget(self.start)
        self.boxofcontrol.addWidget(self.cancel)

        # LAYOUT of BOXES (RELATED TO GUI)

        self.form = QFormLayout()
        self.form.addRow(self.gap)
        self.form.addRow(self.titlebox)
        self.form.addRow(self.gap)
        self.form.addRow(self.stimodour1, self.boxodour1)
        self.form.addRow(self.gap)
        self.form.addRow(self.stimodour2, self.boxodour2)
        self.form.addRow(self.gap)
        self.form.addRow(self.whisker, self.boxwhisker)
        self.form.addRow(self.gap)
        self.form.addRow(self.visual, self.box_auditory)
        self.form.addRow(self.gap)
        self.form.addRow(self.auditory, self.visual_box)
        self.form.addRow(self.gap)
        self.form.addRow(self.gap)
        self.form.addRow(self.gap)
        self.form.addRow(self.gap)
        self.form.addRow(self.boxofcontrol)
        self.main_widget.setLayout(self.form)
        self.main_widget.show()



        # THE MOST IMPORTANT PART: START, THREAD AND CANCEL !

    def function_start(self):

        #CHECK THE SELECTIONS  AND  ASSIGNMENT OF USER'S VALUES

        self.running = 1  # FLAG FOR THREAD RUN

        self.odour1_flag=0
        self.odour2_flag=0
        self.whisker_flag=0
        self.auditory_flag=0
        self.visual_flag=0

        if self.stimodour1.isChecked():
            self.odour1_flag = 1

        if self.stimodour2.isChecked():
            self.odour2_flag = 1

        if self.whisker.isChecked():
            self.whisker_flag = 1
        if self.auditory.isChecked():
            self.auditory_flag = 1
        if self.visual.isChecked():
            self.visual_flag = 1


        global delay_odour1, length_odour1, offtime_odour1, repetition_odour1
        delay_odour1 = self.odour1buton1.value()
        length_odour1 = self.odour1buton2.value()
        offtime_odour1 = self.odour1buton3.value()
        repetition_odour1 = self.odour1buton6.value()

        global delay_odour2, length_odour2, offtime_odour2, repetition_odour2
        delay_odour2 = self.odour2buton1.value()
        length_odour2 = self.odour2buton2.value()
        offtime_odour2 = self.odour2buton3.value()
        repetition_odour2 = self.odour2buton6.value()

        global delay_whisker, length_whisker, offtime_whisker,frequency_whisker,amplitude_whisker, repetition_whisker
        delay_whisker = self.buton2.value()
        length_whisker = self.buton6.value()
        offtime_whisker = self.buton9.value()
        frequency_whisker = self.buton12.value()
        amplitude_whisker = self.buton15.value()
        repetition_whisker = self.buton18.value()

        global delay_auditory, length_auditory, offtime_auditory, frequency_auditory, amplitude_auditory, repetition_auditory
        delay_auditory = self.buton3.value()
        length_auditory = self.buton7.value()
        offtime_auditory = self.buton10.value()
        frequency_auditory = self.buton13.value()
        amplitude_auditory = self.buton16.value()
        repetition_auditory = self.buton19.value()

        global delay_visual, length_visual, offtime_visual, frequency_visual, amplitude_visual, repetition_visual
        delay_visual = self.buton4.value()
        length_visual = self.buton8.value()
        offtime_visual = self.buton11.value()
        frequency_visual = self.buton14.value()
        amplitude_visual = self.buton17.value()
        repetition_visual = self.buton20.value()

        #MAKE DISABLED OF SELECTIONS

        self.stimodour1.setEnabled(0)
        self.stimodour2.setEnabled(0)
        self.whisker.setEnabled(0)
        self.visual.setEnabled(0)
        self.auditory.setEnabled(0)

        #START OF EXPERIMENT

        self.stimThread = StimThread()
        self.stimThread.start()


    def function_cancel(self):

        # MAKE ENABLED OF SELECTIONS

        self.stimodour1.setEnabled(1)
        self.stimodour2.setEnabled(1)
        self.whisker.setEnabled(1)
        self.visual.setEnabled(1)
        self.auditory.setEnabled(1)

        global running
        self.running=0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow= MainWindow()
    sys.exit(app.exec())

