from stubs import GameServer, PORT, SERVER_ADDRESS
from ui import Ui


def main():
    """
    Função principal do programa, corrida após o main do lado do servidor
    """
    gameserver = GameServer(SERVER_ADDRESS, PORT)
    gaming = Ui(gameserver)
    gaming.menu()


main()