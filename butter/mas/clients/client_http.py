from .client import Client


class HttpClient(Client):
    """ Butter MAS HTTP client API """

    def __init__(self, ip, port=3000):
        """Initialize Butter MAS HTTP client
                
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 3000.
        """
        super().__init__(ip, port, 'http')


if __name__ == "__main__":
    client = HttpClient('localhost')

    print(client.getAvailableHandlers().json())
