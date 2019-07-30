from .client_http import HttpClient
from .client_tcp import TcpClient
from .client_udp import UdpClient

class ClientFactory:
    ''' Client factory for diffrent types of protocols '''

    def getClient(self, ip, port=None, protocol="http"):
        """Creates new client
        
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to None.
            protocol (str, optional): communication protocol. Defaults to "http".
        
        Returns:
            Client: requested client
        """
        if (protocol == "http"):
            return HttpClient(ip) if port is None else HttpClient(ip, port)
        elif (protocol == "tcp"):
            return TcpClient(ip) if port is None else TcpClient(ip, port)
        elif (protocol == "udp"):
            return UdpClient(ip) if port is None else UdpClient(ip, port)
        else:
            return None

    def getClientClass(self, protocol="http"):
        """Get client class
        
        Args:
            protocol (str, optional): communication protocol. Defaults to "http".
        
        Returns:
            Client: client class
        """
        if (protocol == "http"):
            return HttpClient
        elif (protocol == "tcp"):
            return TcpClient
        elif (protocol == "udp"):
            return UdpClient
        else:
            return None
