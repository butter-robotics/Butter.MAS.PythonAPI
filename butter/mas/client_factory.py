import HttpClient
import UdpClient

class ClientFactory:
    ''' Client factory for diffrent types of protocols '''

    def getClient(self, ip, port=None, protocol="http"):
        """Creates new client
        
        Arguments:
            ip {str} -- robot IP
        
        Keyword Arguments:
            port {int} -- robot port (default: {None})
            protocol {str} -- communication protocol (default: {"http"})
        
        Returns:
            Client -- requested client
        """
        if (protocol == "http"):
            return HttpClient(ip) if port is None else HttpClient(ip, port)
        elif (protocol == "udp"):
            return UdpClient(ip) if port is None else UdpClient(ip, port)
        else:
            return None

    def getClientClass(self, protocol="http"):
        """Get client class
        
        Keyword Arguments:
            protocol {str} -- communication protocol (default: {"http"})
        
        Returns:
            Client -- client class
        """
        if (protocol == "http"):
            return HttpClient
        elif (protocol == "udp"):
            return UdpClient
        else:
            return None
