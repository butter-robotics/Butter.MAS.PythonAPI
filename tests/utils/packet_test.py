import unittest
from butter.mas.utils.packet import Packet

class TestPacketMethods(unittest.TestCase):

    def testSend(self):
        packet = Packet('localhost', 5555, 'cmd/json/help')
        self.assertIsNotNone(packet.send())

if __name__ == '__main__':
    unittest.main()