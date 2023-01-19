import math
class Direction():
    '''
    Luokka tekee hahmon siirron jos mahdollista.
    '''

    def __init__(self, location, direction, width, height):
        self.width = width
        self.height = height
        self.location = location
        self.direction = direction

    def calculate_new_location(self):
        '''
        Määrittää uuden sijainnin hahmolle.
        '''
        if self.direction == "n":
            y = self.location[0] - 1
            x = self.location[1]
            return x, y

        if self.direction == "e":
            y = self.location[0]
            x = self.location[1] + 1
            return x, y

        if self.direction == "s":
            y = self.location[0] + 1
            x = self.location[1]
            return x, y

        if self.direction == "w":
            y = self.location[0]
            x = self.location[1] - 1
            return x, y

    def new_direction(self, grid, char):
        '''
        Tarkistaa voiko suuntaan liikkua.
        '''
        x, y = self.calculate_new_location()
        if x < 0 or y < 0:
            return False
        if x >= self.width or y >= self.height:
            return False

        if self.check_square(grid[y][x]) == False:
            char.set_new_location(y, x)
            grid[y][x].set_character(char)
            grid[self.location[0]][self.location[1]].remove_body()
            return True
        else:
            return False

    def check_square(self, grid_location):
        '''
        Tarkistaa onko ruutu vapaa mihin halutaan liikkua.
        '''
        if grid_location.is_wall() == False:
            return False
        
    @staticmethod
    def calculate_direction_qui(character, square):
        '''
        Määrittää onko klikattu suunta
        north, east, south vai west suunta.
        '''
        d_x = character.location[1] - square.location[1]
        d_y = character.location[0] - square.location[0]

        if d_y == -1 and d_x == 0:
            return "s"
        elif d_y == 1 and d_x == 0:
            return "n"
        elif d_x == 1 and d_y == 0:
            return "w"
        elif d_x == -1 and d_y == 0:
            return "e"
        else:
            return -1
   