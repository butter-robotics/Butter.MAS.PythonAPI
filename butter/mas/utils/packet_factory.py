from .packet_http import HttpPacket
from .packet_udp import UdpPacket

class PacketFactory:
    ''' Packet factory for diffrent types of protocols '''

    def getPacket(self, ip, port, query, protocol="http"):
        """Creates new packet
        
        Arguments:
            ip {str} -- robot IP
            port {int} -- robot port
            query {str} -- packet payload
        
        Keyword Arguments:
            protocol {str} -- communication protocol (default: {"http"})
        
        Returns:
            Packet -- data packet
        """
        if (protocol == "http"):
            return HttpPacket(ip, port, query)
        elif (protocol == "udp"):
            return UdpPacket(ip, port, query)
        else:
            return None

    def getPacketClass(self, protocol="http"):
        """Get packet class
        
        Keyword Arguments:
            protocol {str} -- communication protocol (default: {"http"})
        
        Returns:
            Packet -- data packet
        """
        if (protocol == "http"):
            return HttpPacket
        elif (protocol == "udp"):
            return UdpPacket
        else:
            return None
