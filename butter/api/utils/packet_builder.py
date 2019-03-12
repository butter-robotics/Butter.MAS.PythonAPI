from .packet import Packet

class PacketBuilder():
    ''' Builds a command packet using the builder design pattern '''

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.cmd = None
        self.args = list()
        self.params = list()
        self.keys = dict()

    def addCommand(self, command):
        self.cmd = command

        return self

    def addArgument(self, argument):
        self.args.append(argument)

        return self
    
    def addArguments(self, *arguments):
        if arguments:
            for argument in arguments:
                self.args.append(argument)

        return self

    def addParameter(self, parameter):
        self.params.append(self._formatParameter(parameter))

        return self

    def addParameters(self, *parameters):
        if parameters:
            for parameter in parameters:
                self.params.append(self._formatParameter(parameter))

        return self

    def addKeyValuePair(self, key, value):
        self.keys[key] = value

        return self

    def _formatParameter(self, param):
        if not param.startswith('--'):
            if  param.startswith('-'):
                param = '-' + param
            else:
                param = '--' + param

        return param

    def build(self):
        if self.cmd == None: 
            return None

        query = "%s?" % self.cmd

        if self.args: 
            query = "%s%s&" % (query, '&'.join(self.args))

        if self.params: 
            params = list(map(self._formatParameter, self.params))
            query = "%s%s&" % (query, '&'.join(params))

        if self.keys:
            keys = list(map(lambda x: "x=%s" % self.keys[x], self.keys))
            query = "%s%s" % (query, '&'.join(keys))

        uri = '/'.join(['cmd', 'json'])
        uri = "%s/%s" % (uri, query.strip('&'))

        return Packet(self.ip, self.port, uri)