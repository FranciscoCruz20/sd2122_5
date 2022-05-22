from game import Minesweeper
from skeletons import GameServer, PORT


def main():
    GameServer(PORT,Minesweeper()).run()


main()
