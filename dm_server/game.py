import random
import csv

class Minesweeper:
  """
  classe do jogo
  """
  def __init__(self):
    self._width = 9     #Minimo por default para width e height
    self._height = 9
    self._matrix = []
    self._bomb_coords = []
    self._tiles = 0
    self._score = 0
    self._flags = 0
    self._list_to_send = []
    self._flag_coords = []
    self._name_list = []

  def create_grid(self,x,y,bomb_perc):
    """
    cria a matriz(tabuleiro) no lado do servidor, que o cliente não consegue ver e que não está encriptada com "#"
    calcula também os valores das casas ao redor das bombas
    :param x
    :param y
    :param bomb_perc
    :return:tiles
    """
    self._width = x
    self._height = y
    self._matrix = [[0 for x in range(self._width)] for y in range(self._height)]
    bombs = (bomb_perc * 100) / (self._width * self._height)
    bombs = round(bombs)
    self._tiles = (self._width * self._height) - bombs
    for i in range(bombs):
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

    return self._tiles

  def conjoin_coords(self, x, y):
    """
    transforma as cooordenadsas numa string
    :param x
    :param y
    :return: string
    """
    return str(x + "," + y)

  def translate_coords(self, msg: str):
    """
    traduz as coordenadas
    :param msg:
    :return:
    """
    return

  def print_matrix(self):
    """
    dá print da matriz
    :return:
    """
    h = 1
    for w in range(self._width + 1):
        print(w, '', end='')
    print('')
    for block in self._matrix:
        print(h, *block)
        h += 1

  def get_flagged(self,x,y):
      """
      atríbui o score ao cliente dependendo se seleciona uma bomba ou não com uma flag
      :param x:
      :param y:
      :return:
      """
      if self._matrix[x][y] == 9:
          self._score += 1
      else:
          self._score -= 3

  def get_score(self):
      """
      dá return do score
      :return:score
      """
      return self._score

  def get_coord_value(self,x,y):
      """
      return dos valores da casa
      :param x:
      :param y:
      :return: matriz
      """
      return self._matrix[y][x]

  def check_around2(self, x, y):
      """
      verifica as casas de 0 no tabuleiro
      coloca as coordenadas das casas numa lista
      envia a lista
      :param x:
      :param y:
      :return:
      """
      # Para os limtes inferiores do tabuleiro

      if y == self._height - 1:
          if x == self._width - 1:
              if self._matrix[self._width - 1][self._height - 1] != 0:
                  pass
              else:
                  self._matrix[self._width - 1][self._height - 1] = ' '
                  self._list_to_send.append(self._width - 1)
                  self._list_to_send.append(self._height - 1)

              if self._matrix[self._width - 2][self._height - 1] != 0:
                  pass
              else:
                  self._matrix[self._width - 2][self._height - 1] = ' '
                  self._list_to_send.append(self._width - 2)
                  self._list_to_send.append(self._height - 1)

              if self._matrix[self._width - 1][self._height - 2] != 0:
                  pass
              else:
                  self._matrix[self._width - 1][self._height - 2] = ' '
                  self._list_to_send.append(self._width - 1)
                  self._list_to_send.append(self._height - 2)

              if self._matrix[self._width - 2][self._height - 2] != 0:
                  pass
              else:
                  self._matrix[self._width - 2][self._height - 2] = ' '
                  self._list_to_send.append(self._width - 2)
                  self._list_to_send.append(self._height - 2)



          elif x == 0:

              if self._matrix[0][self._height - 1] != 0:
                  pass
              else:
                  self._matrix[0][self._height - 1] = ' '
                  self._list_to_send.append(0)
                  self._list_to_send.append(self._height - 1)

              if self._matrix[1][self._height - 1] != 0:
                  pass
              else:
                  self._matrix[1][self._height - 1] = ' '
                  self._list_to_send.append(1)
                  self._list_to_send.append(self._height - 1)

              if self._matrix[0][self._height - 2] != 0:
                  pass
              else:
                  self._matrix[0][self._height - 2] = ' '
                  self._list_to_send.append(0)
                  self._list_to_send.append(self._height - 2)

              if self._matrix[1][self._height - 2] != 0:
                  pass
              else:
                  self._matrix[1][self._height - 2] = ' '
                  self._list_to_send.append(1)
                  self._list_to_send.append(self._height - 2)

      # Para os limtes superiores do tabuleiro
      elif y == 0:
          if x == self._width - 1:
              if self._matrix[self._width - 1][0] != 0:
                  pass
              else:
                  self._matrix[self._width - 1][0] = ' '
                  self._list_to_send.append(self._width - 1)
                  self._list_to_send.append(0)

              if self._matrix[self._width - 2][0] != 0:
                  pass
              else:
                  self._matrix[self._width - 2][0] = ' '
                  self._list_to_send.append(self._width - 2)
                  self._list_to_send.append(0)

              if self._matrix[self._width - 1][1] != 0:
                  pass
              else:
                  self._matrix[self._width - 1][1] = ' '
                  self._list_to_send.append(self._width - 1)
                  self._list_to_send.append(1)

              if self._matrix[self._width - 2][1] != 0:
                  pass
              else:
                  self._matrix[self._width - 2][1] = ' '
                  self._list_to_send.append(self._width - 2)
                  self._list_to_send.append(1)

          elif x == 0:
              if self._matrix[0][0] != 0:
                  pass
              else:
                  self._matrix[0][0] = ' '
                  self._list_to_send.append(0)
                  self._list_to_send.append(0)

              if self._matrix[1][0] != 0:
                  pass
              else:
                  self._matrix[1][0] = ' '
                  self._list_to_send.append(1)
                  self._list_to_send.append(0)
                  self.check_around2(1, 0)

              if self._matrix[0][1] != 0:
                  pass
              else:
                  self._matrix[0][1] = ' '
                  self._list_to_send.append(0)
                  self._list_to_send.append(1)
                  self.check_around2(0, 1)

              if self._matrix[1][1] != 0:
                  pass
              else:
                  self._matrix[1][1] = ' '
                  self._list_to_send.append(1)
                  self._list_to_send.append(1)
                  self.check_around2(1, 1)

          else:
              if self._matrix[x][0] != 0:
                  pass
              else:
                  self._matrix[x][0] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(0)

              if self._matrix[x - 1][0] != 0:
                  pass
              else:
                  self._matrix[x - 1][0] = ' '
                  self._list_to_send.append(x - 1)
                  self._list_to_send.append(0)

              if self._matrix[x + 1][0] != 0:
                  pass
              else:
                  self._matrix[x + 1][0] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(0)


      elif x != 0 and x != self._width - 1 and y != 0 and y != self._height - 1:
          # Centro
          try:
              if self._matrix[x][y] == 0:
                  self._matrix[x][y] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y)
                  self.check_around2(x, y)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y))
              pass

          # Centro Direito
          try:
              if self._matrix[x + 1][y] == 0:
                  self._matrix[x + 1][y] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(y)
                  self.check_around2(x + 1, y)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x+1) + ' Y = ' + str(y))
              pass

          # Centro Esquerdo
          try:
              if self._matrix[x - 1][y] == 0:
                  self._matrix[x - 1][y] = ' '
                  self._list_to_send.append(x - 1)
                  self._list_to_send.append(y)
                  self.check_around2(x - 1, y)
              else:
                  pass

          except IndexError:
              # print('X = ' + str(x-1) + ' Y = ' + str(y))
              pass

          # Baixo Meio
          try:
              if self._matrix[x][y + 1] == 0:
                  self._matrix[x][y + 1] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y + 1)
                  self.check_around2(x, y + 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y+1))
              pass

          # Baixo Esquerda
          try:
              if self._matrix[x - 1][y + 1] == 0:
                  self._matrix[x - 1][y + 1] = ' '
                  self._list_to_send.append(x - 1)
                  self._list_to_send.append(y + 1)
                  self.check_around2(x - 1, y + 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x-1) + ' Y = ' + str(y+1))
              pass

          # Baixo Direita
          try:
              if self._matrix[x + 1][y + 1] == 0:
                  self._matrix[x + 1][y + 1] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(y + 1)
                  self.check_around2(x + 1, y + 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x+1) + ' Y = ' + str(y+1))
              pass

          # Cima meio
          try:
              if self._matrix[x][y - 1] == 0:
                  self._matrix[x][y - 1] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y - 1)
                  self.check_around2(x, y - 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y-1))
              pass

          # Cima direita
          try:
              if self._matrix[x + 1][y - 1] == 0:
                  self._matrix[x + 1][y - 1] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(y - 1)
                  self.check_around2(x + 1, y - 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x+1) + ' Y = ' + str(y-1))
              pass

          # Cima Esquerda
          try:
              if self._matrix[x - 1][y - 1] == 0:
                  self._matrix[x - 1][y - 1] = ' '
                  self._list_to_send.append(x - 1)
                  self._list_to_send.append(y - 1)
                  self.check_around2(x - 1, y - 1)
              else:
                  pass

          except IndexError:
              # print('X = ' + str(x-1) + ' Y = ' + str(y-1))
              pass

      elif x == 0 and y != 0 or y != self._height - 1:
          try:
              if self._matrix[x + 1][y] == 0:
                  self._matrix[x + 1][y] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(y)
                  self.check_around2(x + 1, y)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x+1) + ' Y = ' + str(y))
              pass

          try:
              if self._matrix[x][y - 1] == 0:
                  self._matrix[x][y - 1] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y - 1)
                  self.check_around2(x, y - 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y-1))
              pass

          try:
              if self._matrix[x][y + 1] == 0:
                  self._matrix[x][y + 1] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y + 1)
                  self.check_around2(x, y + 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y+1))
              pass

      elif x != 0 and y == 0 or y != self._height - 1:
          try:
              if self._matrix[x + 1][y] == 0:
                  self._matrix[x + 1][y] = ' '
                  self._list_to_send.append(x + 1)
                  self._list_to_send.append(y)
                  self.check_around2(x + 1, y)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x + 1) + ' Y = ' + str(y))
              pass

          try:
              if self._matrix[x][y] == 0:
                  self._matrix[x][y] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y)
                  self.check_around2(x, y)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y))
              pass

          try:
              if self._matrix[x][y + 1] == 0:
                  self._matrix[x][y + 1] = ' '
                  self._list_to_send.append(x)
                  self._list_to_send.append(y + 1)
                  self.check_around2(x, y + 1)
              else:
                  pass
          except IndexError:
              # print('X = ' + str(x) + ' Y = ' + str(y + 1))
              pass

  def get_list_to_send(self):
      """
      envia a lista com coordenadas das casas com zeros
      :return: list_to_send
      """
      return self._list_to_send

  def file_read_write(self, a: str):
    """
    lê o ficheiro csv dos nomes dos jogadores
    escreve os nomes dos mesmo caso sejam válidos
    :param a: nome
    :return:
    """
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


