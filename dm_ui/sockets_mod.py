class Socket:
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
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next integer read from the current connection
        """
        data = self.current_connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, value: int, n_bytes: int) -> None:
        """
        :param value: The integer value to be sent to the current connection
        :param n_bytes: The number of bytes to send
        """
        self.current_connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = self.current_connection.recv(n_bytes)
        return data.decode()

    def send_str(self, value: str) -> None:
        """
        :param value: The string value to send to the current connection
        """
        self.current_connection.send(value.encode())