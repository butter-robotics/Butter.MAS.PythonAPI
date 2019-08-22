from .packet_factory import PacketFactory

class PacketBuilder():
    ''' Builds a command packet using the builder design pattern '''

    def __init__(self, ip, port, protocol="http"):
        """Initialize builder
        
        Args:
            ip (str): robot IP
            port (int): robot port
            protocol (str, optional): communication protocol. defaults to "http".
        """
        self.ip = ip
        self.port = port

        packetFactory = PacketFactory()
        self.packet = packetFactory.getPacketClass(protocol)

        self.cmd = None
        self.args = list()
        self.params = list()
        self.keys = dict()

    def addCommand(self, command):
        """Add command
        
        Args:
            command (str): command
        
        Returns:
            PacketBuilder: self
        """
        self.cmd = str(command)

        return self

    def addArgument(self, argument):
        """Add argument
        
        Args:
            argument (str): argument
        
        Returns:
            PacketBuilder: self
        """
        self.args.append(str(argument))

        return self
    
    def addArguments(self, *arguments):
        """Add arguments
        
        Returns:
            PacketBuilder: self
        """
        if arguments:
            for argument in arguments:
                self.args.append(str(argument))

        return self

    def addParameter(self, parameter):
        """Add parameter
        
        Args:
            parameter (str): parameter
        
        Returns:
            PacketBuilder: self
        """
        self.params.append(self._formatParameter(str(parameter)))

        return self

    def addParameters(self, *parameters):
        """Add parameters
        
        Returns:
            PacketBuilder: self
        """
        if parameters:
            for parameter in parameters:
                self.params.append(self._formatParameter(str(parameter)))

        return self

    def addKeyValuePair(self, key, value):
        """Add key value pair
        
        Args:
            key (str): attribute key
            value (str): attribute value
        
        Returns:
            PacketBuilder: self
        """
        if value:
            self.keys[key] = str(value)

        return self

    def _formatParameter(self, parameter):
        """Formats parameter properly
        
        Args:
            parameter (str): parameter
        
        Returns:
            str: formated parameter
        """
        if not parameter.startswith('--'):
            if  parameter.startswith('-'):
                parameter = '-' + parameter
            else:
                parameter = '--' + parameter

        return parameter

    def build(self):
        """Builds the packet
        
        Returns:
            Packet: data packet
        """
        if self.cmd == None: 
            return None

        query = "%s?" % self.cmd

        if self.args: 
            query = "%s%s&" % (query, '&'.join(self.args))

        if self.params: 
            params = list(map(self._formatParameter, self.params))
            query = "%s%s&" % (query, '&'.join(params))

        if self.keys:
            keys = list(map(lambda key: "%s=%s" % (key, self.keys[key]), self.keys))
            query = "%s%s" % (query, '&'.join(keys))

        uri = '/'.join(['cmd', 'json'])
        uri = "%s/%s" % (uri, query.strip('&'))

        return self.packet(self.ip, self.port, uri)
