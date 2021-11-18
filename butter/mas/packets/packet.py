from abc import ABC, abstractmethod
from requests import Response


class Packet(ABC):
    """ Represents an abstract data packet """

    def __init__(self, ip, port, query):
        """Initialize packet
        
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 3000.
            query (str): packet payload
        """
        self.ip = ip
        self.port = port
        self.query = query

    @abstractmethod
    def send(self, timeout=None) -> Response:
        """Send packet abstract methud
        
        Args:
            timeout (int, optional): packet timeout. defaults to None.
        """
        pass

    @staticmethod
    def _generateResponse(content) -> Response:
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
    def _generateEmptyResponse(errorType='unknown') -> Response:
        """Generates empty response packet
        
        Args:
            errorType (bytes, optional): error type. defaults to b'unknown'.
        
        Returns:
            Response: error response
        """
        response = Response()

        data = '''request: {
            query: null,
            parameters: null
        },
        response: {
            status: "Failed",
            data: null,
            metadata: { 
                handler: "unknown",
                exception: "Request resolved with an {0} error", 
                timestamp: 0, 
                duration: 0, 
                asynchronous: false 
            }
        },
        executed: false'''.format(errorType)

        response._content = data.encode()
        response.code = "expired"
        response.error_type = "expired"
        response.status_code = 400

        return response

    def __eq__(self, other) -> bool:
        return isinstance(other,
                          Packet) and self.ip == other.ip and self.port == other.port and self.query == other.query
