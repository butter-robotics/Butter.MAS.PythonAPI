import requests
from .general_utils import print_error

class Packet:
    ''' represents a data packet '''

    def __init__(self, ip, port, query):
        self.ip = ip
        self.port = port
        self.query = query

    def send(self, timeout=5):
        response = "'exception': 'Request timeout have been reached'" # todo fix

        try:
            response = requests.get('http://%s:%s/%s' % (self.ip, self.port, self.query), timeout=timeout)
        except requests.exceptions.Timeout as e:
            print_error('Warning: request timeout have been reached')

        return response