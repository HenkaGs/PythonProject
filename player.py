import math
class Player():
    '''
    Luokka määrittää pelaajat
    '''
    def __init__(self, name):
        self.name = name
        self.character_list = []
        self.number = 0
        self.is_bot = False
        self.last_played = "archer"

    def add_character(self, character):
        '''
        Lisää pelihahmon pelaajalle.
        '''
        self.character_list.append(character)

    def remove_character(self, character):
        '''
        Poistaa pelaajalta pelihahmon.
        '''
        character.square.remove_body()
        self.character_list.remove(character)
        if len(self.character_list) == 0:
            return "defeated"
        else:
            return "killed"

    def attack(self, attacker, target, opposite_player):
        '''
        Määrittää kumpi pelaaja lyö toista pelaajaa ja mitä hahmoa.
        '''
        return attacker.attack_target(target, opposite_player)
    
    def get_character_list(self):
        '''
        Palauttaa pelaajan hahmot.
        '''
        return self.character_list
    
    def move(self, world, char, direction):
        '''
        Liikuttaa pelaajan hahmoa.
        '''
        return world.move_character(char, direction)

    def get_chara(self, chara_type):
        '''
        Palauttaa tietyn hahmon pelaajalta.
        '''
        for i in self.character_list:
            if i.character_type == chara_type:
                return i
        return False

    def can_attack(self, attacker, target, opposite_player):
        '''
        Määrittää voiko pelaaja lyödä tiettyä vastustajan hahmoa.
        '''
        if target == None:
                return "already_eliminated"
        else:
            d_x = attacker.location[1] - target.location[1]
            d_y = attacker.location[0] - target.location[0]
            distance = math.sqrt(d_x ** 2 + d_y ** 2)
            if distance <= attacker.range:
                enemy_survived = self.attack(attacker, target, opposite_player)
                if enemy_survived == True:
                    return True
                else:
                    return enemy_survived
                
            else:
                return False

