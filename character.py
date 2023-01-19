import math

class Character():
    '''
    Luokka luo pelihahmot kentälle.
    '''

    def __init__(self, x, y):
        self.character_type = "human"
        self.health = 100
        self.attack_dmg = 30
        self.range = 1.0
        self.draw = 7
        self.location = [y - 1, x - 1]
        self.square = None

    def out(self):
        '''
        Tulostaa pelihahmot omailla kuvioillaan.
        '''
        return str(self.draw)

    def get_location(self):
        '''
        Palauttaa hahmon koordinaatit y, x pelikentällä.
        '''
        return self.location

    def get_s_location(self):
        '''
        Palauttaa hahmon sijainnin tallennusta varten,
        tässä y, x koordinaatit kirjoitetaan ykkösestä
        ylöspäin eikä nollasta jolloin sijainti on 
        helpompi lukea.
        '''
        s_loc = self.get_location()
        s_location = [s_loc[0] + 1, s_loc[1] + 1]
        return s_location

    def set_new_location(self, y, x):
        '''
        Asettaa uuden sijainnin hahmolle.
        '''
        self.location = [y, x]

    def get_character(self):
        '''
        Palauttaa hahmon.
        '''
        return self.character_type

    def set_as_giant(self, hp):
        '''
        Luo hahmon giant.
        '''
        self.character_type = "giant"
        self.health = hp
        self.attack_dmg = 30
        self.range = math.sqrt(7.9)
        self.draw = 7

    def set_as_fighter(self, hp):
        '''
        Luo hahmon fighter.
        '''
        self.character_type = "fighter"
        self.health = hp
        self.attack_dmg = 50
        self.range = math.sqrt(2)
        self.draw = 8

    def set_as_archer(self, hp):
        '''
        Luo hahmon archer.
        '''
        self.character_type = "archer"
        self.health = hp
        self.attack_dmg = 40
        self.range = math.sqrt(8)
        self.draw = 9

    def attack_target(self, target, opposite_player):
        '''
        Määrittää kuka lyö kuinka isolla vahingolla ketä.
        '''
        return target.take_damage(self.attack_dmg, target, opposite_player)

    def take_damage(self, damage, target, opposite_player):
        '''
        Poistaa kohteelta elämänpisteitä lyöjän vahingon verran.
        '''
        self.health -= damage
        if self.health <= 0:
            return opposite_player.remove_character(target)
        else:
            return True

