import unittest
from butter.mas.utils.packet_factory import PacketFactory

class TestHttpPacketMethods(unittest.TestCase):

    def testSend(self):
        packetFactory = PacketFactory()
        packet = packetFactory.getPacket('localhost', 5555, 'cmd/json/help')
        self.assertIsNotNone(packet.send())

if __name__ == '__main__':
    unittest.main()