import socket
import stubs as stubs
from sockets.sockets_mod import Socket


class MathServer(Socket):
    """
    A math stubs stub (client side).
    """

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self._host = host
        self._port = port

    def add(self, a: int, b: int) -> int:
        """
        Read two integers from the current open connection, adds them up,
        and send the result back through the connection.
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(stubs.ADD_OP)
        self.send_int(a, stubs.INT_SIZE)
        self.send_int(b, stubs.INT_SIZE)
        return self.receive_int(stubs.INT_SIZE)

    def sym(self, a: int) -> int:
        """
        Read one integer from the current open connection, computes its
        symmetric, and send the result back to the connection
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(stubs.SYM_OP)
        self.send_int(a, stubs.INT_SIZE)
        return self.receive_int(stubs.INT_SIZE)

    def connect(self):
        self.current_connection = socket.socket()
        self.current_connection.connect((self._host, self._port))

    def stop_server(self):
        self.send_str(stubs.STOP_SERVER_OP)
        self.current_connection.close()
