import random
import csv

class Minesweeper:

    def __init__(self):
        self._width = 9     #Minimo por default para width e height
        self._height = 9
        self._matrix = []
        self._bomb_coords = []
        self._score = 0
        self._flags = 0
        self._flag_coords = []

    def create_grid(self,x,y):
        self._width = x
        self._height = y
        self._matrix = [[0 for x in range(self._width)] for y in range(self._height)]
        bomb_perc = random.randrange(5,24)
        bomb_perc = (bomb_perc * 100) / (self._width * self._height)
        for i in range(round(bomb_perc)):
            x_rng = random.randrange(0,self._width)
            y_rng = random.randrange(0,self._height)
            conj = self.conjoin_coords(str(x_rng),str(y_rng))
            if conj not in self._bomb_coords:
                self._matrix[y_rng][x_rng] = 9
                self._bomb_coords.append(conj)
            #Calcular o valores das casas ao redor da bomba
                if (x_rng >=0 and x_rng <= self._width-2) and (y_rng >= 0 and y_rng <= self._height-1) and self._matrix[y_rng][x_rng + 1] != 9:
                    self._matrix[y_rng][x_rng + 1] += 1 # center right

                if (x_rng >=1 and x_rng <= self._width-1) and (y_rng >= 0 and y_rng <= self._height-1) and self._matrix[y_rng][x_rng - 1] != 9:
                    self._matrix[y_rng][x_rng - 1] += 1  # center left

                if (x_rng >= 1 and x_rng <= self._width-1) and (y_rng >= 1 and y_rng <= self._height) and self._matrix[y_rng - 1][x_rng - 1] != 9:
                    self._matrix[y_rng - 1][x_rng - 1] += 1  # top left

                if (x_rng >= 0 and x_rng <= self._height-2) and (y_rng >= 1 and y_rng <= self._height-1) and self._matrix[y_rng - 1][x_rng + 1] != 9:
                    self._matrix[y_rng - 1][x_rng + 1] += 1  # top right

                if (x_rng >= 0 and x_rng <= self._height-1) and (y_rng >= 1 and y_rng <= self._height-1) and self._matrix[y_rng - 1][x_rng] != 9:
                    self._matrix[y_rng - 1][x_rng] += 1  # top center

                if (x_rng >=0 and x_rng <= self._height-2) and (y_rng >= 0 and y_rng <= self._height-2) and self._matrix[y_rng + 1][x_rng + 1] != 9:
                    self._matrix[y_rng + 1][x_rng + 1] += 1  # bottom right

                if (x_rng >= 1 and x_rng <= self._height-1) and (y_rng >= 0 and y_rng <= self._height-2) and self._matrix[y_rng + 1][x_rng - 1] != 9:
                    self._matrix[y_rng + 1][x_rng - 1] += 1  # bottom left

                if (x_rng >= 0 and x_rng <= self._height-1) and (y_rng >= 0 and y_rng <= self._height-2) and self._matrix[y_rng + 1][x_rng] != 9:
                    self._matrix[y_rng + 1][x_rng] += 1  # bottom center

    def conjoin_coords(self, x, y):
        return str(x + "," + y)

    def translate_coords(self, msg: str):
        return

    def print_matrix(self):
        h = 1
        for w in range(self._width + 1):
            print(w, '', end='')
        print('')
        for block in self._matrix:
            print(h, *block)
            h += 1

    def get_flagged(self,x,y):
        if self._matrix[x][y] == 9:
            self._score += 1
        else:
            self._score -= 3

    def get_coord_value(self,x,y):
        return self._matrix[y][x]

    def check_around(self, y, x):
        range_values = [-1, 0, 1]
        position = self._matrix[x][y]
        print(position)
        if x == self._width or y == self._height:
            if self._matrix[x][y] == 0:
                self._matrix[x][y] = ' '

        else:
            if position !=0:
                pass
            counter = 0
            try:
                if self._matrix[x][y] != 0 and self._matrix[x+1][y] != 0 and self._matrix[x-1][y] != 0 and self._matrix[x-1][y+1] != 0 and self._matrix[x-1][y-1] != 0 and self._matrix[x][y-1] != 0 and self._matrix[x+1][y-1] != 0 and self._matrix[x+1][y+1] != 0 and self._matrix[x][y+1] != 0:
                    print("Stop")
            except IndexError:
                pass
            else:
                while counter < 9:
                    for i in range_values:
                        for j in range_values:
                            next_x = x + j
                            next_y = y + i
                            if next_x == self._width:
                                next_x -= 1
                            if next_x < 0:
                                next_x += 1
                            if next_y == self._height:
                                next_y -= 1
                            if next_y < 0:
                                next_y += 1
                            if self._matrix[next_x][next_y] == 0:
                                self._matrix[next_x][next_y] = ' '

                            counter += 1
            self.check_around(x + 1, y + 1)

    def check_around2(self, y, x):


        # Centro
        try:
            if self._matrix[x][y] == 0:
                self._matrix[x][y] = ' '
                self.check_around2(x, y)
        except IndexError:
            print('X = ' + str(x) + ' Y = ' + str(y))

        #Centro Direito
        try:
            if self._matrix[x+1][y] == 0:
                self._matrix[x+1][y] = ' '
                self.check_around2( x+ 1, y)
        except IndexError:
            print('X = ' + str(x+1) + ' Y = ' + str(y))
        #Centro Esquerdo
        try:
            if self._matrix[x-1][y] == 0:
                self._matrix[x-1][y] = ' '
                self.check_around2(x - 1, y)
        except IndexError:
            print('X = ' + str(x-1) + ' Y = ' + str(y))
        #Baixo Meio
        try:
            if self._matrix[x][y+1] == 0:
                self._matrix[x][y+1] = ' '
                self.check_around2(x, y + 1)
        except IndexError:
            print('X = ' + str(x) + ' Y = ' + str(y+1))
        #Baixo Esquerda
        try:
            if self._matrix[x-1][y+1] == 0:
                self._matrix[x-1][y+1] = ' '
                self.check_around2(x - 1, y + 1)
        except IndexError:
            print('X = ' + str(x-1) + ' Y = ' + str(y+1))
        #Baixo Direita
        try:
            if self._matrix[x+1][y+1] == 0:
                self._matrix[x+1][y+1] = ' '
                self.check_around2(x + 1, y + 1)
        except IndexError:
            print('X = ' + str(x+1) + ' Y = ' + str(y+1))

        #Cima meio
        try:
            if self._matrix[x][y-1] == 0:
                self._matrix[x][y-1] = ' '
                self.check_around2(x, y - 1)
        except IndexError:
            print('X = ' + str(x) + ' Y = ' + str(y-1))
        #Cima direita
        try:
            if self._matrix[x+1][y-1] == 0:
                self._matrix[x+1][y-1] = ' '
                self.check_around2(x + 1, y - 1)
        except IndexError:
            print('X = ' + str(x+1) + ' Y = ' + str(y-1))
        #Cima Esquerda
        try:
            if self._matrix[x-1][y-1] == 0:
                self._matrix[x-1][y-1] = ' '
                self.check_around2(x - 1, y - 1)
        except IndexError:
            print('X = ' + str(x-1) + ' Y = ' + str(y-1))


    def exit(self):
        print("Yeet")

#Srry queria testar os nomes depois tira pra testares
obj_temp = Minesweeper()
obj_temp.create_grid(9,9)
obj_temp.print_matrix()

x_test = int(input('Cord X'))
y_test = int(input('Cord Y'))
obj_temp.check_around2(x_test-1,y_test-1)
obj_temp.print_matrix()


def file_read_write(a: str):
    name_not_here = False
    with open('Nomes_Jogadores', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if a in row:
                name_not_here = True
    with open('Nomes_Jogadores', 'a', newline='') as csvfile:
        if name_not_here == False:
            writer = csv.writer(csvfile)
            writer.writerow([a])
    csvfile.close()

#file_read_write("Mariense")