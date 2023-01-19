from world import World
from character import Character
from player import Player
from savegame import Game
from game_engine import GameEngine
import math
from gui import GUI

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main():
    '''
    Main luo pelin ja juoksee peliä.
    '''
    def __init__(self):
        '''
        Alustaa pelikentän
        '''
        self.test_world = World(7,8)

        # Aseta kivet
        self.test_world.set_obstacle("rocks", 3, 3)
        self.test_world.set_obstacle("rocks", 1, 6)
        self.test_world.set_obstacle("rocks", 1, 3)
        self.test_world.set_obstacle("rocks", 3, 4)
        self.test_world.set_obstacle("rocks", 7, 5)
        self.test_world.set_obstacle("rocks", 6, 3)
        self.test_world.set_obstacle("rocks", 4, 5)

        self.game = Game(None, None, None)

        select = False
        while select == False:
            start = input("Hey, create new game 'n' or continue last game 'l'")
            if start == "n" or start == "l":
                select = True
            else:
                select = False


        if start == "n":
            chosen = False
            while chosen is False:
                bot = input("Choose one '1' or two '2' players")
                if bot == '1' or bot == '2':
                    chosen = True

            # Luo pelaajan 1
            player_1_name = input("Player 1 name: ")
            self.player_1 = Player(player_1_name)
            self.player_1.number = 1


            giant = Character(6, 8)
            giant.set_as_giant(200)
            self.test_world.set_character(giant)
            self.player_1.add_character(giant)
            
            fighter = Character(4, 8)
            fighter.set_as_fighter(150)
            self.test_world.set_character(fighter)
            self.player_1.add_character(fighter)

            archer = Character(2, 8)
            archer.set_as_archer(100)
            self.test_world.set_character(archer)
            self.player_1.add_character(archer)
            
            # Luo pelaajan 2
            if bot == "1":
                player_2_name = "Sane_bot"
                self.player_2 = Player(player_2_name)
                self.player_2.is_bot = True
            else:
                player_2_name = input("Player 2 name: ")
                self.player_2 = Player(player_2_name)
            self.player_2.number = 2
            
            giant = Character(2, 1)
            giant.set_as_giant(200)
            self.test_world.set_character(giant)
            self.player_2.add_character(giant)

            fighter = Character(4, 1)
            fighter.set_as_fighter(150)
            self.test_world.set_character(fighter)
            self.player_2.add_character(fighter)
            
            archer = Character(6, 1)
            archer.set_as_archer(100)
            self.test_world.set_character(archer)
            self.player_2.add_character(archer)
            
        
        elif start == "l":
            self.game.load_save()

            # Luo pelaajan 1 tallennuksesta
            self.player_1 = self.game.p1_saved_name
            self.player_1 = Player(self.player_1)
            self.player_1.number = 1

            if self.game.p1_giant_hp != 0:
                giant = Character(self.game.p1_giant_loc[1], self.game.p1_giant_loc[0])
                giant.set_as_giant(self.game.p1_giant_hp)
                self.test_world.set_character(giant)
                self.player_1.add_character(giant)

            if self.game.p1_fighter_hp != 0:
                fighter = Character(self.game.p1_fighter_loc[1], self.game.p1_fighter_loc[0])
                fighter.set_as_fighter(self.game.p1_fighter_hp)
                self.test_world.set_character(fighter)
                self.player_1.add_character(fighter)

            if self.game.p1_archer_hp != 0:
                archer = Character(self.game.p1_archer_loc[1], self.game.p1_archer_loc[0])
                archer.set_as_archer(self.game.p1_archer_hp)
                self.test_world.set_character(archer)
                self.player_1.add_character(archer)
            
            # Luo pelaajan 2 tallennuksesta
            self.player_2 = self.game.p2_saved_name
            self.player_2 = Player(self.player_2)
            self.player_2.number = 2
            self.player_2.is_bot = self.game.saved_as_bot
            
            if self.game.p2_giant_hp != 0:
                giant = Character(self.game.p2_giant_loc[1], self.game.p2_giant_loc[0])
                giant.set_as_giant(self.game.p2_giant_hp)
                self.test_world.set_character(giant)
                self.player_2.add_character(giant)

            if self.game.p2_fighter_hp != 0:
                fighter = Character(self.game.p2_fighter_loc[1], self.game.p2_fighter_loc[0])
                fighter.set_as_fighter(self.game.p1_fighter_hp)
                self.test_world.set_character(fighter)
                self.player_2.add_character(fighter)
            
            if self.game.p2_archer_hp != 0:
                archer = Character(self.game.p2_archer_loc[1], self.game.p2_archer_loc[0])
                archer.set_as_archer(self.game.p1_archer_hp)
                self.test_world.set_character(archer)
                self.player_2.add_character(archer)


        # Luo pelin tallennuksen
        self.game = Game(self.player_1.name, self.player_2.name, self.player_2.is_bot)

        self.game_engine = GameEngine(self.test_world, self.game, self.player_1, self.player_2)

        #printtaa pelaajat ja heidän hahmot
        print("Players: \n")
        print(self.player_1.name)
        for charac in self.player_1.get_character_list():
            print(charac.character_type)
        print(" ")

        print(self.player_2.name)
        for charac in self.player_2.get_character_list():
            print(charac.character_type)

        print("\nGame ready.")
        self.out()

    def out(self):
        '''
        Funktio tulostaa pelin.
        '''
        self.test_world.out()

    def determine_character(self, player):
        '''
        Funktiossa valitaan hahmo jolla tehdään seuraava toiminto. 
        '''
        chara_type = None
        typ = False
        while typ != True:
            chara_type = input("Player " + str(player.number) + ", select character: ")
            for i in player.get_character_list():
                if chara_type == i.character_type:
                    typ = True
                    break
            else:
                print("Wrong command or character is eliminated! Type character you want to move.")
        
        return player.get_chara(chara_type)

    def execute_moving(self, player, char):
        '''
        Funktiolla liikutetaan hahmoa.
        '''
        turn_done = False
        while not turn_done:
            direction = input("choose direction: ")
            if direction == "n" or direction == "e" or direction == "s" or direction == "w":
                can_move = player.move(self.test_world, char, direction)
                if can_move == False:
                    print("You can't move that direction, try again!")
                else:
                    turn_done = True
            else:
                print("Wrong move command, try again!")

    def execute_attacking(self, player, opposite_player, char):
        '''
        Funktiolla lyödään toista hahmoa.
        '''
        turn_done = False
        while not turn_done:
            target = input("Choose your target! ")
            if target == "giant" or target == "fighter" or target == "archer":
                target_character = opposite_player.get_chara(target)
                can_attack = player.can_attack(char, target_character, opposite_player)
                if can_attack == True:
                    print("You hit enemy " + target + "!")
                    turn_done = True
                elif can_attack == "already_eliminated":
                    print(target + " is already eliminated! Try again.")
                    self.turn(player, opposite_player)
                    turn_done = True
                elif can_attack == "killed":
                    print("You eliminated " + target + "!")
                    turn_done = True
                elif can_attack == "defeated":
                    print("You defeated " + opposite_player.name + "!")
                    print(player.name + " is Victorious!!!")
                    turn_done = True
                    return True
                else:
                    print("Your target is too far!")
                    self.turn(player, opposite_player)
                    turn_done = True
            else:
                print("Wrong attacking command, try again!")
        return False
        
    def turn(self, player, opposite_player):
        '''
        Funktio päätetään kuka tekee ja mitä.
        '''
        char = self.determine_character(player)
        next_move = input("Choose, 'move' or 'attack': ")
        if next_move == "move":
            self.execute_moving(player, char)
        elif next_move == "attack":
            return self.execute_attacking(player, opposite_player, char)
        else:
            print("Wrong command! Try again.")
            self.turn(player, opposite_player)
        return False

    def bot_actions(self, bot, player):
        '''
        Funktiossa määritetään botin seuraava toiminta laskemalla botin etäisyys
        kohteesta ja siitä määrittämällä liikkuuko botti vai lyökö botti
        vihollista riippuen etäisyydestä. Jos Botti ei pysty liikkua ruutuun,
        joka on lähinpänä kohdetta, valitaan seuraavaksi liikkumisruudut
        järjestyksessä south, east, west tai north.
        '''
        
        b_list = bot.get_character_list()
        p_list = player.get_character_list()

        if bot.last_played == "archer":
            for b in b_list:
                if b.character_type == "giant":
                    bot_c = b
                    break
                else:
                    bot_c = b_list[0]

        elif bot.last_played == "giant":
            for b in b_list:
                if b.character_type == "fighter":
                    bot_c = b
                    break
                else:
                    bot_c = b_list[-1]

        elif bot.last_played == "fighter":
            for b in b_list:
                if b.character_type == "archer":
                    bot_c = b
                    break
                else:
                    bot_c = b_list[0]

        bot.last_played = bot_c.character_type
        moved = bot.name + " moved " + bot.last_played

        if bot_c.character_type == "giant" or bot_c.character_type == "archer":
            for p in p_list:
                if p.character_type == "giant":
                    pl_c = p
                    break
                else:
                    pl_c = p_list[0]

        elif bot_c.character_type == "fighter":
            for p in p_list:
                if p.character_type == "fighter":
                    pl_c = p
                    break
                else:
                    pl_c = p_list[0]
            
        in_range = bot_c.range

        d_x_north = bot_c.location[1] - pl_c.location[1]
        d_y_north = bot_c.location[0] - 1 - pl_c.location[0]

        dis_north = math.sqrt(d_x_north ** 2 + d_y_north ** 2)

        d_x_east = bot_c.location[1] + 1 - pl_c.location[1]
        d_y_east = bot_c.location[0] - pl_c.location[0]

        dis_east = math.sqrt(d_x_east ** 2 + d_y_east ** 2)

        d_x_south = bot_c.location[1] - pl_c.location[1]
        d_y_south = bot_c.location[0] + 1 - pl_c.location[0]

        dis_south = math.sqrt(d_x_south ** 2 + d_y_south ** 2)

        d_x_west = bot_c.location[1] - 1 - pl_c.location[1]
        d_y_west = bot_c.location[0] - pl_c.location[0]

        dis_west = math.sqrt(d_x_west ** 2 + d_y_west ** 2)

        d_x_range = bot_c.location[1] - pl_c.location[1]
        d_y_range = bot_c.location[0] - pl_c.location[0]

        dis_range = math.sqrt(d_x_range ** 2 + d_y_range ** 2)

        turn_done = False
        if in_range >= dis_range:
            can_attack = bot.can_attack(bot_c, pl_c, player)
            turn_done = True
            if can_attack == True:
                print(bot.name + " hit " + pl_c.character_type + "!")
            elif can_attack == "killed":
                print(bot.name + " eliminated " + pl_c.character_type + "!")
            elif can_attack == "defeated":
                print(bot.name + " defeated " + player.name + "!")
                print(bot.name + " is Victorious!!!")
                return True
        elif dis_north <= dis_east and dis_north <= dis_south and dis_north <= dis_west:
            direction = "n"
        elif dis_east <= dis_north and dis_east <= dis_south and dis_east <= dis_west:
            direction = "e"
        elif dis_south <= dis_north and dis_south <= dis_east and dis_south <= dis_west:
            direction = "s"
        elif dis_west <= dis_north and dis_west <= dis_south and dis_west <= dis_east:
            direction = "w"

        if turn_done == False:
            print(moved)
            dir_list = ["s", "e", "w", "n"]
            can_move = bot.move(self.test_world, bot_c, direction)
            if can_move == False:
                for d in dir_list:
                    can_move = bot.move(self.test_world, bot_c, d)
                    if can_move == True:
                        break


    def run_game(self):
        '''
        Funktio pyörittää peliä.
        '''
        game = True
        victory = False
        while game == True:
            command = input("Press enter to continue, write 's' to save and quit or 'q' for exit: ")
            if command == "q":
                print("Game over")
                game = False

            elif command == "s":
                filename = input("Write your savefile name: ")
                self.game.load_p1_characters(self.player_1.get_character_list())
                self.game.load_p2_characters(self.player_2.get_character_list())
                self.game.save_game(filename)
                print("Game saved. See you soon!")
                game = False

            else:
                victory = self.turn(self.player_1, self.player_2)
                if victory:
                    self.out()
                    print("Game over!")
                    break
                self.out()
                if not self.player_2.is_bot:
                    victory = self.turn(self.player_2, self.player_1)
                else:
                    victory = self.bot_actions(self.player_2, self.player_1)
                if victory:
                    self.out()
                    print("Game over!")
                    break

            self.out()
        
    def open_gui(self):
        '''
        Funktioa avaa ja käynnistää gui sovelluksen.
        '''
        
        global app 
        app = QApplication(sys.argv)
        gui = GUI(self.test_world, self.player_1, self.player_2, self.game_engine)

        sys.exit(app.exec_())

    def run(self):
        '''
        Funktiossa voidaan päättää juostaanko peli printtinä vai graafisen liitymän kautta.
        '''
        self.run_game()
        self.open_gui()


main = Main()
main.run()