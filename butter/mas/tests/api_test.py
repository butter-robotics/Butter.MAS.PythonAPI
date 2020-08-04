import unittest

from butter.mas.tests.utils.version_validations_test import TestVersionValidationsMethods
from butter.mas.tests.clients.client_http_test import TestHttpClientApiMethods
from butter.mas.tests.clients.client_tcp_test import TestTcpClientApiMethods
from butter.mas.tests.clients.client_udp_test import TestUdpClientApiMethods
from butter.mas.tests.packets.packet_http_test import TestHttpPacketMethods
from butter.mas.tests.packets.packet_tcp_test import TestTcpPacketMethods
from butter.mas.tests.packets.packet_udp_test import TestUdpPacketMethods
from butter.mas.tests.packets.packet_builder_test import TestPacketBuilderMethods


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
