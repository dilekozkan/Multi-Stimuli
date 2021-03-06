import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSpinBox, QDoubleSpinBox, QCheckBox, QLabel, \
    QFormLayout, QPushButton
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QFont
import matplotlib as mpl
from itertools import zip_longest
import csv
mpl.use("QT5Agg")
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
from datetime import datetime

class Whisker_Thread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        self.pin_whisker = 21  # PWM pin set as output
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_whisker, GPIO.OUT)  # PWM pin set as output

        self.time_whisker = 0  # timer of whisker experiment's duration
        self.counter3 = 0  # counter of repetition whisker

        # self.totaltime=delay+length+off (total time of one experiment)


        while mW.running_whisker:
            if mW.whisker_flag == 1 and self.counter3 < mW.repetition_whisker:
                self.whisker()
                time.sleep(1)
            if mW.whisker_flag == 1 and mW.repetition_whisker > 0 and mW.totaltime_whisker > 0:
                self.time_whisker += 1
                print("Time of Whisker Experiment = {}.".format(self.time_whisker),"Status:", GPIO.input(self.pin_whisker), "\n")

            if mW.whisker_flag == 1 and self.time_whisker == mW.totaltime_whisker and mW.repetition_whisker > 0:
                self.counter3 += 1
                print("Duration of Whisker Experiment = ", self.time_whisker*self.counter3, "Whisker Experiment: {} Completed".format(self.counter3), "\n")
                self.time_whisker = 0
                if self.counter3 == mW.repetition_whisker:
                    mW.whisker_flag = 0

    def whisker(self):
        if 0 <= self.time_whisker < mW.delay_whisker:

            GPIO.output(self.pin_whisker, GPIO.LOW)

        elif mW.delay_whisker <= self.time_whisker < mW.delay_whisker + mW.length_whisker:

            GPIO.output(self.pin_whisker, GPIO.HIGH)  # Whisker started

        elif mW.delay_whisker + mW.length_whisker <= self.time_whisker < mW.totaltime_whisker:

            GPIO.output(self.pin_whisker, GPIO.LOW)
        mW.data_whisker.append(GPIO.input(self.pin_whisker))


class General_Thread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        # Pin Definitons:
        Pin_List = [3, 5, 7, 11, 13, 15, 12, 16, 21]

        self.valve1 = 3  # VALVE 1 LED pin set as output for odour1
        self.valve3 = 5  # VALVE 3 PWM pin set as output
        self.valve2 = 7  # VALVE 2 PWM pin set as output for odour2
        self.valve4 = 11  # VALVE 4 LED pin set as output
        self.valve5 = 13  # VALVE 5 PWM pin set as output
        self.valve6 = 15  # VALVE 6 PWM pin set as output
        self.pin_visual = 12  # PWM pin set as output
        self.pin_audio = 16  # PWM pin set as output
        self.pin_empty = 20  # DOES NOT EXIST NOW

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

        # Pin Low-High

        GPIO.output(self.valve1, GPIO.LOW)  # Default
        GPIO.output(self.valve2, GPIO.LOW)
        GPIO.output(self.valve4, GPIO.LOW)
        GPIO.output(self.valve5, GPIO.LOW)
        GPIO.output(self.valve3, GPIO.HIGH)
        GPIO.output(self.valve6, GPIO.HIGH)

        self.time_odour1 = 0  # timer of odour1 experiment's duration (second by second)
        self.time_odour2 = 0  # timer of odour2 experiment's duration (second by second)
        self.time_auditory=0    # timer of auditory experiment's duration (second by second)
        self.counter1 = 0  # counter of repetition odour1
        self.counter2 = 0  # counter of repetition odour2

        self.counter4 = 0  # counter of repetition auditory
        self.counter5 = 0  # counter of repetition visual

        # self.totaltime=delay+length+off (total time of one experiment)

        while mW.running:
            if mW.odour1_flag == 1 and self.counter1 < mW.repetition_odour1:
                self.odour1()
            if mW.odour2_flag == 1 and self.counter2 < mW.repetition_odour2:
                self.odour2()
            if mW.auditory_flag ==1 and self.counter4 < mW.repetition_auditory:
                self.auditory()
            if mW.visual_flag ==1 and self.counter5 < mW.repetition_visual:
                self.visual()
                mW.visual_flag=0

            time.sleep(1)
            if mW.odour1_flag == 1 and mW.repetition_odour1 > 0 and mW.totaltime_odour1 > 0:
                self.time_odour1 += 1
                print("Time of Odour1 = {}.".format(self.time_odour1), "Status:", GPIO.input(self.valve1),"\n")
            if mW.odour2_flag == 1 and mW.repetition_odour2 > 0 and mW.totaltime_odour2 > 0:
                self.time_odour2 += 1
                print("Time of Odour2 = {}.".format(self.time_odour2),"Status:", GPIO.input(self.valve2), "\n")
            if mW.auditory_flag == 1 and mW.repetition_auditory>0 and mW.totaltime_auditory>0:
                self.time_auditory += 1
                print("Time of Auditory = {}.".format(self.time_auditory), "Status:", GPIO.input(self.pin_audio),"\n")

            if mW.odour1_flag == 1 and self.time_odour1 == mW.totaltime_odour1 and mW.repetition_odour1 > 0:
                self.counter1 += 1
                print("Duration of Odour1= ", self.time_odour1*self.counter1, "Odour1 Experiment: {} Completed".format(self.counter1), "\n")
                self.time_odour1 = 0
                if self.counter1 == mW.repetition_odour1:
                    mW.odour1_flag = 0

            if mW.odour2_flag == 1 and self.time_odour2 == mW.totaltime_odour2 and mW.repetition_odour2 > 0:
                self.counter2 += 1
                print("Duration of Odour2 = ", self.time_odour2*self.counter2, "Odour2 Experiment: {} Completed".format(self.counter2), "\n")
                self.time_odour2 = 0
                if self.counter2 == mW.repetition_odour2:
                    mW.odour2_flag = 0
            if mW.auditory_flag == 1 and self.time_auditory == mW.totaltime_auditory and mW.repetition_auditory > 0:
                self.counter4 += 1
                print("Duration of Auditory Experiment= ", self.time_auditory*self.counter4, "Auditory Experiment: {} Completed".format(self.counter4), "\n")
                self.time_auditory = 0
                if self.counter4 == mW.repetition_auditory:
                    mW.auditory_flag = 0
            if mW.odour1_flag == 0 and mW.odour2_flag == 0 and mW.whisker_flag == 0 and mW.auditory_flag == 0 and mW.visual_flag == 0:
                mW.finished_signal.emit(mW.data_valve1, mW.data_valve2, mW.data_whisker)
                mW.creating_csv()
                GPIO.cleanup()  # cleanup all GPIO
                mW.function_cancel()
                time.sleep(1)
                break

    def odour1(self):

        if 0 <= self.time_odour1 < mW.delay_odour1:

            GPIO.output(self.valve1, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)

        elif mW.delay_odour1 <= self.time_odour1 < mW.delay_odour1 + mW.length_odour1:

            GPIO.output(self.valve1, GPIO.HIGH)  # Odour1 started
            GPIO.output(self.valve4, GPIO.HIGH)
            GPIO.output(self.valve5, GPIO.HIGH)
            GPIO.output(self.valve3, GPIO.LOW)
            GPIO.output(self.valve6, GPIO.LOW)

        elif mW.delay_odour1 + mW.length_odour1 <= self.time_odour1 < mW.totaltime_odour1:

            GPIO.output(self.valve1, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
        mW.data_valve1.append(GPIO.input(self.valve1))   # appending pin status to array of odour1's

    def odour2(self):

        if 0 <= self.time_odour2 < mW.delay_odour2:

            GPIO.output(self.valve2, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)

        elif mW.delay_odour2 <= self.time_odour2 < mW.delay_odour2 + mW.length_odour2:

            GPIO.output(self.valve2, GPIO.HIGH)  # Odour2 started
            GPIO.output(self.valve4, GPIO.HIGH)
            GPIO.output(self.valve5, GPIO.HIGH)
            GPIO.output(self.valve3, GPIO.LOW)
            GPIO.output(self.valve6, GPIO.LOW)

        elif mW.delay_odour2 + mW.length_odour2 <= self.time_odour2 < mW.totaltime_odour2:

            GPIO.output(self.valve2, GPIO.LOW)
            GPIO.output(self.valve4, GPIO.LOW)
            GPIO.output(self.valve5, GPIO.LOW)
            GPIO.output(self.valve3, GPIO.HIGH)
            GPIO.output(self.valve6, GPIO.HIGH)
        mW.data_valve2.append(GPIO.input(self.valve2))  # appending pin status to array of odour2's
    def auditory(self):

        if 0<= self.time_auditory <mW.delay_auditory:
            GPIO.output(self.pin_auditory, GPIO.LOW)
        elif mW.delay_auditory <= self.time_auditory < mW.delay_auditory + mW.length_auditory:

            GPIO.output(self.pin_auditory, GPIO.HIGH)  # Auditive started

        elif mW.delay_auditory + mW.length_auditory <= self.time_auditory < mW.totaltime_auditory:

            GPIO.output(self.pin_auditory, GPIO.LOW)
        mW.data_auditory.append(GPIO.input(self.pin_auditory))
    def visual(self):
        pass


class MainWindow(QWidget):
    finished_signal = pyqtSignal(list,list,list)

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.main_widget.setGeometry(450, 100, 950, 800)
        self.main_widget.setWindowTitle("MULTI-STIMULI PROCESS")
        self.main_widget.setFont((QFont("Amble", 11)))
        self.main_widget.setFixedSize(1000, 650)
        # self.main_widget.setMinimumSize(900, 900)
        # self.main_widget.setMaximumSize(900, 600)

        # CREATING SELECTIONS...

        self.stimodour1 = QCheckBox()
        self.stimodour2 = QCheckBox()
        self.whisker = QCheckBox()
        self.auditory = QCheckBox()
        self.visual = QCheckBox()
        self.check_list = [self.stimodour1, self.stimodour2, self.whisker, self.auditory, self.visual]
        self.odour1_flag = 0  # Creating check flag for experiments
        self.odour2_flag = 0
        self.whisker_flag = 0
        self.auditory_flag = 0
        self.visual_flag = 0
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
        self.offtime = QLabel("Off Time")
        self.offtime.setFont(QFont("Amble", 11, QFont.Bold))
        self.offtime.setAlignment(Qt.AlignHCenter)
        self.frequency = QLabel("Frequency")
        self.frequency.setFont(QFont("Amble", 11, QFont.Bold))
        self.frequency.setAlignment(Qt.AlignHCenter)
        self.amplitude = QLabel("Amplitude")
        self.amplitude.setFont(QFont("Amble", 11, QFont.Bold))
        self.amplitude.setAlignment(Qt.AlignHCenter)
        self.repetition = QLabel("Repetition")
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
        self.buton18 = QSpinBox()

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

        self.butonlist = [self.odour1buton1, self.odour1buton2, self.odour1buton3, self.odour1buton6,
                          self.odour2buton1, self.odour2buton2, self.odour2buton3, self.odour2buton6,
                          self.buton2, self.buton6, self.buton9, self.buton12, self.buton15, self.buton18,
                          self.buton3, self.buton7, self.buton10, self.buton13, self.buton16, self.buton19,
                          self.buton4, self.buton8, self.buton11, self.buton14, self.buton17, self.buton20]

        self.visual_box.addWidget(self.label4)
        self.visual_box.addWidget(self.buton4)
        self.visual_box.addWidget(self.buton8)
        self.visual_box.addWidget(self.buton11)
        self.visual_box.addWidget(self.buton14)
        self.visual_box.addWidget(self.buton17)
        self.visual_box.addWidget(self.buton20)

        # CREATING START-CANCEL BUTTONS

        self.boxofcontrol = QHBoxLayout()
        self.start = QPushButton("START")
        self.start.setFixedSize(100, 28)
        self.cancel = QPushButton("CANCEL")
        self.cancel.setFixedSize(100, 28)
        self.cancel.clicked.connect(self.click_cancel)
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
        self.finished_signal.connect(self.plotting_figure)


        self.main_widget.show()

        # THE MOST IMPORTANT PART: START, THREAD AND CANCEL !

    def function_start(self):

        self.running = 1  # FLAG FOR General_THREAD RUN
        self.running_whisker = 1  # FLAG FOR Whisker_THREAD RUN
        GPIO.setwarnings(False)
        self.flag_control()     #Flag of selections control
        self.get_value()        #assign value which received from user
        self.repetition_control()
        self.set_unabled()  # MAKE DISABLED OF SELECTIONS
        self.data_valve1, self.data_valve2, self.data_whisker=[0], [0], [0]
        self.data_auditory, self.data_visual =  [0], [0]  #collecting Rpi's pin status in list
        # START OF EXPERIMENT

        self.general_thread = General_Thread()
        self.general_thread.start()
        self.whisker_thread = Whisker_Thread()
        self.whisker_thread.start()

    def flag_control(self):

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

    def get_value(self):
        self.delay_odour1 = self.odour1buton1.value()  # Getting values from user's selections
        self.length_odour1 = self.odour1buton2.value()
        self.offtime_odour1 = self.odour1buton3.value()
        self.repetition_odour1 = self.odour1buton6.value()

        self.delay_odour2 = self.odour2buton1.value()  # Getting values from user's selections
        self.length_odour2 = self.odour2buton2.value()
        self.offtime_odour2 = self.odour2buton3.value()
        self.repetition_odour2 = self.odour2buton6.value()

        self.delay_whisker = self.buton2.value()  # Getting values from user's selections
        self.length_whisker = self.buton6.value()
        self.offtime_whisker = self.buton9.value()
        self.frequency_whisker = self.buton12.value()
        self.amplitude_whisker = self.buton15.value()
        self.repetition_whisker = self.buton18.value()

        self.delay_auditory = self.buton3.value()  # Getting values from user's selections
        self.length_auditory = self.buton7.value()
        self.offtime_auditory = self.buton10.value()
        self.frequency_auditory = self.buton13.value()
        self.amplitude_auditory = self.buton16.value()
        self.repetition_auditory = self.buton19.value()

        self.delay_visual = self.buton4.value()  # Getting values from user's selections
        self.length_visual = self.buton8.value()
        self.offtime_visual = self.buton11.value()
        self.frequency_visual = self.buton14.value()
        self.amplitude_visual = self.buton17.value()
        self.repetition_visual = self.buton20.value()

        self.totaltime_odour1 = self.delay_odour1 + self.length_odour1 + self.offtime_odour1
        self.totaltime_odour2 = self.delay_odour2 + self.length_odour2 + self.offtime_odour2
        self.totaltime_auditory= self.delay_auditory + self.length_auditory + self.offtime_auditory
        self.totaltime_whisker = self.delay_whisker + self.length_whisker + self.offtime_whisker


    def repetition_control(self):
        if self.repetition_odour1==0:
            self.odour1_flag=0
        if self.repetition_odour2==0:
            self.odour2_flag=0
        if self.repetition_visual==0:
            self.visual_flag=0
        if self.repetition_auditory==0:
            self.auditory_flag=0
        if self.repetition_whisker==0:
            self.whisker_flag=0


    def set_unabled(self):
        for i in self.check_list:
            i.setEnabled(0)
        self.start.setEnabled(0)  # start and cancel unabled!
        self.cancel.setEnabled(0)

    def plotting_figure(self):
        datacompare = max([len(mW.data_valve1), len(mW.data_valve2), len(mW.data_whisker), len(mW.data_auditory),
                           len(mW.data_visual)])

        data_list = [mW.data_valve1, mW.data_valve2, mW.data_whisker, mW.data_auditory, mW.data_visual]
        for i in data_list:
            i += [0] * (datacompare - len(i))
        fig, axes = plt.subplots(3, 1, figsize=(18, 7))

        fig.suptitle("Stimulus-Time Graph")
        axes[0].plot(mW.data_valve1, color='red', drawstyle='steps-pre')
        axes[0].set_ylabel('Odour1')
        axes[0].set_xticks(list(range(0, datacompare)))
        axes[0].set_yticks([0,1])


        axes[1].plot( mW.data_valve2, color='green', drawstyle='steps-pre')
        axes[1].set_ylabel('Odour2')
        axes[1].set_xticks(list(range(0, datacompare)))
        axes[1].set_yticks([0,1])
        axes[2].plot(mW.data_whisker, color='blue', drawstyle='steps-pre')
        axes[2].set_ylabel('Whisker')
        axes[2].set_xlabel('Time')
        axes[2].set_xticks(list(range(0, datacompare)))
        axes[2].set_yticks([0,1])
        plt.subplots_adjust(top=0.94, hspace=0.29, bottom=0.09,left=0.048,right=0.96)
        plt.show()

    def creating_csv(self):
        self.file_name = datetime.ctime(datetime.now())
        self.timecompare=max([len(mW.data_valve1), len(mW.data_valve2), len(mW.data_whisker), len(mW.data_auditory),len(mW.data_visual)])
        self.time=list(range(0,self.timecompare))
        finished_data = list(zip_longest(self.time[1:], mW.data_valve1[1:], mW.data_valve2[1:], mW.data_whisker[1:], mW.data_auditory[1:],mW.data_visual[1:], fillvalue=0))

        header = ['Time', 'Odour1', 'Odour2', 'Whisker', 'Auditive', 'Visual']
        with open(''.join([self.file_name, '.csv']), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for i in finished_data:
                writer.writerow(i)

    def function_cancel(self):

        self.set_enabled()
        global running
        global running_whisker
        self.running = 0
        self.running_whisker = 0
        #mW.general_thread.quit()  # thread-safe quit
        mW.whisker_thread.quit()
        
    def set_enabled(self):
        # MAKE ENABLED OF SELECTIONS
        for i in self.check_list:
            i.setEnabled(1)
        self.start.setEnabled(1)
        self.cancel.setEnabled(1)

    def click_cancel(self):
        for i in self.butonlist:  # When user wants to reset selections and click cancel values are changed as 0
            i = i.setValue(0)
        for i in self.check_list:
            i = i.setChecked(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mW = MainWindow()
    sys.exit(app.exec_())


