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
    self._name_list = []

  def create_grid(self,x,y,bomb_perc):
    self._width = x
    self._height = y
    self._matrix = [[0 for x in range(self._width)] for y in range(self._height)]
    bombs = (bomb_perc * 100) / (self._width * self._height)
    for i in range(round(bombs)):
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

  def check_around(self, x, y):
      range_values = [-1, 0, 1]
      if self._matrix[x][y] != '0':
          pass
      else:
          for i in range_values:
              for j in range_values:
                  if self._matrix[x + j][y + i] == '0':
                      self._matrix[x + j][y + i] = ' '
      if x + 1 != self._width and y + 1 != self._height:
          self.check_around(x, y + 1)
          self.check_around(x + 1, y)
          if x + 1 != self._width and y + 1 != self._height:
            self.check_around(x, y + 1)
            self.check_around(x + 1, y)

  def file_read_write(self, a: str):
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


