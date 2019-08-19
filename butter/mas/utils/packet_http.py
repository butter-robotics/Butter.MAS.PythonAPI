import requests
from .packet import Packet
from .general_utils import print_error

class HttpPacket(Packet):
    ''' Represents a http data packet '''

    def __init__(self, ip, port, query):
        """Initialize packet
        
        Args:
            ip (str): robot IP
            port (int): robot port
            query (str): packet payload
        """
        super().__init__(ip, port, query)

    def send(self, timeout=5):
        """Send packet
        
        Args:
            timeout (int, optional): packet timeout. defaults to 5.
        
        Returns:
            Response: response containing the response
        """
        response = None

        try:
            response = requests.get('http://%s:%s/%s' % (self.ip, self.port, self.query), timeout=timeout)
        except requests.exceptions.HTTPError as http_error:
            print_error('Warning: we have encountered in a http error.\n%s\n' % http_error)
            response = self._generateEmptyResponse('http')
        except requests.exceptions.Timeout as timeout_error:
            print_error('Warning: request timeout have been reached.\n%s\n' % timeout_error)
            response = self._generateEmptyResponse('timeout')
        except requests.exceptions.ConnectionError as connection_error:
            print_error('Warning: we have encountered in a connection error.\n%s\n' % connection_error)
            response = self._generateEmptyResponse('connection')
        except requests.exceptions.RequestException as error:
            print_error('Warning: request failed.\n%s\n' % error)
            response = self._generateEmptyResponse()

        return response

    def __eq__(self, other):
        return isinstance(other, HttpPacket) and self.ip == other.ip and self.port == other.port and self.query == other.query