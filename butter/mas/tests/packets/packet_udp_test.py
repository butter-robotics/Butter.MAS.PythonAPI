import unittest
from butter.mas.packets.packet_factory import PacketFactory


class TestUdpPacketMethods(unittest.TestCase):

    def testSend(self):
        packetFactory = PacketFactory()
        packet = packetFactory.getPacket('localhost', 5000, 'cmd/json/help', protocol='udp')
        self.assertIsNotNone(packet.send())


if __name__ == '__main__':
    unittest.main()
