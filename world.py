from square import Square
from direction import Direction

class World():
    '''
    Luokka luo maailman, asettaa esteet ja pelihahmot paikalleen.
    '''

    def __init__(self, width, height):
        '''
        Luo pelikentän.
        '''
        self.width = width
        self.height = height
        self.all_characters = []
        self.grid = []
        for i in range(0, height):
            row = []
            for j in range(0, width):
                row.append(Square(j, i))
            self.grid.append(row)

    def get_width(self):
        '''
        Palauttaa ruudukon leveyden.
        '''
        return self.width

    def get_height(self):
        '''
        Palauttaa ruudukon korkeuden.
        '''
        return self.height

    def get_square(self, x, y):
        '''
        Palauttaa pyydetyn ruudun objektin.
        '''
        return self.grid[y][x]

    def get_characters(self):
        '''
        Palauttaa kaikki pelikentällä olevat hahmot.
        '''
        return self.all_characters

    def get_grid(self):
        '''
        Palauttaa pelikentän.
        '''
        return self.grid

        
    def set_obstacle(self, obstacle_type, x, y):
        '''
        Asettaa esteet pelikentälle.
        '''
        if obstacle_type == "rocks":
            self.grid[y-1][x-1].set_as_rock()


    def set_character(self, character):
        '''
        Asettaa pelihahmot pelikentälle.
        '''
        location = character.get_location()
        self.grid[location[0]][location[1]].set_character(character)
        self.all_characters.append(character)

    def out(self):
        '''
        Tulostaa pelin tällä hetkellä printtinä.
        '''
        for row in self.grid:
            str_row = "[ "
            for place in row:
                str_row += place.out() + " "
            print(str_row + "]")
    
    def move_character(self, char, direction):
        '''
        Funktio liikuttaa pelihahmoja.
        '''
        if char.character_type == "giant":
            location = char.get_location()
            dire = Direction(location, direction, self.width, self.height)
            return dire.new_direction(self.grid, char)
        
        if char.character_type == "fighter":
            location = char.get_location()
            dire = Direction(location, direction, self.width, self.height)
            return dire.new_direction(self.grid, char)

        if char.character_type == "archer":
            location = char.get_location()
            dire = Direction(location, direction, self.width, self.height)
            return dire.new_direction(self.grid, char)
