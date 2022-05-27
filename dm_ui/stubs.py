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
    GameServer stub (lado do cliente).
    """

    def __init__(self, host: str, port: int) -> None:
        """
        :param host:
        :param port:
        """
        super().__init__()
        self._host = host
        self._port = port

    def create_grid(self, a: int, b: int, c: int) -> int:
        """
        envia a largura e altura do tabueliro e também a percentagem de bombas para o servidor
        :return: numero de casas
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
        envia ao servidor as coordenadas da casa selecionada e recebe o numero escondido dentro da casa
        :return: valor da casa
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(OPN_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)
        return self.receive_int(INT_SIZE)

    def scoring_out(self) -> int:
        """
        recebe o score do cliente
        :return: score
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(SCR_OP)
        return self.receive_int(INT_SIZE)

    def send_name(self, a: str) -> None:
        """
        envia o nome do cliente
        :param a:
        :return:
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(NAM_OP)
        self.send_str(a)


    def flagging(self, a: int,  b: int) -> int:
        """
        envia a casa que o cliente quer colocar flag
        :param a:
        :param b:
        :return:
        """
        if self.current_connection is None:
            self.connect()
        self.send_str(FLG_OP)
        self.send_int(a, INT_SIZE)
        self.send_int(b, INT_SIZE)

    def checking_in(self, a: int,  b: int) -> int:
        """
        envia as coordenadas da casa selecionada pelo cliente
        recebe o tamanho da lista e depois os todos os valores inteiros da lista
        :param a:
        :param b:
        :return: lista de coordenadas
        """
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
        """
        Conecta-se ao servidor
        """
        self.current_connection = socket.socket()
        self.current_connection.connect((self._host, self._port))

    def stop_server(self):
        """
        Para a conecção ao servidor
        """
        self.send_str(STOP_SERVER_OP)
        self.current_connection.close()
