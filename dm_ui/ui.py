class Ui:

    #Alterar para o lado do cliente
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
            while self._width < 9 and self._width > 24:
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