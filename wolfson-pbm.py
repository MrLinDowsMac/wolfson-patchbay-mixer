from PyQt4.QtGui import *
from PyQt4.QtCore import *
from dragbutton import DragButton
from wiringgraphicsview import *
import collections
import subprocess

import icons_rc

app = QApplication([])

scene = MyScene()
menu = QMenu()
widget_container = QWidget()

#dictonaries for dragbuttons (used later for connecting them)
jacks_dic = {}
inputs_dic = collections.OrderedDict()
wire_dic = {}

#                                     AIF1RX (PLAYBACK CONTROLS)

# put a button into the scene and move it
btn_AIF1RX1 = DragButton()
btn_AIF1RX1.setObjectName("btn_AIF1RX1")
btn_AIF1RX1.setControlName("AIF1RX1")
btn_AIF1RX1.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_AIF1RX1.setAcceptDrops(False)
btn_AIF1RX1.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of button1
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_AIF1RX1.setIcon(icon)
btn_AIF1RX1.setFlat(False)
btn_AIF1RX1.setMenu(menu)
jacks_dic['AIF1RX1'] = btn_AIF1RX1

btn_AIF1RX2 = DragButton()
btn_AIF1RX2.setObjectName("btn_AIF1RX2")
btn_AIF1RX2.setControlName("AIF1RX2")
btn_AIF1RX2.setGeometry(QRect(200, -50, 51, 31)) #Set dimensions of it
btn_AIF1RX2.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_AIF1RX2.setAcceptDrops(False)
#Set input line icon
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_AIF1RX2.setIcon(icon)
btn_AIF1RX2.setFlat(False)
btn_AIF1RX2.setMenu(menu)
jacks_dic['AIF1RX2'] = btn_AIF1RX2

#Create Layouts for AIF1RX
AIF1RX_main_layout = QVBoxLayout()
AIF1RX_layout = QHBoxLayout()
AIF1RX1_layout = QVBoxLayout()
AIF1RX2_layout = QVBoxLayout()

#Create Labels for AIF1RXl
lbl_playback = QLabel("Playback From RPi")
lbl_AIF1RX1_L = QLabel("L")
AIF1RX1_layout.addWidget(lbl_AIF1RX1_L)
lbl_AIF1RX2_R = QLabel("R")
AIF1RX2_layout.addWidget(lbl_AIF1RX2_R)
lbl_AIF1RX1 = QLabel("AIF1RX1")
AIF1RX1_layout.addWidget( lbl_AIF1RX1 )
lbl_AIF1RX2 = QLabel("AIF1RX2")
AIF1RX2_layout.addWidget( lbl_AIF1RX2 )


#fit AIF1RX layouts
AIF1RX_main_layout.addWidget( lbl_playback )
AIF1RX_main_layout.addLayout(AIF1RX_layout)
AIF1RX_layout.addLayout(AIF1RX1_layout)
AIF1RX_layout.addLayout(AIF1RX2_layout)

AIF1RX1_layout.addWidget(btn_AIF1RX1)
AIF1RX2_layout.addWidget(btn_AIF1RX2)


#                                                /////  AIF1TX (RECORD INPUTS)    ////

btn_AIF1TX1_1 = DragButton()
btn_AIF1TX1_1.setObjectName("btn_AIF1TX1_1")
btn_AIF1TX1_1.setControlName("AIF1TX1 Input 1")
#This button shoudn't be dragged, it is just for dropping.
btn_AIF1TX1_1.setAllowDrag(False)
btn_AIF1TX1_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX1_1.setIcon(icon)
btn_AIF1TX1_1.setFixedWidth(16)
inputs_dic['AIF1TX1_1'] = btn_AIF1TX1_1

btn_AIF1TX1_2 = DragButton()
btn_AIF1TX1_2.setObjectName("btn_AIF1TX1_2")
btn_AIF1TX1_2.setControlName("AIF1TX1 Input 2")
btn_AIF1TX1_2.setAllowDrag(False)
btn_AIF1TX1_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX1_2.setIcon(icon)
btn_AIF1TX1_2.setFixedWidth(16)
inputs_dic['AIF1TX1_2'] = btn_AIF1TX1_2

btn_AIF1TX1_3 = DragButton()
btn_AIF1TX1_3.setObjectName("btn_AIF1TX1_3")
btn_AIF1TX1_3.setControlName("AIF1TX1 Input 3")
btn_AIF1TX1_3.setAllowDrag(False)
btn_AIF1TX1_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX1_3.setIcon(icon)
btn_AIF1TX1_3.setFixedWidth(16)
inputs_dic['AIF1TX1_3'] = btn_AIF1TX1_3


btn_AIF1TX1_4 = DragButton()
btn_AIF1TX1_4.setObjectName("btn_AIF1TX1_4")
btn_AIF1TX1_4.setControlName("AIF1TX1 Input 4")
btn_AIF1TX1_4.setAllowDrag(False)
btn_AIF1TX1_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX1_4.setIcon(icon)
btn_AIF1TX1_4.setFixedWidth(16)
inputs_dic['AIF1TX1_4'] = btn_AIF1TX1_4

btn_AIF1TX2_1 = DragButton()
btn_AIF1TX2_1.setObjectName("btn_AIF1TX2_1")
btn_AIF1TX2_1.setControlName("AIF1TX2 Input 1")
btn_AIF1TX2_1.setAllowDrag(False)
btn_AIF1TX2_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX2_1.setIcon(icon)
btn_AIF1TX2_1.setFixedWidth(16)
inputs_dic['AIF1TX2_1'] = btn_AIF1TX2_1

btn_AIF1TX2_2 = DragButton()
btn_AIF1TX2_2.setObjectName("btn_AIF1TX2_2")
btn_AIF1TX2_2.setControlName("AIF1TX2 Input 2")
btn_AIF1TX2_2.setAllowDrag(False)
btn_AIF1TX2_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX2_2.setIcon(icon)
btn_AIF1TX2_2.setFixedWidth(16)
inputs_dic['AIF1TX2_2'] = btn_AIF1TX2_2

btn_AIF1TX2_3 = DragButton()
btn_AIF1TX2_3.setObjectName("btn_AIF1TX2_3")
btn_AIF1TX2_3.setControlName("AIF1TX2 Input 3")
btn_AIF1TX2_3.setAllowDrag(False)
btn_AIF1TX2_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX2_3.setIcon(icon)
btn_AIF1TX2_3.setFixedWidth(16)
inputs_dic['AIF1TX2_3'] = btn_AIF1TX2_3

btn_AIF1TX2_4 = DragButton()
btn_AIF1TX2_4.setObjectName("btn_AIF1TX2_4")
btn_AIF1TX2_4.setControlName("AIF1TX2 Input 4")
btn_AIF1TX2_4.setAllowDrag(False)
btn_AIF1TX2_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_AIF1TX2_4.setIcon(icon)
btn_AIF1TX2_4.setFixedWidth(16)
inputs_dic['AIF1TX2_4'] = btn_AIF1TX2_4

#Create Layouts for AIF1TX
AIF1TX_main_layout = QVBoxLayout()
AIF1TX_layout = QHBoxLayout()
AIF1TX1_layout = QVBoxLayout()
AIF1TX2_layout = QVBoxLayout()
AIF1TX1_inputs_layout = QHBoxLayout()
AIF1TX2_inputs_layout = QHBoxLayout()

#Create Labels for AIF1TX
lbl_record = QLabel("Record to RPi")
lbl_AIF1TX1_L = QLabel("L")
AIF1TX1_layout.addWidget(lbl_AIF1TX1_L)
lbl_AIF1TX2_R = QLabel("R")
AIF1TX2_layout.addWidget(lbl_AIF1TX2_R)
lbl_AIF1TX1 = QLabel("AIF1TX1")
AIF1TX1_layout.addWidget( lbl_AIF1TX1 )
lbl_AIF1TX2 = QLabel("AIF1TX2")
AIF1TX2_layout.addWidget( lbl_AIF1TX2 )

#fit AIF1TX layouts
AIF1TX_main_layout.addWidget( lbl_record )
AIF1TX_main_layout.addLayout(AIF1TX_layout)
AIF1TX_layout.addLayout(AIF1TX1_layout)
AIF1TX_layout.addLayout(AIF1TX2_layout)
AIF1TX1_layout.addLayout(AIF1TX1_inputs_layout)
AIF1TX2_layout.addLayout(AIF1TX2_inputs_layout)

#Inputs
AIF1TX1_inputs_layout.addWidget(btn_AIF1TX1_1)
AIF1TX1_inputs_layout.addWidget(btn_AIF1TX1_2)
AIF1TX1_inputs_layout.addWidget(btn_AIF1TX1_3)
AIF1TX1_inputs_layout.addWidget(btn_AIF1TX1_4)
AIF1TX1_inputs_layout.setSpacing(0)
AIF1TX1_inputs_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)

AIF1TX2_inputs_layout.addWidget(btn_AIF1TX2_1)
AIF1TX2_inputs_layout.addWidget(btn_AIF1TX2_2)
AIF1TX2_inputs_layout.addWidget(btn_AIF1TX2_3)
AIF1TX2_inputs_layout.addWidget(btn_AIF1TX2_4)
AIF1TX2_inputs_layout.setSpacing(0)
AIF1TX2_inputs_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)

#Wrap Playback/Record controls into a layout
#record_playback_layouts = QHBoxLayout(widget_container)
record_playback_layouts = QHBoxLayout()
record_playback_layouts.addStretch(1)
record_playback_layouts.addLayout(AIF1RX_main_layout)
record_playback_layouts.addLayout(AIF1TX_main_layout)
record_playback_layouts.addStretch(1)
#widget_container.setFixedWidth(290)

#                                               ////////////////// INPUT DEVICES ////////////////////////
#                                                    /////       Digital Microphones (DMIC)   ////

#IN2L (Headset Mic IN LEFT CHANNEL) 
btn_IN2L = DragButton()
btn_IN2L.setObjectName("btn_IN2L")
btn_IN2L.setControlName("IN2L")
btn_IN2L.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN2L.setAcceptDrops(False)
btn_IN2L.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN2L
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN2L.setIcon(icon)
btn_IN2L.setFlat(False)
btn_IN2L.setMenu(menu)
jacks_dic['IN2L'] = btn_IN2L

#IN2R (Headset IN RIGHT CHANNEL)
btn_IN2R = DragButton()
btn_IN2R.setObjectName("btn_IN2R")
btn_IN2R.setControlName("IN2R")
btn_IN2R.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN2R.setAcceptDrops(False)
btn_IN2R.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN2L
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN2R.setIcon(icon)
btn_IN2R.setFlat(False)
btn_IN2R.setMenu(menu)
jacks_dic['IN2R'] = btn_IN2R

#Checkbox On/off
chk_box = QtGui.QCheckBox('On')
chk_box.setObjectName("chk_box")

#Labels and Icons
lbl_IN2L = QtGui.QLabel()
lbl_IN2L.setObjectName("lbl_IN2L")
lbl_IN2R = QtGui.QLabel()
lbl_IN2R.setObjectName("lbl_IN2R")
lbl_IN2L.setText("<html><head/><body><p><img src=\":/DMIC.png\"/><span style=\" font-weight:600;\"> IN2 L</span></p></body></html>")
lbl_IN2R.setText("<html><head/><body><p><img src=\":/DMIC.png\"/><span style=\" font-weight:600;\"> IN2 R</span></p></body></html>")
lbl_DMIC = QtGui.QLabel()
lbl_DMIC.setObjectName("lbl_DMIC")
lbl_DMIC.setText("<html><head/><body><p><span style=\" font-weight:600;\">DMIC</span></p></body></html>")


#Layouts
IN2L_layout = QHBoxLayout()
IN2L_layout.addWidget(lbl_IN2L)
IN2L_layout.addWidget(btn_IN2L)

IN2R_layout = QHBoxLayout()
IN2R_layout.addWidget(lbl_IN2R)
IN2R_layout.addWidget(btn_IN2R)

IN2_layout = QVBoxLayout()
IN2_layout.addWidget(chk_box)
IN2_layout.addLayout(IN2L_layout)
IN2_layout.addLayout(IN2R_layout)

DMIC_layout = QHBoxLayout()
DMIC_layout.addWidget(lbl_DMIC)
DMIC_layout.addLayout(IN2_layout)

#                                                                           /////    HEADSET MIC      ////
#IN2L (LINE IN LEFT CHANNEL)
btn_IN1L = DragButton()
btn_IN1L.setObjectName("btn_IN1L")
btn_IN1L.setControlName("IN1L")
btn_IN1L.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN1L.setAcceptDrops(False)
btn_IN1L.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN1L
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN1L.setIcon(icon)
btn_IN1L.setFlat(False)
btn_IN1L.setMenu(menu)
jacks_dic['IN1L'] = btn_IN1L

#IN2R (LINE IN RIGHT CHANNEL)
btn_IN1R = DragButton()
btn_IN1R.setObjectName("btn_IN1R")
btn_IN1R.setControlName("IN1R")
btn_IN1R.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN1R.setAcceptDrops(False)
btn_IN1R.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN1R
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN1R.setIcon(icon)
btn_IN1R.setFlat(False)
btn_IN1R.setMenu(menu)
jacks_dic['IN1R'] = btn_IN1R

#Checkbox On/off
chk_headsetmic = QtGui.QCheckBox('On')
chk_headsetmic.setObjectName("chk_headsetmic")

#Labels and Icons
lbl_IN1L = QtGui.QLabel()
lbl_IN1L.setObjectName("lbl_IN1L")
lbl_IN1R = QtGui.QLabel()
lbl_IN1R.setObjectName("lbl_IN1R")
lbl_IN1L.setText("<html><head/><body><p><span style=\" font-weight:600;\"> IN1 L</span></p></body></html>")
lbl_IN1R.setText("<html><head/><body><p><span style=\" font-weight:600;\"> IN1 R</span></p></body></html>")
lbl_HeadsetMic = QtGui.QLabel()
lbl_HeadsetMic.setObjectName("lbl_HeadsetMic")
lbl_HeadsetMic.setText("<html><head/><body><p><img src=\":/audio-headset.png\"/></p><p><span style=\" font-weight:600;\"> Headset Mic</span></p></body></html>")


#Layouts
IN1L_layout = QHBoxLayout()
IN1L_layout.addWidget(lbl_IN1L)
IN1L_layout.addWidget(btn_IN1L)

IN1R_layout = QHBoxLayout()
IN1R_layout.addWidget(lbl_IN1R)
IN1R_layout.addWidget(btn_IN1R)

IN1_layout = QVBoxLayout()
IN1_layout.addWidget(chk_headsetmic)
IN1_layout.addLayout(IN1L_layout)
IN1_layout.addLayout(IN1R_layout)

HeadsetMic_layout = QHBoxLayout()
HeadsetMic_layout.addWidget(lbl_HeadsetMic)
HeadsetMic_layout.addLayout(IN1_layout)

#                                                                       /// LINE IN (IN3) ///
#IN3L (LINE IN LEFT CHANNEL)
btn_IN3L = DragButton()
btn_IN3L.setObjectName("btn_IN3L")
btn_IN3L.setControlName("IN3L")
btn_IN3L.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN3L.setAcceptDrops(False)
btn_IN3L.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN3L
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN3L.setIcon(icon)
btn_IN3L.setFlat(False)
btn_IN3L.setMenu(menu)
jacks_dic['IN3L'] = btn_IN3L

#IN3R (LINE IN RIGHT CHANNEL)
btn_IN3R = DragButton()
btn_IN3R.setObjectName("btn_IN3R")
btn_IN3R.setControlName("IN3R")
btn_IN3R.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_IN3R.setAcceptDrops(False)
btn_IN3R.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of IN3R
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_IN3R.setIcon(icon)
btn_IN3R.setFlat(False)
btn_IN3R.setMenu(menu)
jacks_dic['IN3R'] = btn_IN3R

#Checkbox On/off
chk_linein = QtGui.QCheckBox('On')
chk_linein.setObjectName("chk_linein")

#Labels and Icons
lbl_IN3L = QtGui.QLabel()
lbl_IN3L.setObjectName("lbl_IN3L")
lbl_IN3R = QtGui.QLabel()
lbl_IN3R.setObjectName("lbl_IN3R")
lbl_IN3L.setText("<html><head/><body><p><span style=\" font-weight:600;\"> IN3 L</span></p></body></html>")
lbl_IN3R.setText("<html><head/><body><p><span style=\" font-weight:600;\"> IN3 R</span></p></body></html>")
lbl_LineIn = QtGui.QLabel()
lbl_LineIn.setObjectName("lbl_LineIn")
lbl_LineIn.setText("<html><head/><body><p><img src=\":/Line_In.png\"/></p><p><span style=\" font-weight:600;\"> Line In</span></p></body></html>")


#Layouts
IN3L_layout = QHBoxLayout()
IN3L_layout.addWidget(lbl_IN3L)
IN3L_layout.addWidget(btn_IN3L)

IN3R_layout = QHBoxLayout()
IN3R_layout.addWidget(lbl_IN3R)
IN3R_layout.addWidget(btn_IN3R)

IN3_layout = QVBoxLayout()
IN3_layout.addWidget(chk_linein)
IN3_layout.addLayout(IN3L_layout)
IN3_layout.addLayout(IN3R_layout)

LineIn_layout = QHBoxLayout()
LineIn_layout.addWidget(lbl_LineIn)
LineIn_layout.addLayout(IN3_layout)

#                                                                       /// SPDIF IN (AIF2RX) ///
#AIF2RX1 (SPDIF IN LEFT CHANNEL)
btn_AIF2RX1 = DragButton()
btn_AIF2RX1.setObjectName("btn_AIF2RX1")
btn_AIF2RX1.setControlName("AIF2RX1")
btn_AIF2RX1.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_AIF2RX1.setAcceptDrops(False)
btn_AIF2RX1.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of AIF2RX1
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_AIF2RX1.setIcon(icon)
btn_AIF2RX1.setFlat(False)
btn_AIF2RX1.setMenu(menu)
jacks_dic['AIF2RX1'] = btn_AIF2RX1

#AIF2RX2 (SPDIF IN RIGHT CHANNEL)
btn_AIF2RX2 = DragButton()
btn_AIF2RX2.setObjectName("btn_AIF2RX2")
btn_AIF2RX2.setControlName("AIF2RX2")
btn_AIF2RX2.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_AIF2RX2.setAcceptDrops(False)
btn_AIF2RX2.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of AIF2RX2
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_AIF2RX2.setIcon(icon)
btn_AIF2RX2.setFlat(False)
btn_AIF2RX2.setMenu(menu)
jacks_dic['AIF2RX2'] = btn_AIF2RX2

#Checkbox On/off
chk_spdifin = QtGui.QCheckBox('On')
chk_spdifin.setObjectName("chk_spdifin")

#Labels and Icons
lbl_AIF2RX1 = QtGui.QLabel()
lbl_AIF2RX1.setObjectName("lbl_AIF2RX1")
lbl_AIF2RX2 = QtGui.QLabel()
lbl_AIF2RX2.setObjectName("lbl_AIF2RX2")
lbl_AIF2RX1.setText("<html><head/><body><p><span style=\" font-weight:600;\"> AIF2RX1 L</span></p></body></html>")
lbl_AIF2RX2.setText("<html><head/><body><p><span style=\" font-weight:600;\"> AIF2RX2 R</span></p></body></html>")
lbl_SPDIFIN = QtGui.QLabel()
lbl_SPDIFIN.setObjectName("lbl_SPDIFIN")
lbl_SPDIFIN.setText("<html><head/><body><p><img src=\":/SPDIFIN.png\"/></p><p><span style=\" font-weight:600;\"> SPDIF In</span></p></body></html>")


#Layouts
AIF2RX1_layout = QHBoxLayout()
AIF2RX1_layout.addWidget(lbl_AIF2RX1)
AIF2RX1_layout.addWidget(btn_AIF2RX1)

AIF2RX2_layout = QHBoxLayout()
AIF2RX2_layout.addWidget(lbl_AIF2RX2)
AIF2RX2_layout.addWidget(btn_AIF2RX2)

AIF2RX_layout = QVBoxLayout()
AIF2RX_layout.addWidget(chk_spdifin)
AIF2RX_layout.addLayout(AIF2RX1_layout)
AIF2RX_layout.addLayout(AIF2RX2_layout)

SPDIF_IN_layout = QHBoxLayout()
SPDIF_IN_layout.addWidget(lbl_SPDIFIN)
SPDIF_IN_layout.addLayout(AIF2RX_layout)

#                                                                       ////Tone Generator 1 ////
#Tone Generator 1 KHz
btn_ToneGenerator1 = DragButton()
btn_ToneGenerator1.setObjectName("btn_ToneGenerator1")
btn_ToneGenerator1.setControlName("Tone Generator 1")
btn_ToneGenerator1.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_ToneGenerator1.setAcceptDrops(False)
btn_ToneGenerator1.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of Tone Generator 1
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_ToneGenerator1.setIcon(icon)
btn_ToneGenerator1.setFlat(False)
btn_ToneGenerator1.setMenu(menu)
jacks_dic['Tone Generator 1'] = btn_ToneGenerator1

#Tone Generator 2 KHz
btn_ToneGenerator2 = DragButton()
btn_ToneGenerator2.setObjectName("btn_ToneGenerator2")
btn_ToneGenerator2.setControlName("Tone Generator 2")
btn_ToneGenerator2.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_ToneGenerator2.setAcceptDrops(False)
btn_ToneGenerator2.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of AIF2RX2
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_ToneGenerator2.setIcon(icon)
btn_ToneGenerator2.setFlat(False)
btn_ToneGenerator2.setMenu(menu)
jacks_dic['Tone Generator 2'] = btn_ToneGenerator2

#White Noise Generator
btn_NoiseGenerator = DragButton()
btn_NoiseGenerator.setObjectName("btn_NoiseGenerator")
btn_NoiseGenerator.setControlName("Noise Generator")
btn_NoiseGenerator.setAllowDrag(True) #Allow Drag n Drop of DragButton
btn_NoiseGenerator.setAcceptDrops(False)
btn_NoiseGenerator.setGeometry(QRect(-100, 50, 51, 31)) #Set dimensions of it
#Set icon of AIF2RX2
icon = QIcon()
icon.addPixmap(QPixmap(":/audio-input-line.png"), QIcon.Normal, QIcon.Off)
btn_NoiseGenerator.setIcon(icon)
btn_NoiseGenerator.setFlat(False)
btn_NoiseGenerator.setMenu(menu)
jacks_dic['Noise Generator'] = btn_NoiseGenerator

#Labels and Icons
lbl_ToneGenerator1 = QtGui.QLabel()
lbl_ToneGenerator1.setObjectName("lbl_ToneGenerator1")
lbl_ToneGenerator2 = QtGui.QLabel()
lbl_ToneGenerator2.setObjectName("lbl_ToneGenerator2")
lbl_NoiseGenerator = QtGui.QLabel()
lbl_NoiseGenerator.setObjectName("lbl_NoiseGenerator")
lbl_ToneGenerator1.setText("<html><head/><body><p><span style=\" font-weight:600;\"> Tone Generator 1 (1Khz)</span></p></body></html>")
lbl_ToneGenerator2.setText("<html><head/><body><p><span style=\" font-weight:600;\"> Tone Generator 2 (1KHz)</span></p></body></html>")
lbl_NoiseGenerator.setText("<html><head/><body><p><span style=\" font-weight:600;\"> White Noise Generator </span></p></body></html>")
lbl_Generators = QtGui.QLabel()
lbl_Generators.setObjectName("lbl_Generators")
lbl_Generators.setText("<html><head/><body><p><span style=\" font-weight:600;\"> Noise Generators</span></p></body></html>")


#Layouts
ToneGenerator1_layout = QHBoxLayout()
ToneGenerator1_layout.addWidget(lbl_ToneGenerator1)
ToneGenerator1_layout.addWidget(btn_ToneGenerator1)

ToneGenerator2_layout = QHBoxLayout()
ToneGenerator2_layout.addWidget(lbl_ToneGenerator2)
ToneGenerator2_layout.addWidget(btn_ToneGenerator2)

NoiseGenerator_layout = QHBoxLayout()
NoiseGenerator_layout.addWidget(lbl_NoiseGenerator)
NoiseGenerator_layout.addWidget(btn_NoiseGenerator)

Generators_layout = QVBoxLayout()
Generators_layout.addWidget(lbl_Generators)
Generators_layout.addLayout(ToneGenerator1_layout)
Generators_layout.addLayout(ToneGenerator2_layout)
Generators_layout.addLayout(NoiseGenerator_layout)

#                                                            //////////////// OUTPUT DEVICES ////////////////
#                                                                       //// Headset (HPOUT1) ////
btn_HPOUT1L_1 = DragButton()
btn_HPOUT1L_1.setObjectName("btn_HPOUT1L_1")
btn_HPOUT1L_1.setControlName("HPOUT1L Input 1")
btn_HPOUT1L_1.setAllowDrag(False)
btn_HPOUT1L_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1L_1.setIcon(icon)
btn_HPOUT1L_1.setFixedWidth(16)
inputs_dic['HPOUT1L Input 1'] = btn_HPOUT1L_1

btn_HPOUT1L_2 = DragButton()
btn_HPOUT1L_2.setObjectName("btn_HPOUT1L_2")
btn_HPOUT1L_2.setControlName("HPOUT1L Input 2")
btn_HPOUT1L_2.setAllowDrag(False)
btn_HPOUT1L_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1L_2.setIcon(icon)
btn_HPOUT1L_2.setFixedWidth(16)
inputs_dic['HPOUT1L Input 2'] = btn_HPOUT1L_2

btn_HPOUT1L_3 = DragButton()
btn_HPOUT1L_3.setObjectName("btn_HPOUT1L_3")
btn_HPOUT1L_3.setControlName("HPOUT1L Input 3")
btn_HPOUT1L_3.setAllowDrag(False)
btn_HPOUT1L_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1L_3.setIcon(icon)
btn_HPOUT1L_3.setFixedWidth(16)
inputs_dic['HPOUT1L Input 3'] = btn_HPOUT1L_3


btn_HPOUT1L_4 = DragButton()
btn_HPOUT1L_4.setObjectName("btn_HPOUT1L_4")
btn_HPOUT1L_4.setControlName("HPOUT1L Input 4")
btn_HPOUT1L_4.setAllowDrag(False)
btn_HPOUT1L_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1L_4.setIcon(icon)
btn_HPOUT1L_4.setFixedWidth(16)
inputs_dic['HPOUT1L Input 4'] = btn_HPOUT1L_4

btn_HPOUT1R_1 = DragButton()
btn_HPOUT1R_1.setObjectName("btn_HPOUT1R_1")
btn_HPOUT1R_1.setControlName("HPOUT1R Input 1")
btn_HPOUT1R_1.setAllowDrag(False)
btn_HPOUT1R_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1R_1.setIcon(icon)
btn_HPOUT1R_1.setFixedWidth(16)
inputs_dic['HPOUT1R Input 1'] = btn_HPOUT1R_1

btn_HPOUT1R_2 = DragButton()
btn_HPOUT1R_2.setObjectName("btn_HPOUT1R_2")
btn_HPOUT1R_2.setControlName("HPOUT1R Input 2")
btn_HPOUT1R_2.setAllowDrag(False)
btn_HPOUT1R_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1R_2.setIcon(icon)
btn_HPOUT1R_2.setFixedWidth(16)
inputs_dic['HPOUT1R Input 2'] = btn_HPOUT1R_2


btn_HPOUT1R_3 = DragButton()
btn_HPOUT1R_3.setObjectName("btn_HPOUT1R_3")
btn_HPOUT1R_3.setControlName("HPOUT1R Input 3")
btn_HPOUT1R_3.setAllowDrag(False)
btn_HPOUT1R_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1R_3.setIcon(icon)
btn_HPOUT1R_3.setFixedWidth(16)
inputs_dic['HPOUT1R Input 3'] = btn_HPOUT1R_3

btn_HPOUT1R_4 = DragButton()
btn_HPOUT1R_4.setObjectName("btn_HPOUT1R_4")
btn_HPOUT1R_4.setControlName("HPOUT1R Input 4")
btn_HPOUT1R_4.setAllowDrag(False)
btn_HPOUT1R_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT1R_4.setIcon(icon)
btn_HPOUT1R_4.setFixedWidth(16)
inputs_dic['HPOUT1R Input 4'] = btn_HPOUT1R_4

#Labels and Icons
lbl_HPOUT1L = QtGui.QLabel()
lbl_HPOUT1L.setObjectName("lbl_HPOUT1L")
lbl_HPOUT1R = QtGui.QLabel()
lbl_HPOUT1R.setObjectName("lbl_HPOUT1R")
lbl_HPOUT1L.setText("<html><head/><body><p><span style=\" font-weight:600;\"> HPOUT1 L</span></p></body></html>")
lbl_HPOUT1R.setText("<html><head/><body><p><span style=\" font-weight:600;\"> HPOUT1 R</span></p></body></html>")
lbl_HPOUT1 = QtGui.QLabel()
lbl_HPOUT1.setObjectName("lbl_HPOUT1")
lbl_HPOUT1.setText("<html><head/><body><p><img src=\":/Headset_output.png\"/></p><p><span style=\" font-weight:600;\"> Headset output </p><p>(HPOUT1) </span></p></body></html>")

#Layouts
HPOUT1L_connectors_layout = QVBoxLayout()
#HPOUT1L_connectors_layout.addStretch(1)
HPOUT1L_connectors_layout.addWidget(btn_HPOUT1L_1)
HPOUT1L_connectors_layout.addWidget(btn_HPOUT1L_2)
HPOUT1L_connectors_layout.addWidget(btn_HPOUT1L_3)
HPOUT1L_connectors_layout.addWidget(btn_HPOUT1L_4)
#HPOUT1L_connectors_layout.addStretch(1)

HPOUT1L_layout = QHBoxLayout()
HPOUT1L_layout.addLayout(HPOUT1L_connectors_layout)
HPOUT1L_layout.addWidget(lbl_HPOUT1L)

HPOUT1R_connectors_layout = QVBoxLayout()
#HPOUT1R_connectors_layout.addStretch(1)
HPOUT1R_connectors_layout.addWidget(btn_HPOUT1R_1)
HPOUT1R_connectors_layout.addWidget(btn_HPOUT1R_2)
HPOUT1R_connectors_layout.addWidget(btn_HPOUT1R_3)
HPOUT1R_connectors_layout.addWidget(btn_HPOUT1R_4)
#HPOUT1R_connectors_layout.addStretch(1)

HPOUT1R_layout = QHBoxLayout()
HPOUT1R_layout.addLayout(HPOUT1R_connectors_layout)
HPOUT1R_layout.addWidget(lbl_HPOUT1R)

HPOUT1_layout = QVBoxLayout()
HPOUT1_layout.addLayout(HPOUT1L_layout)
HPOUT1_layout.addLayout(HPOUT1R_layout)

Headset_layout = QHBoxLayout()
Headset_layout.addLayout(HPOUT1_layout)
Headset_layout.addWidget(lbl_HPOUT1)


#                                                                       //// LINE OUT (HPOUT2) ////
btn_HPOUT2L_1 = DragButton()
btn_HPOUT2L_1.setObjectName("btn_HPOUT2L_1")
btn_HPOUT2L_1.setControlName("HPOUT2L Input 1")
btn_HPOUT2L_1.setAllowDrag(False)
btn_HPOUT2L_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2L_1.setIcon(icon)
btn_HPOUT2L_1.setFixedWidth(16)
inputs_dic['HPOUT2L Input 1'] = btn_HPOUT2L_1

btn_HPOUT2L_2 = DragButton()
btn_HPOUT2L_2.setObjectName("btn_HPOUT2L_2")
btn_HPOUT2L_2.setControlName("HPOUT2L Input 2")
btn_HPOUT2L_2.setAllowDrag(False)
btn_HPOUT2L_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2L_2.setIcon(icon)
btn_HPOUT2L_2.setFixedWidth(16)
inputs_dic['HPOUT2L Input 2'] = btn_HPOUT2L_2

btn_HPOUT2L_3 = DragButton()
btn_HPOUT2L_3.setObjectName("btn_HPOUT2L_3")
btn_HPOUT2L_3.setControlName("HPOUT2L Input 3")
btn_HPOUT2L_3.setAllowDrag(False)
btn_HPOUT2L_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2L_3.setIcon(icon)
btn_HPOUT2L_3.setFixedWidth(16)
inputs_dic['HPOUT2L Input 3'] = btn_HPOUT2L_3


btn_HPOUT2L_4 = DragButton()
btn_HPOUT2L_4.setObjectName("btn_HPOUT2L_4")
btn_HPOUT2L_4.setControlName("HPOUT2L Input 4")
btn_HPOUT2L_4.setAllowDrag(False)
btn_HPOUT2L_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2L_4.setIcon(icon)
btn_HPOUT2L_4.setFixedWidth(16)
inputs_dic['HPOUT2L Input 4'] = btn_HPOUT2L_4

btn_HPOUT2R_1 = DragButton()
btn_HPOUT2R_1.setObjectName("btn_HPOUT2R_1")
btn_HPOUT2R_1.setControlName("HPOUT2R Input 1")
btn_HPOUT2R_1.setAllowDrag(False)
btn_HPOUT2R_1.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2R_1.setIcon(icon)
btn_HPOUT2R_1.setFixedWidth(16)
inputs_dic['HPOUT2R Input 1'] = btn_HPOUT2R_1

btn_HPOUT2R_2 = DragButton()
btn_HPOUT2R_2.setObjectName("btn_HPOUT2R_2")
btn_HPOUT2R_2.setControlName("HPOUT2R Input 2")
btn_HPOUT2R_2.setAllowDrag(False)
btn_HPOUT2R_2.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2R_2.setIcon(icon)
btn_HPOUT2R_2.setFixedWidth(16)
inputs_dic['HPOUT2R Input 2'] = btn_HPOUT2R_2


btn_HPOUT2R_3 = DragButton()
btn_HPOUT2R_3.setObjectName("btn_HPOUT2R_3")
btn_HPOUT2R_3.setControlName("HPOUT2R Input 3")
btn_HPOUT2R_3.setAllowDrag(False)
btn_HPOUT2R_3.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2R_3.setIcon(icon)
btn_HPOUT2R_3.setFixedWidth(16)
inputs_dic['HPOUT2R Input 3'] = btn_HPOUT2R_3

btn_HPOUT2R_4 = DragButton()
btn_HPOUT2R_4.setObjectName("btn_HPOUT2R_4")
btn_HPOUT2R_4.setControlName("HPOUT2R Input 4")
btn_HPOUT2R_4.setAllowDrag(False)
btn_HPOUT2R_4.setAcceptDrops(True)
icon = QIcon()
icon.addPixmap(QPixmap(":/input_small.png"), QIcon.Normal, QIcon.Off)
btn_HPOUT2R_4.setIcon(icon)
btn_HPOUT2R_4.setFixedWidth(16)
inputs_dic['HPOUT2R Input 4'] = btn_HPOUT2R_4

#Labels and Icons
lbl_HPOUT2L = QtGui.QLabel()
lbl_HPOUT2L.setObjectName("lbl_HPOUT2L")
lbl_HPOUT2R = QtGui.QLabel()
lbl_HPOUT2R.setObjectName("lbl_HPOUT2R")
lbl_HPOUT2L.setText("<html><head/><body><p><span style=\" font-weight:600;\"> HPOUT2 L</span></p></body></html>")
lbl_HPOUT2R.setText("<html><head/><body><p><span style=\" font-weight:600;\"> HPOUT2 R</span></p></body></html>")
lbl_HPOUT2 = QtGui.QLabel()
lbl_HPOUT2.setObjectName("lbl_HPOUT2")
lbl_HPOUT2.setText("<html><head/><body><p><img src=\":/Line_Out.png\"/></p><p><span style=\" font-weight:600;\"> Line Out </p><p>(HPOUT2) </span></p></body></html>")

#Layouts
HPOUT2L_connectors_layout = QVBoxLayout()
#HPOUT2L_connectors_layout.addStretch(1)
HPOUT2L_connectors_layout.addWidget(btn_HPOUT2L_1)
HPOUT2L_connectors_layout.addWidget(btn_HPOUT2L_2)
HPOUT2L_connectors_layout.addWidget(btn_HPOUT2L_3)
HPOUT2L_connectors_layout.addWidget(btn_HPOUT2L_4)
#HPOUT2L_connectors_layout.addStretch(1)

HPOUT2L_layout = QHBoxLayout()
HPOUT2L_layout.addLayout(HPOUT2L_connectors_layout)
HPOUT2L_layout.addWidget(lbl_HPOUT2L)

HPOUT2R_connectors_layout = QVBoxLayout()
#HPOUT2R_connectors_layout.addStretch(1)
HPOUT2R_connectors_layout.addWidget(btn_HPOUT2R_1)
HPOUT2R_connectors_layout.addWidget(btn_HPOUT2R_2)
HPOUT2R_connectors_layout.addWidget(btn_HPOUT2R_3)
HPOUT2R_connectors_layout.addWidget(btn_HPOUT2R_4)
#HPOUT2R_connectors_layout.addStretch(1)

HPOUT2R_layout = QHBoxLayout()
HPOUT2R_layout.addLayout(HPOUT2R_connectors_layout)
HPOUT2R_layout.addWidget(lbl_HPOUT2R)

HPOUT2_layout = QVBoxLayout()
HPOUT2_layout.addLayout(HPOUT2L_layout)
HPOUT2_layout.addLayout(HPOUT2R_layout)

LineOut_layout = QHBoxLayout()
LineOut_layout.addLayout(HPOUT2_layout)
LineOut_layout.addWidget(lbl_HPOUT2)




#                                                                        ////  In Devices Layouts  ////
#Put all the IN Devices
In_layouts = QVBoxLayout()
lbl_in = QLabel("IN Devices")
In_layouts.addWidget(lbl_in)
In_layouts.addLayout(HeadsetMic_layout) 
In_layouts.addLayout(DMIC_layout)
In_layouts.addLayout(LineIn_layout)
In_layouts.addLayout(SPDIF_IN_layout)
In_layouts.addLayout(Generators_layout)


#                                                                       /// Out Devices Layouts ///
Out_layouts = QVBoxLayout()
lbl_out = QLabel("Out Devices")
Out_layouts.addWidget(lbl_out)
Out_layouts.addLayout(Headset_layout)
Out_layouts.addLayout(LineOut_layout)

#                                                                       ///Filters Layouts///
#TODO: Implement Filters


#IN/FILTERS/OUT Layout
In_filters_out_layout = QHBoxLayout()
In_filters_out_layout.addLayout(In_layouts)
#In this line should be the filters layout
In_filters_out_layout.addLayout(Out_layouts)

#Fits all the layouts here
Main_layout = QVBoxLayout(widget_container)
Main_layout.addLayout(record_playback_layouts)
Main_layout.addLayout(In_filters_out_layout)

widget_scene = scene.addWidget(widget_container)

# Instantiate our own proxy which forwars drag/drop events to the child widget
#of AIFTX
#                       // Proxy Widgets for AIF1TX1 //
proxy_btn_AIF1TX1_1 = ProxyWidget() 
proxy_btn_AIF1TX1_1.setWidget(btn_AIF1TX1_1)
proxy_btn_AIF1TX1_1.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX1_1)

proxy_btn_AIF1TX1_2 = ProxyWidget() 
proxy_btn_AIF1TX1_2.setWidget(btn_AIF1TX1_2)
proxy_btn_AIF1TX1_2.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX1_2)

proxy_btn_AIF1TX1_3 = ProxyWidget() 
proxy_btn_AIF1TX1_3.setWidget(btn_AIF1TX1_3)
proxy_btn_AIF1TX1_3.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX1_3)

proxy_btn_AIF1TX1_4 = ProxyWidget() 
proxy_btn_AIF1TX1_4.setWidget(btn_AIF1TX1_4)
proxy_btn_AIF1TX1_4.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX1_4)
#                    // Proxy Widgets for AIF1TX2  //
proxy_btn_AIF1TX2_1 = ProxyWidget() 
proxy_btn_AIF1TX2_1.setWidget(btn_AIF1TX2_1)
proxy_btn_AIF1TX2_1.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX2_1)

proxy_btn_AIF1TX2_2 = ProxyWidget() 
proxy_btn_AIF1TX2_2.setWidget(btn_AIF1TX2_2)
proxy_btn_AIF1TX2_2.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX2_2)

proxy_btn_AIF1TX2_3 = ProxyWidget() 
proxy_btn_AIF1TX2_3.setWidget(btn_AIF1TX2_3)
proxy_btn_AIF1TX2_3.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX2_3)

proxy_btn_AIF1TX2_4 = ProxyWidget() 
proxy_btn_AIF1TX2_4.setWidget(btn_AIF1TX2_4)
proxy_btn_AIF1TX2_4.setAcceptDrops(True)
scene.addItem(proxy_btn_AIF1TX2_4)


#                // Proxy Widgets for HPOUT1 //
proxy_btn_HPOUT1L_1 = ProxyWidget() 
proxy_btn_HPOUT1L_1.setWidget(btn_HPOUT1L_1)
proxy_btn_HPOUT1L_1.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1L_1)

proxy_btn_HPOUT1L_2 = ProxyWidget() 
proxy_btn_HPOUT1L_2.setWidget(btn_HPOUT1L_2)
proxy_btn_HPOUT1L_2.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1L_2)

proxy_btn_HPOUT1L_3 = ProxyWidget() 
proxy_btn_HPOUT1L_3.setWidget(btn_HPOUT1L_3)
proxy_btn_HPOUT1L_3.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1L_3)

proxy_btn_HPOUT1L_4 = ProxyWidget() 
proxy_btn_HPOUT1L_4.setWidget(btn_HPOUT1L_4)
proxy_btn_HPOUT1L_4.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1L_4)

proxy_btn_HPOUT1R_1 = ProxyWidget() 
proxy_btn_HPOUT1R_1.setWidget(btn_HPOUT1R_1)
proxy_btn_HPOUT1R_1.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1R_1)

proxy_btn_HPOUT1R_2 = ProxyWidget() 
proxy_btn_HPOUT1R_2.setWidget(btn_HPOUT1R_2)
proxy_btn_HPOUT1R_2.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1R_2)

proxy_btn_HPOUT1R_3 = ProxyWidget() 
proxy_btn_HPOUT1R_3.setWidget(btn_HPOUT1R_3)
proxy_btn_HPOUT1R_3.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1R_3)

proxy_btn_HPOUT1R_4 = ProxyWidget() 
proxy_btn_HPOUT1R_4.setWidget(btn_HPOUT1R_4)
proxy_btn_HPOUT1R_4.setAcceptDrops(True)
scene.addItem(proxy_btn_HPOUT1R_4)


def amixer_command(control, value):
    p = subprocess.Popen(["amixer", "-c0", "sset", control, value ], stdout=subprocess.PIPE)
    p.communicate()
    rc = p.returncode
    #print rc
    return rc


#Slot for connecting by drag n drop
def on_link(input, jack):
    print input 
    print jack
    #print link
    #Check if a wire was already created between them
    #if wire_dic.get( str(input)[4:] ) == None:
    if wire_dic.get( input.objectName()[4:] ) == None:
        #Check if the input is disabled (or in use) to avoid connecting different jacks into the same input
#        print actions_dic[ str(input)[4:] ].isEnabled()
        #if actions_dic[ str(input)[4:] ].isEnabled() == True:
        if actions_dic[ str(input.objectName()[4:]) ].isEnabled() == True:
            #Run amixer command and gets returncode
            if amixer_command( input.controlName, jack.controlName ) == 0:
            #Input name as key, and a tuple( jack name, a new instance of Wire ) as value. 
                wire_dic[  str(input.objectName())[4:] ] = ( str(jack.objectName())[4:] , Wire( jack , input , None, scene))
                #Disable input option in menu
                actions_dic[ str(input.objectName())[4:] ].setEnabled(False)
                print "Connection Sucessful"
            else:
                print "Connection Failed"
            
            print actions_dic
            #actions_dic[ str(input)[4:] ].setEnabled(False)
    print wire_dic

def on_press(self):
    #Condition checks if receiving object is a button receives that Drops. If is false it means that is a Jack connector dragbutton
    if self.sender().acceptDrops() == False:
        print self.sender()
        for action in actions_dic:
            #Set parent every QAction after click
            actions_dic[ action ].setParent(self.sender())
    
    elif self.sender().acceptDrops() == True: #is for inputs, mouse press should disconnect any connection to them
        input =  str(self.sender().objectName())[4:]
        if wire_dic.get( input ) != None:
            #Run amixer command and checks returncode, sucess command is a 0
            if amixer_command( self.sender().controlName, "None" ) == 0:
               #Clear line
               wire_dic[ input ][1].clear()
               #Delete object reference by deleting key
               del wire_dic[ input ]
               #Enable the input in the menu
               actions_dic[ input ].setEnabled(True)
               print "Disconnected"
            else:
                print "Can't disconnect"


#This method is for connecting the buttons with a Wire from jack buttons menu
def on_connect(self,  input):
    print 'connected'
    jack_connector = self.sender().parent() #sender's parent of QAction should be the button
    #Create a Wire Connection between buttons
    print jack_connector #object
    print input #input name
    #Condition to check if the connection was already created
    #if wire_dic.get( input ) == None:
    if wire_dic.get( str(input.objectName())[4:] ) == None:
        #Run amixer command and checks returncode
        if amixer_command( input.controlName, jack_connector.controlName ) == 0:
            #Sets the tuple as the key and a Wire object as the value
            wire_dic[ str(input.objectName())[4:] ] =  ( str(jack_connector.objectName())[4:] ,  Wire(  jack_connector , input , None, scene),  )
            #Disable input in menu
            actions_dic[ str(input.objectName())[4:] ].setEnabled(False)
            print "Connection Sucessful"
        else:
            print "Connection Failed"
    print wire_dic
    
#Load Menu options for Jacks dragbuttons
#create sub-menus
submenus_dic = collections.OrderedDict()
submenus_dic['AIF1TX1_submenu'] = QMenu("AIF1TX1 (L) Record to RPi")
submenus_dic['AIF1TX2_submenu'] = QMenu("AIF1TX2 (R) Record to RPi")
submenus_dic['HPOUT1L_submenu'] = QMenu("HPOUT1 (L) Headset Output")
submenus_dic['HPOUT1R_submenu'] = QMenu("HPOUT1 (R) Headset Output")
submenus_dic['HPOUT2L_submenu'] = QMenu("HPOUT2 (L) Line Out")
submenus_dic['HPOUT2R_submenu'] = QMenu("HPOUT2 (R) Line Out")

#Create a actions ordered dictionary for Menu
actions_dic = collections.OrderedDict()
for input   in inputs_dic:
    #Create an Action
    actions_dic[ input  ] = QtGui.QAction( inputs_dic[ input ].controlName , None)
    # Connect every action to a slot()
    #actions_dic[ input ].triggered[()].connect( lambda input=input:  on_connect(actions_dic[ input  ], input )  )
    actions_dic[ input ].triggered[()].connect( lambda input=input:  on_connect(actions_dic[ input  ], inputs_dic[ input ] )  )

    
    #Condition to add actions to a submenu
    if input[:7] == 'AIF1TX1' :
        submenus_dic['AIF1TX1_submenu'].addAction( actions_dic[ input ] )
    
    if input[:7] == 'AIF1TX2' :
        submenus_dic['AIF1TX2_submenu'].addAction( actions_dic[ input ] )
    
    if input[:7] == 'HPOUT1L' :
        submenus_dic['HPOUT1L_submenu'].addAction( actions_dic[ input ] )
    
    if input[:7] == 'HPOUT1R' :
        submenus_dic['HPOUT1R_submenu'].addAction( actions_dic[ input ] )
    
    if input[:7] == 'HPOUT2L' :
        submenus_dic['HPOUT2L_submenu'].addAction( actions_dic[ input ] )
    
    if input[:7] == 'HPOUT2R' :
        submenus_dic['HPOUT2R_submenu'].addAction( actions_dic[ input ] )
    
    #Connect every input button to slot (on_link)
    inputs_dic[ input ].linked.connect( on_link )
    inputs_dic[ input ].mousepressed.connect( lambda: on_press(   inputs_dic[ input ] ) )

#Add SubMenus to Main Menu
for submenu in submenus_dic:
    menu.addMenu(submenus_dic[ submenu ] )

#Connect jack buttons press to on_press method
for jacks in jacks_dic:
    jacks_dic[ jacks ].mousepressed.connect( lambda: on_press(   jacks_dic[ jacks ] ) )
    #inputs_dic[ jacks ].mousepressed.connect( lambda: on_link(   jacks_dic[ jacks ] ) )


# Create the view using the scene
view = WiringGraphicsView(None, scene)
#view.resize(480,720)
view.show()
view.setWindowTitle("Wolfson Patchbay and Mixer")

app.exec_()
