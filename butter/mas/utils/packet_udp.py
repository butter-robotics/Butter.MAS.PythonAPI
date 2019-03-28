import requests
from .packet import Packet
from .general_utils import print_error

class UdpPacket(Packet):
    ''' represents a udp data packet '''

    def __init__(self, ip, port, query):
        super().__init__(ip, port, query)

    def send(self, timeout=5):
        pass

    @staticmethod
    def _generateEmptyResponse(errorType=b'unknown'):
        pass

    def __eq__(self, other):
        return isinstance(other, UdpPacket) and self.ip == other.ip and self.port == other.port and self.query == other.query