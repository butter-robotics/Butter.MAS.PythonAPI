import unittest
from butter.mas.packets.packet_factory import PacketFactory


class TestHttpPacketMethods(unittest.TestCase):

    def testSend(self):
        packetFactory = PacketFactory()
        packet = packetFactory.getPacket('localhost', 3000, 'cmd/json/help')
        self.assertIsNotNone(packet.send())


if __name__ == '__main__':
    unittest.main()
