import logging
import socket
from game import Minesweeper as minesweeper
from sockets_mod import Socket
import csv

COMMAND_SIZE = 9
INT_SIZE = 8
CRT_OP = "crt      "
OPN_OP = "opn      "
FLG_OP = "flg      "
NAM_OP = "nam      "
BYE_OP = "bye      "
STOP_SERVER_OP = "terminate"
PORT = 35000
MSG_STR = 40

LOG_FILENAME = "math-server.log"
LOG_LEVEL = logging.DEBUG

class GameServer(Socket):
    def __init__(self, port: int, game: minesweeper) -> None:
        """
        Creates a client given the server server to use
        :param port: The math server port of the host the client will use
        """
        super().__init__()
        self._port = port
        self._server = game
        logging.basicConfig(filename=LOG_FILENAME,
                            level=LOG_LEVEL,
                            format='%(asctime)s (%(levelname)s): %(message)s')

    def position_info(self) -> None:
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        result = self._server.get_coord_value(a,b)
        self.send_int(result, INT_SIZE)

    def generate_grid(self) -> None:
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        c = self.receive_int(INT_SIZE)
        self._server.create_grid(a, b, c)

    def flag_it_up(self) -> None:
        a = self.receive_int(INT_SIZE)
        b = self.receive_int(INT_SIZE)
        self._server.get_flagged(a, b)

    def name_on_the_list(self) -> None:
        a = self.receive_str(COMMAND_SIZE)
        self._server.file_read_write(a)


    def run(self) -> None:
        """
        Runs the server server until the client sends a "terminate" action
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
        elif request_type == BYE_OP:
            last_request = True
        elif request_type == STOP_SERVER_OP:
            last_request = True
            keep_running = False
        return keep_running, last_request

