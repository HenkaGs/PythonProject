from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from character_graphics_item import CharacterGraphicsItem
from square_graphics_item import SquareGraphicsItem
from character import Character
from direction import Direction


class GUI(QtWidgets.QMainWindow):
    '''
    GUI luo grafiikat pelille ja juoksee peliä.
    Peliä pelataan klikkaamalla hiirellä hahmoja ja ruutuja.
    '''

    def __init__(self, world, p1, p2, game_engine):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.world = world
        self.square_size = 50
        self.p1 = p1
        self.p2 = p2
        self.game_engine = game_engine
        self.selected_character = None
        self.turn_label = None
        self.player_1_label = None
        self.player_2_label = None
        self.message_label = None
        self.added_characters = []
        self.added_gui_items = []
        self.init_window()
        self.init_grid()
        self.character_graphics()
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_characters)
        self.timer.start(10)
        
    def set_selected_square(self, square):
        '''
        Funktiossa määritetään mihin ruutuun halutaan liikkua
        klikkaamalla ensin hahmoa ja sitten kyseistä ruutua.
        Klikkaamalla ruutua, ikkunaan printataan mikä ruudun sijainti 
        on koordinaatistossa [x,y].

        Jos vastustaja on botti,
        kutsutaan bot_actions() funktiota heti pelaajan liikeen jälkeen
        jolloin botti pelaa heti liikkeensä.
        '''
        self.message_info("Clicked square: " + "[ " + str(square.location[1] + 1) + " , " + str(square.location[0] + 1) + " ]")
        if self.selected_character == None:
            self.message_info("Character not selected.")
            return

        new_dir = Direction.calculate_direction_qui(self.selected_character, square)
        if new_dir == -1:
            self.message_info("You can't move there")
            self.selected_character = None
            return
        self.game_engine.execute_moving(self.selected_character, new_dir)
        self.selected_character = None
        if self.p2.is_bot is True and self.game_engine.get_current_turn() == 2:
            pl_c, bot_result = self.game_engine.bot_actions()
            if bot_result == 3:
                self.remove_character_item(pl_c)
                self.message_info(self.p2.name + " eliminated " + pl_c.character_type)
                self.game_engine.bot_actions()
            elif bot_result == 4:
                self.remove_character_item(pl_c)
                self.message_info(self.p2.name + " defeated " + self.p1.name)

    def init_grid(self):
        '''
        Funktiossa piirretään pelikentän ruudukko luokan
        SquareGraphicsItem avulla.
        
        '''
        for x in range(self.world.get_width()):
            for y in range(self.world.get_height()):
                square = self.world.get_square(x, y)
                item = SquareGraphicsItem(square, self.set_selected_square, x * self.square_size, y * self.square_size, self.square_size, self.square_size)
                self.scene.addItem(item)

    def set_selecteted_character(self, character):
        '''
        Funktiossa määritetään hahmo klikkaamalla kyseistä hahmoa.
        Seuraavaksi voidaan liikkua klikkaamalla viereistä ruutua tai 
        lyödä klikkaamalla vastustajan hahmoa. 
        
        Jos vastustaja on botti,
        kutsutaan bot_actions() funktiota heti pelaajan liikeen jälkeen
        jolloin botti pelaa heti liikkeensä.
        '''
        self.message_info("Clicked character: " + character.character_type)
        if not self.game_engine.check_own_character(character) and self.selected_character is None:
            self.message_info("Not you character.")
            return
        if self.selected_character is None:
            self.selected_character = character
            return

        result = self.game_engine.execute_attacking(self.selected_character, character)

        if result == 0:
            self.message_info("You hit enemy " + character.character_type + "!")
            if self.p2.is_bot is True and self.game_engine.get_current_turn() == 2:
                pl_c, bot_result = self.game_engine.bot_actions()
                if bot_result == 3:
                    self.remove_character_item(pl_c)
                    self.message_info(self.p2.name + " eliminated " + pl_c.character_type)
                elif bot_result == 4:
                    self.remove_character_item(pl_c)
                    self.message_info(self.p2.name + " defeated " + self.p1.name)
                
        elif result == -2:
            self.message_info(character.character_type + " is already eliminated! Try again.")
        elif result == -1:
            self.message_info("Your target is too far!")
            self.selected_character = None
            return
        elif result == 1:
            self.remove_character_item(character)
            self.message_info("You eliminated " + character.character_type + "!")
            if self.p2.is_bot is True and self.game_engine.get_current_turn() == 2:
                pl_c, bot_result = self.game_engine.bot_actions()
                if bot_result == 3:
                    self.remove_character_item(pl_c)
                    self.message_info(self.p2.name + " eliminated " + pl_c.character_type)
                    self.game_engine.bot_actions()
                elif bot_result == 4:
                    self.remove_character_item(pl_c)
                    self.message_info(self.p2.name + " defeated " + self.p1.name)

        if result == 2:
            self.remove_character_item(character)
            self.message_info("You defeated " + self.game_engine.get_opposite_player().name + "!")
            self.message_info(self.game_engine.get_current_player().name + " is Victorious!!!")
            self.game_engine.turn_done()
        self.selected_character = None


    def remove_character_item(self, character):
        '''
        Funktion avulla poistetaan hahmo pelikentältä
        kun hahmo eliminoidaan.
        '''
        char_item = None
        for item in self.added_gui_items:
            if item.character == character:
                char_item = item
        self.scene.removeItem(char_item)
        self.added_gui_items.remove(char_item)

    def character_graphics(self):
        '''
        Funktiolla luodaan hahmoille grafiikka pelikentälle
        CharacterGraphicsItem luokan avulla.
        '''
        for character in self.world.get_characters():
            if not character in self.added_characters:
                new_character = CharacterGraphicsItem(character, self.square_size, self.set_selecteted_character)
                self.scene.addItem(new_character)
                self.added_characters.append(character)
                self.added_gui_items.append(new_character)

    def update_characters(self):
        '''
        Päivittää hahmojen sijainnit pelikentällä.
        '''
        for character_item in self.added_gui_items:
            character_item.updateAll()

        self.game_info()
        self.turn_info()



    def game_info(self):
        '''
        Funktiossa luodaan tekstit ikkunaan kuten tiedot hahmoista,
        paljonko heillä on elämänpisteitä vielä jäljellä ja
        mitä milläkin hetkellä on tehty.
        '''
        giant = self.game_engine.player_1.get_chara('giant')
        if giant:
            giant = giant.health
        else:
            giant = 0
        fighter = self.game_engine.player_1.get_chara('fighter')
        if fighter:
            fighter = fighter.health
        else:
            fighter = 0
        archer = self.game_engine.player_1.get_chara('archer')
        if archer:
            archer = archer.health
        else:
            archer = 0
        if self.player_1_label is None:
            self.player_1_label = QtWidgets.QLabel(self)

        self.player_1_label.setText("Player 1: {} \nGiant hp: {} \nFigther hp: {}\nArcher hp: {}".format(
            self.game_engine.player_1.name,
            giant, fighter, archer))

        self.player_1_label.move(420,50)
        self.player_1_label.adjustSize()

        giant = self.game_engine.player_2.get_chara('giant')
        if giant:
            giant = giant.health
        else:
            giant = 0
        fighter = self.game_engine.player_2.get_chara('fighter')
        if fighter:
            fighter = fighter.health
        else:
            fighter = 0
        archer = self.game_engine.player_2.get_chara('archer')
        if archer:
            archer = archer.health
        else:
            archer = 0
        if self.player_2_label is None:
            self.player_2_label = QtWidgets.QLabel(self)

        self.player_2_label.setText("Player 2: {} \nGiant hp: {} \nFigther hp: {}\nArcher hp: {}".format(
            self.game_engine.player_2.name,
            giant, fighter, archer))

        self.player_2_label.move(420,120)
        self.player_2_label.adjustSize()

        self.character_info = QtWidgets.QLabel(self)
        self.character_info.setText("Characters info at start:\nGiant, health: 200, attack damage: 30, range: medium\nFighter, health: 150, attack damage: 50, range: short\nArcher, health: 100, attack damage: 40, range: long")
        self.character_info.move(420,300)
        self.character_info.adjustSize()

        self.how_to_play = QtWidgets.QLabel(self)
        self.how_to_play.setText("Eliminate your opponents characters to win!\nWhen you eliminate enemy character, you get extra turn.")
        self.how_to_play.move(420, 400)
        self.how_to_play.adjustSize()

        
    def message_info(self, message):
        '''
        Tällä funktiolla voidaan päivittää ajankohtainen
        teksti.
        '''
        if self.message_label is None:
            self.message_label = QtWidgets.QLabel(self)
        self.message_label.setText(message)
        self.message_label.move(420,250)
        self.message_label.adjustSize()

    def turn_info(self):
        '''
        Tässä luodaan teksti mikä kertoo tämän hetkisen
        pelaajan vuoron.
        '''
        if self.turn_label is None:
            self.turn_label = QtWidgets.QLabel(self)
        self.turn_label.setText("Player {} turn \nSelect move or attack!".format(
            self.game_engine.current_turn
        ))
        self.turn_label.move(420,200)
        self.turn_label.adjustSize()

    def button_clicked(self):
        '''
        Tässä luodaan tallennus nappi, millä voidaan
        tallentaa peli, jotta sitä voidaan jatkaa myöhemmin.
        '''
        filename, okPressed = QtWidgets.QInputDialog.getText(self, "Save Game","Filename:", QtWidgets.QLineEdit.Normal, "saveme")
        if okPressed and filename != '':
            self.game_engine.save_game(filename)

    def init_window(self):
        '''
        Funktiossa luodaan ikkuna peliä varten.
        '''
        self.game_info()  
        self.turn_info()
        self.message_info("Game started!")     

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Save Game!")
        self.b1.move(50,500)
        self.b1.clicked.connect(self.button_clicked)

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Strategy Game')
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)