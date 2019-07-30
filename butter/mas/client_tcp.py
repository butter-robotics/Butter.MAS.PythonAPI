from .client import Client

class TcpClient(Client):
    ''' Butter MAS TCP client API '''

    def __init__(self, ip, port=5050, protocol='tcp'):
        """Initialize Butter MAS TCP client
                
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 5000.
            protocol (str, optional): communication protocol. Defaults to "tcp".
        """
        super().__init__(ip, port, protocol)

if __name__ == "__main__":
    client = TcpClient('localhost')

    print(client.getAvailableHandlers())