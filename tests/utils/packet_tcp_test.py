import unittest
from butter.mas.utils.packet_factory import PacketFactory

class TestTcpPacketMethods(unittest.TestCase):

    def testSend(self):
        packetFactory = PacketFactory()
        packet = packetFactory.getPacket('localhost', 5050, 'cmd/json/help', protocol='tcp')
        self.assertIsNotNone(packet.send())

if __name__ == '__main__':
    unittest.main()