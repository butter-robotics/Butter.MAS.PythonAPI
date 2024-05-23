from .client import Client


class TcpClient(Client):
    """ Butter MAS TCP client API """

    def __init__(self, ip, port=3003):
        """Initialize Butter MAS TCP client
                
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 3003.
        """
        super().__init__(ip, port, 'tcp')


if __name__ == "__main__":
    client = TcpClient('localhost')

    print(client.getAvailableHandlers())
