import socket
from sockets_mod import Socket

COMMAND_SIZE = 9
INT_SIZE = 8
CRT_OP = "crt      "
OPN_OP = "opn      "
FLG_OP = "flg      "
BYE_OP = "bye      "
STOP_SERVER_OP = "terminate"
SERVER_ADDRESS = "localhost"
PORT = 35000

class GameServer(Socket):
    """
    A math stubs stub (client side).
    """

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self._host = host
        self._port = port

    def create_grid(self, a: int, b: int, c: int) -> int:
        """
        Read two integers from the current open connection, adds them up,
        and send the result back through the connection.
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(CRT_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)
        self.send_int(c, INT_SIZE)

    def open_position(self, a: int,  b: int) -> int:
        """
        Read one integer from the current open connection, computes its
        symmetric, and send the result back to the connection
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(OPN_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)
        return self.receive_int(INT_SIZE)

    def flagging(self, a: int,  b: int) -> int:
        """
        Read one integer from the current open connection, computes its
        symmetric, and send the result back to the connection
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(FLG_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)

    def connect(self):
        self.current_connection = socket.socket()
        self.current_connection.connect((self._host, self._port))

    def stop_server(self):
        self.send_str(STOP_SERVER_OP)
        self.current_connection.close()
