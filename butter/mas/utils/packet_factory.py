from .packet_http import HttpPacket
from .packet_udp import UdpPacket

class PacketFactory:
    ''' packet factory for diffrent types of protocols '''

    def getPacket(self, ip, port, query, protocol="http"):
        if (protocol == "http"):
            return HttpPacket(ip, port, query)
        elif (protocol == "udp"):
            return UdpPacket(ip, port, query)
        else:
            return None

    def getPacketClass(self, protocol="http"):
        if (protocol == "http"):
            return HttpPacket
        elif (protocol == "udp"):
            return UdpPacket
        else:
            return None
