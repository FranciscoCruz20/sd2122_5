import server as server
import logging
import socket
from sockets_mod import Socket


class MathServer(Socket):
    def __init__(self, port: int, math_server: server.MathServer) -> None:
        """
        Creates a client given the server server to use
        :param port: The math server port of the host the client will use
        """
        super().__init__()
        self._port = port
        self._server = math_server
        logging.basicConfig(filename=server.LOG_FILENAME,
                            level=server.LOG_LEVEL,
                            format='%(asctime)s (%(levelname)s): %(message)s')

    def position_info(self) -> None:
        a = self.receive_int(server.INT_SIZE)
        b = self.receive_int(server.INT_SIZE)
        result = self._server.add(a, b)
        self.send_int(result, server.INT_SIZE)


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
        request_type = self.receive_str(server.COMMAND_SIZE)
        keep_running = True
        last_request = False
        if request_type == server.ADD_OP:
            self.add()
        elif request_type == server.SYM_OP:
            self.sym()
        elif request_type == server.BYE_OP:
            last_request = True
        elif request_type == server.STOP_SERVER_OP:
            last_request = True
            keep_running = False
        return keep_running, last_request
