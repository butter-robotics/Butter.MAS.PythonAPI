from butter.mas.api import TcpClient
from butter.mas.tests.clients.client_test import TestClientApiMethods


class TestTcpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = TcpClient('localhost')
