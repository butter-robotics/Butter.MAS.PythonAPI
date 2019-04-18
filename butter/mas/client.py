from .utils.packet_builder import PacketBuilder

class Client():
    ''' Butter MAS client API '''

    def __init__(self, ip, port=5555, protocol='http'):
        """Initialize client
        
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 5555.
            protocol (str, optional): communication protocol. Defaults to "http".
        """
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def getAvailableHandlers(self):
        """Get available robot handlers
        
        Returns:
            Response: response containing all the available robot handlers
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('list').build()

        return packet.send()

    def getAvailableAnimations(self, reload=False):
        """Get available (loaded) robot animations        
        
        Args:
            reload (bool, optional): reload all animations. Defaults to False.
        
        Returns:
            Response: response containing all the available (loaded) robot animations
        """
        builder = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate')

        if reload:
            builder.addParameter('reload')

        packet = builder.addParameter('list').build()

        return packet.send()

    def getAvailableSounds(self, reload=False):
        """Get available (loaded) robot sound assets        
        
        Args:
            reload (bool, optional): reload all sound assets. Defaults to False.
        
        Returns:
            Response: response containing all the available (loaded) robot sound assets
        """
        builder = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio')

        if reload:
            builder.addParameter('reload')

        packet = builder.addParameter('list').build()

        return packet.send()

    def getAvailableMotorRegisters(self, motorName, readableOnly=False):
        """Get all available motor registers
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            readableOnly (bool, optional): get readable registers only. Defaults to False.
        
        Returns:
            Response: response containing all the available motor registers
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('get').addParameter('list') \
                    .addKeyValuePair('readableOnly', readableOnly).build()

        return packet.send()

    def getMotorRegister(self, motorName, registerName):
        """Get motor register value
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
        
        Returns:
            Response: response containing register value
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('get') \
                    .addArguments(motorName, registerName).build()

        return packet.send()

    def setMotorRegister(self, motorName, registerName, value):
        """Get motor register value
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
            value (str): register value
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('set') \
                    .addArguments(motorName, registerName, value).build()        

        return packet.send()

    def playAnimation(self, animationName):
        """Play animation on the robot
        
        Args:
            animationName (str): animation name
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addArgument(animationName).build()        

        return packet.send()

    def pauseAnimation(self):
        """Pause currently playing animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('pause').build()        

        return packet.send()

    def resumeAnimation(self):
        """Resume currently paused animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('resume').build()        

        return packet.send()

    def stopAnimation(self):
        """Stop currently playing animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('stop').build()        

        return packet.send() 

    def playAudio(self, fileName):
        """Play audio on the robot
        
        Args:
            fileName (str): audio asset name
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addArgument(fileName).build()        

        return packet.send()

    def pauseAudio(self):
        """Pause current audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('pause').build()        

        return packet.send()

    def resumeAudio(self):
        """Resume currently paused audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('resume').build()        

        return packet.send()

    def stopAudio(self):
        """Stop current audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('stop').build()        

        return packet.send()
