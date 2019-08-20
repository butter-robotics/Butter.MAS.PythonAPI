import unittest

from butter.mas.api import HttpClient
from tests.client_test import TestClientApiMethods

class TestHttpClientApiMethods(TestClientApiMethods):

    @classmethod
    def setUpClass(self):
        self.client = HttpClient('localhost')
