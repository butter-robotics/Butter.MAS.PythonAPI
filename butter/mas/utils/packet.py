from abc import ABC, abstractmethod

class Packet(ABC):
    ''' represents an abstract data packet '''

    def __init__(self, ip, port, query):
        self.ip = ip
        self.port = port
        self.query = query

    @abstractmethod
    def send(self, timeout=None):
        pass

    def __eq__(self, other):
        return isinstance(other, Packet) and self.ip == other.ip and self.port == other.port and self.query == other.query
