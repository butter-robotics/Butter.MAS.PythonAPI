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
        """Get all available motor registers (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            readableOnly (bool, optional): get readable registers only. Defaults to False.
        
        Returns:
            Response: response containing all the available motor registers
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('dxl').addArguments('get', motorName) \
                    .addParameter('list').addKeyValuePair('readableOnly', readableOnly).build()

        return packet.send()

    def getMotorRegister(self, motorName, registerName):
        """Get motor register value (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
        
        Returns:
            Response: response containing register value
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('dxl') \
                    .addArguments('get', motorName, registerName).build()

        return packet.send()

    def getMotorRegisterRange(self, motorName, registerName):
        """Get motor register value range (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
        
        Returns:
            Response: response containing register range value
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('dxl') \
                    .addArguments('get', motorName, registerName).addParameter('range').build()

        return packet.send()

    def setMotorRegister(self, motorName, registerName, value):
        """Get motor register value (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
            value (str): register value
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('dxl') \
                    .addArguments('set', motorName, registerName, value).build()        

        return packet.send()

    def moveMotorToPosition(self, motorName, position, velocity=None, acceleration=None):
        """move motor to a certian position (relative to the motor's zero position)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            position (float): motor final position (in radians)
            velocity (float, optional): motor movement speed (in radians / sec). Defaults to None.
            acceleration (float, optional): motor maximal acceleration (in radians / sec * sec). Defaults to None.
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('move').addArguments(motorName, position) \
                    .addKeyValuePair('velocity', velocity).addKeyValuePair('acceleration', acceleration).build()        

        return packet.send()

    def moveMotorInTime(self, motorName, position, duration):
        """move motor to a certian position (relative to the motor's zero position) in fixed duration
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            position (float): motor final position (in radians)
            duration (int): motor movement duration (in milliseconds)
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('move').addArguments(motorName, position) \
                    .addKeyValuePair('duration', duration).build()        

        return packet.send()

    def moveMotorInDirection(self, motorName, direction, velocity=None):
        """move motor to a certian direction (relative to the motor's current position)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            direction (str): motor movement direction (left, right, stop)
            velocity (float, optional): motor movement speed (in radians / sec). Defaults to None.
        
        Returns:
            Response: response containing execution result
        """
        direction_code = -1 if direction.lower() == 'left' else 1 if direction.lower() == 'right' else 0
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('move').addArguments(motorName, direction_code) \
                    .addKeyValuePair('velocity', velocity).addParameter('continuously').build()        

        return packet.send()

    # def moveMotorInSteps(self, motorName, direction, steps, velocity=None, interpolator=None):
    #     """move motor a certian amount of steps (relative to the motor's current position)
        
    #     Args:
    #         motorName (str): motor name (as configured on the configurator)
    #         direction (str): motor movement direction (left, right, stop)
    #         steps (str): amount of steps to move
    #         velocity (float, optional): motor movement speed (in radians / sec). Defaults to None.
    #         interpolator (str, optional): interpolation function. Defaults to None.
        
    #     Returns:
    #         Response: response containing execution result
    #     """
    #     direction_code = -1 if direction.lower() == 'left' else 1 if direction.lower() == 'right' else 0
    #     packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('move').addArguments(motorName, direction_code) \
    #                 .addKeyValuePair('steps', steps).addKeyValuePair('velocity', velocity) \
    #                 .addKeyValuePair('interpolator', interpolator).build()        

    #     return packet.send()

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
