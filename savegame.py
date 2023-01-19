import json
from character import Character

class Game():
    '''
    Luokka luo pelitallennuksen.
    '''
    def __init__(self, p1_name, p2_name, is_bot):
        
        self.p1_name = p1_name
        self.p2_name = p2_name

        self.is_bot = is_bot
        self.saved_as_bot = False

        self.p1_characters = []
        self.p2_characters = []

        self.p1_saved_name = None
        self.p2_saved_name = None

        self.p1_giant_hp = None
        self.p1_giant_loc = None

        self.p2_giant_hp = None
        self.p2_giant_loc = None

        self.p1_fighter_hp = None
        self.p1_fighter_loc = None

        self.p2_fighter_hp = None
        self.p2_fighter_loc = None

        self.p1_archer_hp = None
        self.p1_archer_loc = None

        self.p2_archer_hp = None
        self.p2_archer_loc = None



    def load_p1_characters(self, c_list):
        '''
        Lataa pelaajan 1 pelihahmot listana.
        '''
        for char in c_list:
            self.p1_characters.append(char)


    def load_p2_characters(self, c_list):
        '''
        Lataa pelaajan 2 pelihahmot listana.
        '''
        for char in c_list:
            self.p2_characters.append(char)


    def save_game(self, filename):
        '''
        Tallentaa pelaajien hahmot, niiden elämänpisteiden määrän 
        ja niiden sijainnin koordinaatit.
        '''
        
        file = open(filename + ".json", 'w')
        data = dict()
        p1_giant = [0,[0,0]]
        p2_giant = [0,[0,0]]
        p1_fighter = [0,[0,0]]
        p2_fighter = [0,[0,0]]
        p1_archer = [0,[0,0]]
        p2_archer = [0,[0,0]]

        for character in self.p1_characters:
            if character.character_type == "giant":
                p1_giant = [character.health, character.get_s_location()]
            elif character.character_type == "fighter":
                p1_fighter = [character.health, character.get_s_location()]
            elif character.character_type == "archer":
                p1_archer = [character.health, character.get_s_location()]

        for character in self.p2_characters:
            if character.character_type == "giant":
                p2_giant = [character.health, character.get_s_location()]
            elif character.character_type == "fighter":
                p2_fighter = [character.health, character.get_s_location()]
            elif character.character_type == "archer":
                p2_archer = [character.health, character.get_s_location()]

        data['players'] = [{'name': self.p1_name, 'giant': p1_giant, 'fighter': p1_fighter, 'archer': p1_archer}, 
        {'name': self.p2_name, 'giant': p2_giant, 'fighter': p2_fighter, 'archer': p2_archer, 'is_bot': self.is_bot}]

        json.dump(data, file, indent=4)

    def load_save(self):
        '''
        Lataa tallennuksesta edellisen pelin ja antaa 
        pelin tiedot Main luokkaan joka luo sitten pelin
        tallennuksen tiedoilla.
        '''
        filename = input("Write files name you want to open:")
        try:
            with open(filename + ".json") as f:
                data = json.load(f)

        except:
            print("Save not found, saveme file opened!")
            with open("saveme" + ".json") as f:
                data = json.load(f)

        self.p1_saved_name = data['players'][0]['name']
        self.p2_saved_name = data['players'][1]['name']

        self.p1_giant_hp = data['players'][0]['giant'][0]
        self.p1_giant_loc = data['players'][0]['giant'][1]

        self.p2_giant_hp = data['players'][1]['giant'][0]
        self.p2_giant_loc = data['players'][1]['giant'][1]

        self.p1_fighter_hp = data['players'][0]['fighter'][0]
        self.p1_fighter_loc = data['players'][0]['fighter'][1]

        self.p2_fighter_hp = data['players'][1]['fighter'][0]
        self.p2_fighter_loc = data['players'][1]['fighter'][1]

        self.p1_archer_hp = data['players'][0]['archer'][0]
        self.p1_archer_loc = data['players'][0]['archer'][1]

        self.p2_archer_hp = data['players'][1]['archer'][0]
        self.p2_archer_loc = data['players'][1]['archer'][1]

        self.saved_as_bot = data['players'][1]['is_bot']
