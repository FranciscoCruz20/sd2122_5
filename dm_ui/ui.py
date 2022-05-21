
class Ui:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._f_matrix = []
        self._bomb_perc = 0

    def print_matrix(self):
        h = 1
        for w in range(self._width + 1):
            print(w, '', end='')
        print('')
        for block in self._matrix:
            print(h, *block)
            h += 1

    def create_fake_grid(self):
        self._matrix = [[chr(35) for x in range(self._width)] for y in range(self._height)]



    #Alterar para o lado do cliente
    #Quantidade de bombas entre 5% a 20% - Feito
    #Mandar coordenadas x - Feito
    #Mandar coordenadas y - Feito
    #Quando inseridas as coordenadas escolher entre - Abrir celula OU - Colocar bandeira - Feito
    #Por o print em loop junto com o acima menos as bombas

    def menu(self):
        print("Bem-Vindo ao Minesweeper!\n"
              "1 - Jogar\n"
              "2 - Ajuda\n"
              "3 - Quit\n")
        option = int(input("Introduza a sua opção: "))
        if option == 1:
            self._width = int(input("Valor minimo - 9 \n"
                                    "Valor Máximo - 24 \n"
                                    "Introduza o valor para a largura : "))
            while self._width < 9 or self._width > 24:
                self._width = int(input("Valor inesperado introduza novamente \n"
                                        "Valor minimo - 9 \n"
                                        "Valor Máximo - 24 \n "
                                        "Introduza o valor para a largura : "))
            self._height = int(input("Valor minimo - 9 \n"
                                     "Valor Máximo - 24 \n"
                                     "Introduza o valor para a altura : "))
            while self._height < 9 or self._height > 24:
                self._height = int(input("Valor inesperado introduza novamente \n"
                                         "Valor minimo - 9 \n"
                                         "Valor Máximo - 24 \n"
                                         "Introduza o valor para a altura : "))
            while self._bomb_perc > 20 or self._bomb_perc < 5:
                self._bomb_perc = int(input("Valor minimo - 5\n"
                                "Valor máximo - 20\n"
                                "Introduza a percentagem de bombas do tabuleiro : "))
            self.create_fake_grid()
            self.print_matrix()
            coord_x = 0
            coord_y = 0
            while coord_x > self._width or coord_x == 0:
                coord_x = int(input("Insira a coordenada X: "))
            while coord_y > self._height or coord_y == 0:
                coord_y = int(input("Insira a coordenada Y: "))
            choice = self.jogada()
            if choice == 'Open':
                self.check_around(coord_x-1,coord_y-1)
            if choice == 'Flag':
                self._matrix[coord_x-1][coord_y-1]='F'
            self.print_matrix()

    def check_around(self, x, y):
        range_values=[-1,0,1]
        if self._matrix[x][y]!='#':
            pass
        else:
            for i in range_values:
                for j in range_values:
                    if self._matrix[x+j][y+i] == '#':
                        self._matrix[x+j][y+i] = ' '


        if x+1!= self._width and y+1!= self._height:
            self.check_around(x,y+1)
            self.check_around(x+1,y)

    def jogada(self):

        choice = 0
        while choice > 2 or choice == 0:
            choice = int(input("Escolha uma ação\n"
                           " 1 - Abrir casa\n"
                           " 2 - Marcar com bandeira\n->"))

        if choice == 1:
            return 'Open'
        if choice == 2:
            return 'Flag'









obj = Ui()
obj.menu()