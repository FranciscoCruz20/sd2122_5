class Socket:
    """
    classe Socket estabelece conectividade entre o lado do servidor e do cliente
    """
    def __init__(self):
        self._current_connection = None

    @property
    def current_connection(self):
        return self._current_connection

    @current_connection.setter
    def current_connection(self, value):
        self._current_connection = value

    def receive_int(self, n_bytes: int) -> int:
        """
        :param n_bytes: O número de bytes a serem lidos da conexão atual
        :return: O próximo inteiro lido da conexão atual
        """
        data = self.current_connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, value: int, n_bytes: int) -> None:
        """
        :param value: O valor inteiro a ser enviado para a conexão atual
        :param n_bytes: O número de bytes para enviar
        """
        self.current_connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self, n_bytes: int) -> str:
        """
        :param n_bytes: O número de bytes a serem lidos da conexão atual
        :return: A próxima string lida da conexão atual
        """
        data = self.current_connection.recv(n_bytes)
        return data.decode()

    def send_str(self, value: str) -> None:
        """
        :param value: O valor da string para enviar para a conexão atual
        """
        self.current_connection.send(value.encode())