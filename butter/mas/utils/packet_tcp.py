import socket
from .packet import Packet
from .general_utils import print_error

class TcpPacket(Packet):
    ''' Represents a tcp data packet '''

    def __init__(self, ip, port, query):
        """Initialize packet
        
        Args:
            ip (str): robot IP
            port (int): robot port
            query (str): packet payload
        """
        super().__init__(ip, port, query)
        self.bufferSize  = 2048

    def send(self, timeout=5):
        """Send packet
        
        Args:
            timeout (int, optional): packet timeout. defaults to 5.
        
        Returns:
            Response: response containing the response
        """
        response = None
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpSocket:
                tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                tcpSocket.settimeout(timeout)
                tcpSocket.connect((self.ip, self.port))
                tcpSocket.send(bytes(self.query + '\n', "utf-8"))
                tcpResponse = tcpSocket.recv(self.bufferSize)
                response = self._generateResponse(tcpResponse)
        except socket.herror as host_error:
            print_error('Warning: we have encountered in a host error.\n%s\n' % host_error)
            response = self._generateEmptyResponse('host')
        except socket.gaierror as address_error:
            print_error('Warning: we have encountered in a address error.\n%s\n' % address_error)
            response = self._generateEmptyResponse('address')
        except socket.timeout as timeout_error:
            print_error('Warning: request timeout have been reached.\n%s\n' % timeout_error)
            response = self._generateEmptyResponse('timeout')
        except (OSError, InterruptedError) as error:
            print_error('Warning: request failed.\n%s\n' % error)
            response = self._generateEmptyResponse()

        return response

    def __eq__(self, other):
        return isinstance(other, TcpPacket) and self.ip == other.ip and self.port == other.port and self.query == other.query