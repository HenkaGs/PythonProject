from PyQt5 import QtWidgets, QtGui, QtCore

class SquareGraphicsItem(QtWidgets.QGraphicsRectItem):
    '''
    Luokka luo grafiikan pelikentän ruuduille.
    '''
    def __init__(self, square, mouse_click_handler, *args, **kwargs):
        super(SquareGraphicsItem, self).__init__(*args, **kwargs)
        self.square = square
        self.mouse_click_handler = mouse_click_handler
        self.set_brush()


    def set_brush(self):
        '''
        Värittää nurmikkoruudut (vapaat) vihreäksi ja
        kiviruudut (ei vapaat) harmaaksi.
        '''
        if self.square.draw == 3:
            self.setBrush(QtGui.QColor(124,252,0))
        else:
            self.setBrush(QtGui.QColor(220,220,220))

    def mousePressEvent(self, *args, **kwargs):
        '''
        Antaa ruudulle ominaisuuden klikata sitä.
        '''
        self.mouse_click_handler(self.square)