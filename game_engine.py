from player import Player
import math

class GameEngine():

    def __init__(self, world, gamesave, player_1, player_2):
        self.world = world
        self.gamesave = gamesave
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_turn = 1

    def get_current_turn(self):
        return self.current_turn

    def get_current_player(self):
        if self.current_turn == 1:
            return self.player_1
        if self.current_turn == 2:
            return self.player_2

    def get_opposite_player(self):
        if self.current_turn == 2:
            return self.player_1
        if self.current_turn == 1:
            return self.player_2

    def turn_done(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1

    def check_own_character(self, character):
        if character in self.get_current_player().character_list:
            return True
        return False

    def execute_moving(self, char, direction):
        '''
        Funktiolla liikutetaan hahmoa.

        return - 0 = Success, -1 = Not success
        '''
        if not char in self.get_current_player().character_list:
            return -1

        can_move = self.get_current_player().move(self.world, char, direction)
        if can_move == False:
            print("You can't move that direction, try again!")
            return -1

        self.turn_done()
        return 0

    def execute_attacking(self, char, target):
        '''
        Funktiolla lyödään toista hahmoa.

        return - 0 = success, 1 = killed, 2 = victorious, -1 = Not success
        '''
        if not char in self.get_current_player().character_list:
            return -1

        if not target in self.get_opposite_player().character_list:
            return -1
        

        can_attack = self.get_current_player().can_attack(char, target, self.get_opposite_player())
        if can_attack == True:
            self.turn_done()
            return 0
        elif can_attack == "already_eliminated":
            return -2
        elif can_attack == "killed":
            return 1
        elif can_attack == "defeated":
            return 2
        else:
            print("Your target is too far!")
            return -1

    def bot_actions(self):
        try:
            b_list = self.get_current_player().get_character_list()
            p_list = self.get_opposite_player().get_character_list()

            bot_c = None

            if self.get_current_player().last_played == "archer":
                for b in b_list:
                    if b.character_type == "giant":
                        bot_c = b
                        break
                    else:
                        bot_c = b_list[0]

            elif self.get_current_player().last_played == "giant":
                for b in b_list:
                    if b.character_type == "fighter":
                        bot_c = b
                        break
                    else:
                        bot_c = b_list[-1]

            elif self.get_current_player().last_played == "fighter":
                for b in b_list:
                    if b.character_type == "archer":
                        bot_c = b
                        break
                    else:
                        bot_c = b_list[0]

            self.get_current_player().last_played = bot_c.character_type
            moved = self.get_current_player().name + " moved " + self.get_current_player().last_played

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
                can_attack = self.get_current_player().can_attack(bot_c, pl_c, self.get_opposite_player())
                turn_done = True
                if can_attack == True:
                    print(self.get_current_player().name + " hit " + pl_c.character_type + "!")
                    self.turn_done()
                    return pl_c, 5
                elif can_attack == "killed":
        
                    return pl_c, 3
                    print(self.get_current_player().name + " eliminated " + pl_c.character_type + "!")
                elif can_attack == "defeated":
                    self.turn_done()
                    return pl_c, 4
                    print(self.get_current_player().name + " defeated " + self.get_opposite_player().name + "!")
                    print(self.get_current_player().name + " is Victorious!!!")

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
                can_move = self.get_current_player().move(self.world, bot_c, direction)
                if can_move == False:
                    for d in dir_list:
                        can_move = self.get_current_player().move(self.world, bot_c, d)
                        if can_move == True:
                            break
            self.turn_done()
            return pl_c, 5
        except:
            self.turn_done()
            return self.get_opposite_player, 5

    def save_game(self, filename):
        self.gamesave.load_p1_characters(self.player_1.get_character_list())
        self.gamesave.load_p2_characters(self.player_2.get_character_list())
        self.gamesave.save_game(filename)
        print("Game saved. See you soon!")