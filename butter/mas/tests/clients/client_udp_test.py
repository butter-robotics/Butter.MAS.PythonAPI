from butter.mas.api import UdpClient
from butter.mas.tests.clients.client_test import TestClientApiMethods


class TestUdpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = UdpClient('localhost')
