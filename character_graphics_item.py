from PyQt5 import QtWidgets, QtGui, QtCore
class CharacterGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    '''
    Luo grafiikan jokaiselle hahmolle.
    '''
    def __init__(self, character, square_size, mouse_click_handler):
        super(CharacterGraphicsItem, self).__init__()
        self.character = character
        self.square_size = square_size
        brush = QtGui.QBrush(1)
        self.setBrush(brush)
        self.constructTriangleVertices()
        self.updateAll()
        self.mouse_click_handler = mouse_click_handler

    def constructTriangleVertices(self):
        '''
        Luo hahmot kolmioiksi.
        '''
        triangle = QtGui.QPolygonF()

        triangle.append(QtCore.QPointF(self.square_size/2, 0)) 
        triangle.append(QtCore.QPointF(0, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size, self.square_size))
        triangle.append(QtCore.QPointF(self.square_size/2, 0))

        self.setPolygon(triangle)

        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)

    def updateAll(self):
        '''
        Päivittää hahmojen sijainnin ja värityksen
        updatePosition() ja updateColor() funktion avulla.
        '''
        self.updatePosition()
        self.updateColor()

    def updatePosition(self):
        '''
        Päivittää hahmojen sijainnin.
        '''
        x_coordinate = self.character.get_location()[1]
        y_coordinate = self.character.get_location()[0]
        self.setPos(x_coordinate * self.square_size, y_coordinate * self.square_size)

    def updateColor(self):
        '''
        Värittää hahmot omilla väreillä.
        '''
        if self.character.draw == 7:
            self.setBrush(QtGui.QColor(0,100,0))
        elif self.character.draw == 8:
            self.setBrush(QtGui.QColor(169,169,169))
        elif self.character.draw == 9:
            self.setBrush(QtGui.QColor(255,248,220))
        
    def mousePressEvent(self, *args, **kwargs):
        '''
        Antaa hahmolle ominaisuuden klikata sitä.
        '''
        self.mouse_click_handler(self.character)