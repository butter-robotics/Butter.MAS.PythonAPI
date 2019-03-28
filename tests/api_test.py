import unittest

from tests.client_http_test import TestHttpClientApiMethods
from tests.client_udp_test import TestUdpClientApiMethods
from tests.utils.packet_http_test import TestHttpPacketMethods
from tests.utils.packet_udp_test import TestUdpPacketMethods
from tests.utils.packet_builder_test import TestPacketBuilderMethods

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    testCases = (TestPacketBuilderMethods, 
                TestHttpPacketMethods, 
                TestUdpPacketMethods, 
                TestHttpClientApiMethods, 
                TestUdpClientApiMethods)

    for testClass in testCases:
        tests = loader.loadTestsFromTestCase(testClass)
        suite.addTests(tests)

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())