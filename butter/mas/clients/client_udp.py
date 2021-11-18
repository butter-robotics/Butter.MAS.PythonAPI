from .client import Client


class UdpClient(Client):
    """ Butter MAS UDP client API """

    def __init__(self, ip, port=3030, protocol='udp'):
        """Initialize Butter MAS UDP client
                
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 3030.
            protocol (str, optional): communication protocol. Defaults to "udp".
        """
        super().__init__(ip, port, protocol)


if __name__ == "__main__":
    client = UdpClient('localhost')

    print(client.getAvailableHandlers())
