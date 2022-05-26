import socket
from sockets_mod import Socket

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
        return self.receive_int(INT_SIZE)

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

    def scoring_out(self) -> int:
        """
        Read one integer from the current open connection, computes its
        symmetric, and send the result back to the connection
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(SCR_OP)
        return self.receive_int(INT_SIZE)

    def send_name(self, a: str) -> None:
        """
        Read one integer from the current open connection, computes its
        symmetric, and send the result back to the connection
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(NAM_OP)
        self.send_str(a)


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

    def checking_in(self, a: int,  b: int) -> int:
        list_to_receive = []
        if self.current_connection is None:
            self.connect()
        self.send_str(CHK_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)
        size = self.receive_int(INT_SIZE)
        for i in range(size):
            list_to_receive.append(self.receive_int(INT_SIZE))
        print(list_to_receive)
        return list_to_receive

    def connect(self):
        self.current_connection = socket.socket()
        self.current_connection.connect((self._host, self._port))

    def stop_server(self):
        self.send_str(STOP_SERVER_OP)
        self.current_connection.close()
