import random

class Minesweeper:

  def __init__(self):
    self._width = 9     #Minimo por default para width e height
    self._height = 9
    self._matrix = []
    self._bomb_coords = []

  def create_grid(self):
    self._matrix = [[chr(35) for x in range(self._width)] for y in range(self._height)]
    bomb_perc = random.randrange(5,24)
    bomb_perc = (bomb_perc * 100) / (self._width * self._height)
    for i in range(round(bomb_perc)):
        x_rng = random.randrange(0,self._width)
        y_rng = random.randrange(0,self._height)
        conj = self.conjoin_coords(x_rng,y_rng)
        if conj not in self._bomb_coords:
            self._bomb_coords.append(conj)

    #Continuar

  def print_matrix(self):
    h=1
    for w in range(self._width + 1):
        print(w, '', end='')
    print('')
    for block in self._matrix:
        print(h,*block)
        h+=1

  def conjoin_coords(self, x, y):
    return str(x + "," + y)

  #Alterar provavelmente remover
  def menu(self):
    print("Bem-Vindo ao Minesweeper!\n"
          "1 - Jogar\n"
          "2 - Ajuda\n"
          "3 - Quit\n")
    option = int(input("Introduza a sua opção: "))
    if option == 1:
        self._width = int(input("Valor minimo - 9 \n"
                                "Valor Máximo - 24 \n "
                                "Introduza o valor para a largura : "))
        while self._width < 9 and self._width > 24 :
            self._width = int(input("Valor inesperado introduza novamente"
                                    "Valor minimo - 9 \n"
                                    "Valor Máximo - 24 \n "
                                    "Introduza o valor para a largura : "))
        self._height = int(input("Valor minimo - 9 \n"
                                "Valor Máximo - 24 \n "
                                "Introduza o valor para a altura : "))
        while self._height < 9 and self._height > 24:
            self._height = int(input("Valor inesperado introduza novamente"
                                    "Valor minimo - 9 \n"
                                    "Valor Máximo - 24 \n "
                                    "Introduza o valor para a altura : "))
        self.create_grid()


