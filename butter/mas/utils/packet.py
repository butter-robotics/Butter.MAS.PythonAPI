from abc import ABC, abstractmethod
from requests import Response

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

    @staticmethod
    def _generateResponse(content):
        """Generates response from packet
        
        Args:
            content (bytes): response content
        
        Returns:
            Response: structured response
        """
        response = Response()

        response._content = content
        response.status_code = 200

        return response

    @staticmethod
    def _generateEmptyResponse(errorType='unknown'):
        """Generates empty response packet
        
        Args:
            errorType (bytes, optional): error type. defaults to b'unknown'.
        
        Returns:
            Response: error response
        """
        response = Response()

        response._content = ('{ "exception": "Request resolved with an %s error" }' % errorType).encode()
        response.code = "expired"
        response.error_type = "expired"
        response.status_code = 400

        return response

    def __eq__(self, other):
        return isinstance(other, Packet) and self.ip == other.ip and self.port == other.port and self.query == other.query
