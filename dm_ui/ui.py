class Ui:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._f_matrix = []

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
    #Quantidade de bombas entre 5% a 20%
    #Mandar coordenadas x
    #Mandar coordenadas y
    #Quando inseridas as coordenadas escolher entre - Abrir celula OU - Colocar bandeira
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
            self.create_fake_grid()
            self.print_matrix()

obj = Ui()
obj.menu()