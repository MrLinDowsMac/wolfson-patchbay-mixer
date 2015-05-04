from PyQt4.QtGui import *
from PyQt4.QtCore import *
from dragbutton import DragButton
from wiringgraphicsview import *
import collections

import icons_rc

app = QApplication([])

scene = MyScene()
menu = QMenu()
widget_container = QWidget()

#dictonaries for dragbuttons (used later for connecting them)
jacks_dic = {}
inputs_dic = collections.OrderedDict()
wire_dic = {}

#AIF1RX (PLAYBACK CONTROLS)

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


#AIF1TX (RECORD INPUTS)

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
record_playback_layouts = QHBoxLayout(widget_container)
record_playback_layouts.addLayout(AIF1RX_main_layout)
record_playback_layouts.addLayout(AIF1TX_main_layout)
#widget_container.setFixedWidth(290)

widget_scene = scene.addWidget(widget_container)

# Instantiate our own proxy which forwars drag/drop events to the child widget
#of AIFTX

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

#TODO: Implement method to trigger amixer command:

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
            #Input name as key, and a tuple( jack name, a new instance of Wire ) as value.
            #wire_dic[  str(input)[4:] ] = ( str(jack)[4:] , Wire(  widget_container.findChild( DragButton,  jack) , widget_container.findChild( DragButton, input ) , None, scene))
            wire_dic[  str(input.objectName())[4:] ] = ( str(jack.objectName())[4:] , Wire( jack , input , None, scene))
            #TODO: Put the call to the method that calls the amixer command
            #Disable input option in menu
            print actions_dic
            #actions_dic[ str(input)[4:] ].setEnabled(False)
            actions_dic[ str(input.objectName())[4:] ].setEnabled(False)
    print wire_dic

def on_press(self):
    #Condition checks if receiving object is a button receives that Drops. If is false it means that is Jack connector dragbutton
    if self.sender().acceptDrops() == False:
        print self.sender()
        for action in actions_dic:
            #Set parent every QAction after click
            actions_dic[ action ].setParent(self.sender())
    
    elif self.sender().acceptDrops() == True: #is for inputs, mouse press should disconnect any connection to them
        input =  str(self.sender().objectName())[4:]
        #if wire_dic[]
        #print connection
        if wire_dic.get( input ) != None:
            #Clear line
            wire_dic[ input ][1].clear()
            #Delete object reference by deleting key
            del wire_dic[ input ]
            #Enable the input in the menu
            actions_dic[ input ].setEnabled(True)
        


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
        #Sets the tuple as the key and a Wire object as the value
        #wire_dic[ input ] =  ( str(jack_connector.objectName())[4:] ,  Wire(  jack_connector , widget_container.findChild( DragButton,  'btn_' + input ) , None, scene),  )
        wire_dic[ str(input.objectName())[4:] ] =  ( str(jack_connector.objectName())[4:] ,  Wire(  jack_connector , input , None, scene),  )
        #TODO: Put the call to the method that calls the amixer command
        #Disable input in menu
        #actions_dic[ input ].setEnabled(False)
        actions_dic[ str(input.objectName())[4:] ].setEnabled(False)
        print wire_dic
    
#Load Menu options for Jacks dragbuttons
#create sub-menus
submenus_dic = collections.OrderedDict()
submenus_dic['AIF1TX1_submenu'] = QMenu("AIF1TX1 (L) Record to RPi")
submenus_dic['AIF1TX2_submenu'] = QMenu("AIF1TX2 (R) Record to RPi")

#Create a actions ordered dictionary for Menu
actions_dic = collections.OrderedDict()
for input   in inputs_dic:
    #Create an Action
    actions_dic[ input  ] = QtGui.QAction( inputs_dic[ input ].controlName , None)
    # Connect every action to a slot()
    #actions_dic[ input ].triggered[()].connect( lambda input=input:  on_connect(actions_dic[ input  ], input )  )
    actions_dic[ input ].triggered[()].connect( lambda input=input:  on_connect(actions_dic[ input  ], inputs_dic[ input ] )  )

    
    #Condition to add actions to a submenu
    if input[:-2] == 'AIF1TX1' :
        submenus_dic['AIF1TX1_submenu'].addAction( actions_dic[ input ] )
    
    if input[:-2] == 'AIF1TX2' :
        submenus_dic['AIF1TX2_submenu'].addAction( actions_dic[ input ] )
        
    
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
#view.resize(640, 480)
view.show()
view.setWindowTitle("Wolfson Connector and Mixer")
#and paint a wire between those buttons
#wire_dic['wire_1'] = Wire(btn_AIF1RX1, btn_AIF1TX2_4, None, scene)
#wire_dic['wire_1'].clear()
#del wire_dic['wire_1']

#wire1 = Wire(btn_AIF1RX1, btn_AIF1TX2_4, None, scene)
#wire2 = Wire(button4, button3, None, scene)
#wire1.clear()
#wire1 = None
#view.paintWire(button1, button2)
#view.paintWire(button4, button3)

app.exec_()
