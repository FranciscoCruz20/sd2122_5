from stubs import GameServer
from sockets_mod import Socket

class Ui:
    """
    Interface de utilizador onde é disponibilizado tudo oque é recebido do servidor
    """

    def __init__(self, gameserver: GameServer):
        """
        :param gameserver:
        """
        self._server = gameserver
        self._width = 0
        self._height = 0
        self._f_matrix = []
        self._bomb_perc = 0
        self._tiles = 0

    def print_matrix(self):
        """
        Imprime a matriz(tabuleiro de jogo)
        :return:
        """
        h = 1
        for w in range(self._width + 1):
            print(w, '', end='')
        print('')
        for block in self._matrix:
            print(h, *block)
            h += 1

    def create_fake_grid(self):
        """
        Cria uma matriz falsa com o tamanho que o cliente quer
        :return:
        """
        self._matrix = [[chr(35) for x in range(self._width)] for y in range(self._height)]

    def menu(self):
        """
        chama a função register_name para validar e guardar o nome do cliente
        menu inicial, com inputs do tamanho do tabuleiro, percentagem de bombas
        chama create_fake_grid
        chama choice_play
        termina o jogo
        :return:
        """
        self.register_name()
        print("Bem-Vindo ao Minesweeper!\n"
              "1 - Jogar\n"
              "2 - Quit\n")
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
            self._tiles = self._server.create_grid(self._width,self._height,self._bomb_perc)
            self.create_fake_grid()
            self.choice_play()
            print("Game Ended")

    def choice_play(self):
        """
        input da casa selecionada pelo cliente
        opções de ações para a casa selcionada
        :return:
        """

        self.print_matrix()
        coord_x = 0
        coord_y = 0
        while coord_x > self._width or coord_x == 0:
            coord_x = int(input("Insira a coordenada X: "))
        while coord_y > self._height or coord_y == 0:
            coord_y = int(input("Insira a coordenada Y: "))
        choice = self.jogada()
        if choice == 'Open':
            pos_info_char = self._server.open_position(coord_y-1,coord_x-1)
            if pos_info_char == 0:
                zero_list = self._server.checking_in(coord_y,coord_x)
                self.check_around(zero_list)
                self.choice_play()
            elif pos_info_char == 9:
                self._matrix[coord_y - 1][coord_x - 1] = chr(184)
                print("Bomba encontrada - Score final = 0")
            elif self._tiles == 0 and pos_info_char != 9:
                print("Victory - ", self._server.scoring_out())
            else:
                self._matrix[coord_y - 1][coord_x - 1] = str(pos_info_char)

        elif choice == 'Flag':
            self._matrix[coord_y-1][coord_x-1]='F'
            self._server.flagging(coord_y,coord_x)
            self.choice_play()

        elif choice == 'FlagDelete':
            self._matrix[coord_y - 1][coord_x - 1] = '#'
            self._server.flagging(coord_y, coord_x)
            self.choice_play()


    def check_around(self, z_list: list):
        """
        Verificar as casas ao redor da selecionada
        :param z_list:
        :return:
        """
        total_len = len(z_list)
        total_len_div_2 = round(total_len / 2)
        cont = 0
        for i in range(0,total_len,2):
            if cont == total_len_div_2 :
                break
            else:
                self._matrix[z_list[i]][z_list[i + 1]] = ' '
                self._tiles -= 1
            cont += 1


    def jogada(self):
        """
        input da ação quando é selecionada uma casa do tabuleiro
        :return:
        """
        choice = 0
        while choice > 3 or choice == 0:
            choice = int(input("Escolha uma ação\n"
                           " 1 - Abrir casa\n"
                           " 2 - Marcar com bandeira\n"
                           " 3 - Apagar bandeira\n->"))

        if choice == 1:
            return 'Open'

        if choice == 2:
            return 'Flag'

        if choice == 3:
            return 'FlagDelete'

    def register_name(self):
        """
        input do nome do cliente
        envio do nome para o servidor, posteriormente para validação e registro
        :return:
        """
        name = (input("Digite o seu nome de jogador:"))
        self._server.send_name(name)

