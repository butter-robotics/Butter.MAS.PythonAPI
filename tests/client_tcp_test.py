import unittest

from butter.mas.api import TcpClient
from tests.client_test import TestClientApiMethods

class TestTcpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = TcpClient('localhost')
