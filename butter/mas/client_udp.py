from .client import Client

class UdpClient(Client):
    ''' Butter MAS UDP client API '''

    def __init__(self, ip, port=5000, protocol='http'):
        super().__init__(ip, port, protocol)

if __name__ == "__main__":
    client = UdpClient('localhost')

    print(client.getAvailableHandlers())