import random

class Minesweeper:

  def __init__(self):
    self._width = 9     #Minimo por default para width e height
    self._height = 9
    self._matrix = []
    self._bomb_coords = []
    self._flags = 0
    self._flag_coords = []

  def create_grid(self):
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

  def print_matrix(self):
    self.create_grid()
    h = 1
    for w in range(self._width + 1):
        print(w, '', end='')
    print('')
    for block in self._matrix:
        print(h, *block)
        h += 1

  def get_jogada(self,x,y,jogada):
      if jogada == 'Open':
           pass
      if jogada == 'Flag':
          self._matrix[x][y] = 'F'
          self._flags += 1
          self._flag_coords.append(self.conjoin_coords(x,y))


obj_temp = Minesweeper()
obj_temp.print_matrix()