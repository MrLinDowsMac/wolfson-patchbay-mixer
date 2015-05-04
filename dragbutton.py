from PyQt4 import QtGui, QtCore

class DragButton(QtGui.QPushButton):
    
    #linked = QtCore.pyqtSignal(str, str)
    linked = QtCore.pyqtSignal(object, object)
    mousepressed = QtCore.pyqtSignal()
    
    def __init__(self, parent = None):
         super(DragButton,  self).__init__(parent)
         self.allowDrag = True
         self.controlName = ""
         
    
    def setControlName(self, name):
        self.controlName = name

    def controlName(self):
        return self.controlName

    def setAllowDrag(self, allowDrag):
        if type(allowDrag) == bool:
           self.allowDrag = allowDrag
        else:
            raise TypeError("You have to set a boolean type")
            
    
    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return QtGui.QPushButton.mouseMoveEvent(self, e)

        if self.allowDrag == True:
            
            # write the relative cursor position to mime data
            mimeData = QtCore.QMimeData()
            origin_widget = self.objectName()
            mimeData.setText(origin_widget)
            #print mimeData.text()
    
            # let's make it fancy. we'll show a "ghost" of the button as we drag
            # grab the button to a pixmap
            pixmap = QtGui.QPixmap.grabWidget(self)
    
            # below makes the pixmap half transparent
            painter = QtGui.QPainter(pixmap)
            painter.setCompositionMode(painter.CompositionMode_DestinationIn)
            painter.fillRect(pixmap.rect(), QtGui.QColor(0, 0, 0, 127))
            painter.end()
    
            # make a QDrag
            drag = QtGui.QDrag(self)
            # put our MimeData
            drag.setMimeData(mimeData)
            # set its Pixmap
            drag.setPixmap(pixmap)
            # shift the Pixmap so that it coincides with the cursor position
            drag.setHotSpot(e.pos())
            
            # start the drag operation
            # exec_ will return the accepted action from dropEvent
            if drag.exec_(QtCore.Qt.LinkAction | QtCore.Qt.MoveAction) == QtCore.Qt.LinkAction:
                print 'linked'
            else:
                print 'moved'
                
        return QtGui.QPushButton.mouseMoveEvent(self, e)    


    def mousePressEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'
            #AQUI DEBO IMPLEMENTAR EL MENU CONTEXTUAL
            self.mousepressed.emit()
            return QtGui.QPushButton.mousePressEvent(self, e)
#        if e.button() == QtCore.Qt.RightButton:
#            self.mouseMoveEvent(e)

    def dragEnterEvent(self, event):
        event.accept()
        return QtGui.QPushButton.dragEnterEvent(self, event)

    def dragLeaveEvent(self, event):
        print "leave"
        self.dragOver = False
        self.update()

    def dropEvent(self, e):
        # get the relative position from the mime data
        #mime = e.mimeData().text()
        #print mime
        print e.source().objectName()
        print self.objectName()
        # e.source().move(e.pos()-QtCore.QPoint(x, y))
            # set the drop action as LinkAction
        e.setDropAction(QtCore.Qt.LinkAction)
        # tell the QDrag we accepted it
        e.accept()
        #Emit linked signal with the names of the source and received objects as parameters
        #self.linked.emit( self.objectName() ,  e.source().objectName() )
        self.linked.emit( self ,  e.source() )
        return QtGui.QPushButton.dropEvent(self, QtGui.QDropEvent(QtCore.QPoint(e.pos().x(), e.pos().y()), e.possibleActions(), e.mimeData(), e.buttons(), e.modifiers()))

#    @QtCore.pyqtSlot(str)
#    def on_connect(self, str):
#        print'linked ' + self.sender().objectName() + ' and ' + self.objectName()
#        print 'ok'
