import unittest

from tests.version_validations_test import TestVersionValidationsMethods
from tests.client_http_test import TestHttpClientApiMethods
from tests.client_tcp_test import TestTcpClientApiMethods
from tests.client_udp_test import TestUdpClientApiMethods
from tests.utils.packet_http_test import TestHttpPacketMethods
from tests.utils.packet_tcp_test import TestTcpPacketMethods
from tests.utils.packet_udp_test import TestUdpPacketMethods
from tests.utils.packet_builder_test import TestPacketBuilderMethods

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    testCases = (TestVersionValidationsMethods,
                TestPacketBuilderMethods, 
                TestHttpPacketMethods, 
                TestTcpPacketMethods,
                TestUdpPacketMethods,
                TestHttpClientApiMethods,
                TestTcpClientApiMethods,
                TestUdpClientApiMethods)

    for testClass in testCases:
        tests = loader.loadTestsFromTestCase(testClass)
        suite.addTests(tests)

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # runner.run(suite()) # avoid running test twice (for some reason test run after import -?!-)