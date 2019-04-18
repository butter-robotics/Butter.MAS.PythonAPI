from abc import ABC, abstractmethod

class Packet(ABC):
    ''' Represents an abstract data packet '''

    def __init__(self, ip, port, query):
        """Initialize packet
        
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 5555.
            query (str): packet payload
        """
        self.ip = ip
        self.port = port
        self.query = query

    @abstractmethod
    def send(self, timeout=None):
        """Send packet abstract methud
        
        Args:
            timeout (int, optional): packet timeout. defaults to None.
        """
        pass

    def __eq__(self, other):
        return isinstance(other, Packet) and self.ip == other.ip and self.port == other.port and self.query == other.query
