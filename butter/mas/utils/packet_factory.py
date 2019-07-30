from .packet_http import HttpPacket
from .packet_tcp import TcpPacket
from .packet_udp import UdpPacket

class PacketFactory:
    ''' Packet factory for diffrent types of protocols '''

    def getPacket(self, ip, port, query, protocol="http"):
        """Creates new packet
        
        Arguments:
            ip (str): robot IP
            port (int): robot port
            query (str): packet payload
            protocol (str, optional): communication protocol. defaults to "http".
        
        Returns:
            Packet: data packet
        """
        if (protocol == "http"):
            return HttpPacket(ip, port, query)
        elif (protocol == "tcp"):
            return TcpPacket(ip, port, query)
        elif (protocol == "udp"):
            return UdpPacket(ip, port, query)
        else:
            return None

    def getPacketClass(self, protocol="http"):
        """Get packet class
        
        Args:
            protocol (str, optional): communication protocol. defaults to "http".
        
        Returns:
            Packet: data packet
        """
        if (protocol == "http"):
            return HttpPacket
        elif (protocol == "tcp"):
            return TcpPacket
        elif (protocol == "udp"):
            return UdpPacket
        else:
            return None
