class Square():
    '''
    Luokka määrittää minkälainen ruutu pelikentässä on kyse.
    '''
    def __init__(self, x, y):
        '''
        Oletus ruutu on ruohikko, eikä ole este.
        '''
        self.obstacle_type = "grass"
        self.draw = 3
        self.wall = False
        self.character = None
        self.location = [y, x]
 
    def out(self):
        '''
        Printtaa ruudut omailla kuvioillaan.
        '''
        if self.character != None:
            return self.character.out()
        else:
            return str(self.draw)

    def is_wall(self):
        '''
        Palauttaa onko ruutu vapaa vai ei.
        '''
        return self.wall or self.character != None

    def set_as_rock(self):
        '''
        Asettaa ruutuun kivet.
        '''
        self.obstacle_type = "rocks"
        self.draw = 0
        self.wall = True

    def get_character(self):
        '''
        Palauttaa ruudussa olevan hahmon.
        '''
        return self.character

    def set_character(self, character):
        '''
        Asettaa ruutuun hahmon.
        '''
        self.character = character
        self.character.square = self

    def remove_body(self):
        '''
        Vapauttaa ruudun jos hahmo kuolee kyseisessä ruudussa.
        '''
        self.character = None