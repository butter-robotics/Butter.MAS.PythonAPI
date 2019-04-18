from .client import Client

class HttpClient(Client):
    ''' Butter MAS HTTP client API '''

    def __init__(self, ip, port=5555, protocol='http'):
        """Initialize Butter MAS HTTP client
                
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 5555.
            protocol (str, optional): communication protocol. Defaults to "http".
        """
        super().__init__(ip, port, protocol)

if __name__ == "__main__":
    client = HttpClient('localhost')

    print(client.getAvailableHandlers().json())