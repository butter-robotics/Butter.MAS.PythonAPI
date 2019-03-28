import socket
from .packet import Packet
from .general_utils import print_error

class UdpPacket(Packet):
    ''' represents a udp data packet '''

    def __init__(self, ip, port, query):
        super().__init__(ip, port, query)
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bufferSize  = 1024

    def send(self, timeout=5):
        response = None

        try:
            self.udpSocket.sendto(bytes(self.query, "utf-8"), (self.ip, self.port))
            # response = self.udpSocket.recvfrom(self.bufferSize)
        except socket.herror as host_error:
            print_error('Warning: we have encountered in a host error.\n%s\n' % host_error)
            response = self._generateEmptyResponse('host')
        except socket.gaierror as address_error:
            print_error('Warning: we have encountered in a address error.\n%s\n' % address_error)
            response = self._generateEmptyResponse('address')
        except socket.timeout as timeout_error:
            print_error('Warning: request timeout have been reached.\n%s\n' % timeout_error)
            response = self._generateEmptyResponse('timeout')
        except (OSError | InterruptedError) as error:
            print_error('Warning: request failed.\n%s\n' % error)
            response = self._generateEmptyResponse()

        return response

    @staticmethod
    def _generateEmptyResponse(errorType=b'unknown'):
        error = '{ "exception": "Request resolved with an %s error" }' % errorType

        return (error, None)

    def __eq__(self, other):
        return isinstance(other, UdpPacket) and self.ip == other.ip and self.port == other.port and self.query == other.query