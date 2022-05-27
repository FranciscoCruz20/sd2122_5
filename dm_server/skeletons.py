import logging
import socket
from game import Minesweeper as minesweeper
from sockets_mod import Socket
import pickle
import csv

COMMAND_SIZE = 9
INT_SIZE = 8
CRT_OP = "crt      "
OPN_OP = "opn      "
FLG_OP = "flg      "
NAM_OP = "nam      "
SCR_OP = "scr      "
CHK_OP = "chk      "
BYE_OP = "bye      "
STOP_SERVER_OP = "terminate"
PORT = 35000
MSG_STR = 40

LOG_FILENAME = "math-server.log"
LOG_LEVEL = logging.DEBUG

class GameServer(Socket):
    """
    GameServer stub (lado do servidor).
    """
    def __init__(self, port: int, game: minesweeper) -> None:
        """
        :param port
        :param game
        """
        super().__init__()
        self._port = port
        self._server = game
        logging.basicConfig(filename=LOG_FILENAME,
                            level=LOG_LEVEL,
                            format='%(asctime)s (%(levelname)s): %(message)s')

    def position_info(self) -> None:
        """
        recebe a informação da posição da casa selecionada
        envia pó cliente o valor da casa
        :return:
        """
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        result = self._server.get_coord_value(a,b)
        self.send_int(result, INT_SIZE)

    def generate_grid(self) -> None:
        """
        recebe o largura, altura e percentagem de bombas escolhido pelo cliente
        envia o número tiles
        :return:
        """
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        c = self.receive_int(INT_SIZE)
        result = self._server.create_grid(a, b, c)
        self.send_int(result, INT_SIZE)

    def flag_it_up(self) -> None:
        """
        recebe as coordenadas da casa selecionada
        chama get_flagged
        :return:
        """
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        self._server.get_flagged(a, b)

    def scoring_in(self) -> None:
       """
       chama get_score
       envia o score
       :return:
       """
       result =  self._server.get_score()
       self.send_int(result, INT_SIZE)

    def checking_out(self):
        """
        recebe as coordenadas da casa selecionada, verifica as casa em redor
        dá uma lista com as coordenadas
        vê o tamanho da lista e envia o valor da mesma
        envia os valores da lista até acabarem
        :return:
        """
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        self._server.check_around2(a, b)
        result = self._server.get_list_to_send()
        self.send_int(len(result), INT_SIZE)
        print("here")
        for i in result:
            self.send_int(i, INT_SIZE)
        print(result)


    def name_on_the_list(self) -> None:
        """
        recebe o nome do cliente
        guarda o nome num ficheiro csv
        :return:
        """
        a = self.receive_str(COMMAND_SIZE)
        self._server.file_read_write(a)


    def run(self) -> None:
        """
        Dá run no server até o cliente terminar a conecção
        """
        current_socket = socket.socket()
        current_socket.bind(('', self._port))
        current_socket.listen(1)
        logging.info("Waiting for clients to connect on port " + str(self._port))
        keep_running = True
        while keep_running:
            self.current_connection, address = current_socket.accept()
            logging.debug("Client " + str(address) + " just connected")
            with self.current_connection:
                last_request = False
                while not last_request:
                    keep_running, last_request = self.dispatch_request()
                logging.debug("Client " + str(address) + " disconnected")
        current_socket.close()
        logging.info("Server stopped")

    def dispatch_request(self) -> (bool, bool):
        """
        recebe o comando do cliente
        executa a funçaõ relativa ao comando do cliente
        :return:
        """
        request_type = self.receive_str(COMMAND_SIZE)
        keep_running = True
        last_request = False
        if request_type == CRT_OP:
            self.generate_grid()
            self._server.print_matrix()
        elif request_type == OPN_OP:
            self.position_info()
        elif request_type == FLG_OP:
            self.flag_it_up()
        elif request_type == NAM_OP:
            self.name_on_the_list()
        elif request_type == SCR_OP:
            self.scoring_in()
        elif request_type == CHK_OP:
            self.checking_out()
        elif request_type == BYE_OP:
            last_request = True
        elif request_type == STOP_SERVER_OP:
            last_request = True
            keep_running = False
        return keep_running, last_request

