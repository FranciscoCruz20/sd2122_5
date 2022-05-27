from game import Minesweeper
from skeletons import GameServer, PORT


def main():
    """
    Função principal do programa do lado do server, corrida primeiro que o main do lado do cliente
    """
    GameServer(PORT,Minesweeper()).run()


main()
