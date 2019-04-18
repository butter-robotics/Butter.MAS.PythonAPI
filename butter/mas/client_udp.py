from .client import Client

class UdpClient(Client):
    ''' Butter MAS UDP client API '''

    def __init__(self, ip, port=5000, protocol='udp'):
        """Initialize Butter MAS UDP client
        
        Arguments:
            ip {str} -- robot IP
        
        Keyword Arguments:
            port {int} -- robot port (default: {5555})
            protocol {str} -- communication protocol (default: {'udp'})
        """
        super().__init__(ip, port, protocol)

if __name__ == "__main__":
    client = UdpClient('localhost')

    print(client.getAvailableHandlers())