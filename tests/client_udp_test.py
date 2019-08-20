import unittest

from butter.mas.api import UdpClient
from tests.client_test import TestClientApiMethods

class TestUdpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = UdpClient('localhost')
