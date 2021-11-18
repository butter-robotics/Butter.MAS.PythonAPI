import unittest
from butter.mas.packets.packet_factory import PacketFactory


class TestTcpPacketMethods(unittest.TestCase):

    def testSend(self):
        packetFactory = PacketFactory()
        packet = packetFactory.getPacket('localhost', 3003, 'cmd/json/help', protocol='tcp')
        self.assertIsNotNone(packet.send())


if __name__ == '__main__':
    unittest.main()
