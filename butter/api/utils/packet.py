import requests
from .general_utils import print_error

class Packet:
    ''' represents a data packet '''

    def __init__(self, ip, port, query):
        self.ip = ip
        self.port = port
        self.query = query

    def send(self, timeout=5):
        response = None

        try:
            response = requests.get('http://%s:%s/%s' % (self.ip, self.port, self.query), timeout=timeout)
        except requests.exceptions.HTTPError as http_error:
            print_error('Warning: we have encountered in a http error.\n%s\n' % http_error)
            response = self._generateEmptyResponse('http')
        except requests.exceptions.Timeout as timeout_error:
            print_error('Warning: request timeout have been reached.\n%s\n' % timeout_error)
            response = self._generateEmptyResponse('timeout')
        except requests.exceptions.ConnectionError as connection_error:
            print_error('Warning: we have encountered in a connection error.\n%s\n' % connection_error)
            response = self._generateEmptyResponse('connection')
        except requests.exceptions.RequestException as error:
            print_error('Warning: request failed.\n%s\n' % error)
            response = self._generateEmptyResponse()

        return response

    @staticmethod
    def _generateEmptyResponse(errorType=b'unknown'):
        response = requests.Response()

        response._content = b'{ "exception": "Request resolved with an %s error" }' % errorType.encode("ascii")
        response.code = "expired"
        response.error_type = "expired"
        response.status_code = 400

        return response

    def __eq__(self, other):
        return isinstance(other, Packet) and self.ip == other.ip and self.port == other.port and self.query == other.query