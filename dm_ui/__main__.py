from stubs import GameServer, PORT, SERVER_ADDRESS
from ui import Ui


def main():
    gameserver = GameServer(SERVER_ADDRESS, PORT)
    gaming = Ui(gameserver)
    gaming.menu()


main()