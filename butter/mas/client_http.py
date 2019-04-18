from .client import Client

class HttpClient(Client):
    ''' Butter MAS HTTP client API '''

    def __init__(self, ip, port=5555, protocol='http'):
        """Initialize Butter MAS HTTP client
        
        Arguments:
            ip {str} -- robot IP
        
        Keyword Arguments:
            port {int} -- robot port (default: {5555})
            protocol {str} -- communication protocol (default: {'http'})
        """
        super().__init__(ip, port, protocol)

if __name__ == "__main__":
    client = HttpClient('localhost')

    print(client.getAvailableHandlers().json())