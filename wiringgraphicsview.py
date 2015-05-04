from PyQt4 import QtGui, QtCore
from random import randint

class WiringGraphicsView(QtGui.QGraphicsView):
    
    def __init__(self, parent = None,  scene=None):
        QtGui.QGraphicsView.__init__(self, scene, parent)
        #self.setAcceptDrops(True)
        #self.setScene(QtGui.QGraphicsScene(scene))
        #self.setSceneRect(QtCore.QRectF(self.viewport().rect()))
    
    def paintWire(self, start_widget,  end_widget):
        _start = start_widget.geometry()
        _end = end_widget.geometry()
#        print start_widget.pos()
#        print end_widget.pos()
        #brush = QtGui.QBrush(QtGui.QColor(255, 0, 0) )
        line = QtGui.QGraphicsLineItem(_start.x() + _start.width() / 2, _start.y() + _start.height() / 2, _end.x() + _end.width() / 2, _end.y() + _end.height() / 2)
        gradient = QtGui.QLinearGradient( 0, 0, 135)
        #gradient.setStart(5.5, 50)
        gradient.setColorAt(0.2,  QtGui.QColor(0, 0, 0) )
        gradient.setColorAt(0.5,  QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)) ) #Random color
        gradient.setColorAt(0.8, QtGui.QColor(0, 0, 0) )
        gradient.setCoordinateMode(0)
        gradient.setSpread(0)
        brush = QtGui.QBrush( gradient )
        pen = QtGui.QPen(brush, 5)        
        line.setPen(pen)
        #line.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.scene().addItem( line )
        
#        _start = start_widget.geometry()
#        _end = end_widget.geometry()
#        self.scene().addLine(_start.x() + _start.width() / 2, _start.y() + _start.height() / 2, _end.x() + _end.width() / 2, _end.y() + _end.height() / 2)
        

class Wire(QtGui.QGraphicsItem):
    
    def __init__(self, start_widget,  end_widget,  parent = None,  scene=None ):
        QtGui.QGraphicsItem.__init__(self, parent, scene)
        print start_widget.objectName()
        print end_widget.objectName()
        _start = start_widget.geometry()
        _end = end_widget.geometry()
        #Create a Line between the widgets
        self.line = QtGui.QGraphicsLineItem(_start.x() + _start.width() / 2, _start.y() + _start.height() / 2, _end.x() + _end.width() / 2, _end.y() + _end.height() / 2)
        #get top left rectangule of line
        x_position = self.line.boundingRect().topLeft().x()
        y_position = self.line.boundingRect().topLeft().y()
        
        #Create Gradient for Line
        gradient = QtGui.QLinearGradient()
        
        #Calculate diagonal of gradient with object's boundingRect coordinates
        if x_position < 0 and y_position > 0:
            gradient.setStart(0, 0)
            gradient.setFinalStop(1, 1)
        
        if x_position > 0 and y_position > 0:
            gradient.setStart(0, 1)
            gradient.setFinalStop(1, 0)

        if y_position < 0 and x_position < 0:
            gradient.setStart(0, 1)
            gradient.setFinalStop(1, 0)
        
        #set line object's boundingRect as coordinate mode for gradient
        gradient.setCoordinateMode(2)
        
        #Set Gradient Colors
        gradient.setColorAt(0.42,  QtGui.QColor(0, 0, 0) )
        gradient.setColorAt(0.49, QtGui.QColor(255, 255, 255) )
        gradient.setColorAt(0.53,  QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)) )
        
        gradient.setSpread(2)
        
        #Create a Brush
        brush = QtGui.QBrush( gradient )
        #Create Pen
        self.pen = QtGui.QPen(brush, 6)
        self.pen.setCapStyle(QtCore.Qt.RoundCap)
        #Set Pen to a Line
        self.line.setPen(self.pen)
        #self.line.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        #add line to the scene
        self.scene().addItem( self.line )
        
    def boundingRect(self):
        return QtCore.QRectF()
#        extra = (self.pen.width() + 20) / 2.0
#        p1 = self.line.p1()
#        p2 = self.line.p2()
#        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, option, widget=None):
        pass
    
    def clear(self):
        self.scene().removeItem( self.line)

class MyScene(QtGui.QGraphicsScene):
    def dragEnterEvent(self, e):
        e.acceptProposedAction()

    def dropEvent(self, e):
        # find item at these coordinates
        item = self.itemAt(e.scenePos())
        if isinstance(item, ProxyWidget):
            if item.acceptDrops() == True:
                # pass on event to item at the coordinates
                try:
                   item.dropEvent(e)
                except RuntimeError: 
                    pass #This will supress a Runtime Error generated when dropping into a widget with no ProxyWidget


    def dragMoveEvent(self, e):
        e.acceptProposedAction()

class ProxyWidget(QtGui.QGraphicsProxyWidget):  
    def dragEnterEvent(self, e):
        e.acceptProposedAction()

    def dropEvent(self, e):
        # pass drop event to child widget
        return self.widget().dropEvent(e)        

    def dragMoveEvent(self, e):
        e.acceptProposedAction()
