from butter.mas.api import HttpClient
from butter.mas.tests.clients.client_test import TestClientApiMethods


class TestHttpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = HttpClient('localhost')
