from butter.mas.packets.packet_builder import PacketBuilder
from butter.mas.interfaces.types import RotationUnits
from requests import Response


class Client:
    """ Butter MAS client API """

    def __init__(self, ip, port=3000, protocol='http'):
        """Initialize client
        
        Args:
            ip (str): robot IP
            port (int, optional): robot port. Defaults to 3000.
            protocol (str, optional): communication protocol. Defaults to "http".
        """
        self._timeout = 40
        self.ip = ip
        self.port = port
        self.protocol = protocol

    @property
    def timeout(self):
        """Get command execution timeout

        Returns:
            integer: command execution timeout in milliseconds
        """
        return self._timeout 
       
    @timeout.setter 
    def timeout(self, timeout):
        """Set time for the command execution

        Args:
            timeout (integer): command execution timeout in milliseconds

        Raises:
            ValueError: if timeout is not in the range [20, 500]
        """
        if (timeout < 20 or timeout > 500): 
           raise ValueError("Timeout most be an integer number in the range [20, 500]")

        self._timeout = timeout 

    def getAvailableHandlers(self) -> Response:
        """Get available robot handlers
        
        Returns:
            Response: response containing all the available robot handlers
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('list').build()

        return packet.send(self._timeout)

    def getAvailableAnimations(self, reload=False) -> Response:
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

        return packet.send(self._timeout)

    def getAvailableSounds(self, reload=False) -> Response:
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

        return packet.send(self._timeout)

    def getAvailableMotorRegisters(self, motorName, readableOnly=False) -> Response:
        """Get all available motor registers (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            readableOnly (bool, optional): get readable registers only. Defaults to False.
        
        Returns:
            Response: response containing all the available motor registers
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('dxl') \
            .addArguments('get', motorName) \
            .addParameter('list') \
            .addKeyValuePair('readableOnly', readableOnly) \
            .build()

        return packet.send(self._timeout)

    def getMotorRegister(self, motorName, registerName) -> Response:
        """Get motor register value (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
        
        Returns:
            Response: response containing register value
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('dxl') \
            .addArguments('get', motorName, registerName) \
            .build()

        return packet.send(self._timeout)

    def getMotorRegisterRange(self, motorName, registerName) -> Response:
        """Get motor register value range (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
        
        Returns:
            Response: response containing register range value
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('dxl') \
            .addArguments('get', motorName, registerName) \
            .addParameter('range') \
            .build()

        return packet.send(self._timeout)

    def setMotorRegister(self, motorName, registerName, value) -> Response:
        """Set motor register value (for Dynamixel motors only)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            registerName (str): motor register name
            value (str): register value
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('dxl') \
            .addArguments('set', motorName, registerName, value) \
            .build()

        return packet.send(self._timeout)

    def moveMotorToPosition(self, motorName, position, velocity=None, acceleration=None, units=RotationUnits.RADIANS.value) -> Response:
        """move motor to a certain position (relative to the motor's zero position)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            position (float): motor final position (in units)
            velocity (float, optional): motor movement speed (in units / sec). Defaults to None.
            acceleration (float, optional): motor maximal acceleration (in units / sec * sec). Defaults to None.
            units (RotationUnits, optional): rotation units. Defaults to 'radians'.
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('move').addArguments(motorName, position) \
            .addKeyValuePair('velocity', velocity) \
            .addKeyValuePair('acceleration', acceleration) \
            .addKeyValuePair('units', units) \
            .build()

        return packet.send(self._timeout)

    def moveMotorInTime(self, motorName, position, duration, units=RotationUnits.RADIANS.value) -> Response:
        """move motor to a certain position (relative to the motor's zero position) in fixed duration
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            position (float): motor final position (in units)
            duration (int): motor movement duration (in milliseconds)
            units (RotationUnits, optional): rotation units. Defaults to 'radians'.
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('move') \
            .addArguments(motorName, position) \
            .addKeyValuePair('duration', str(duration)) \
            .addKeyValuePair('units', units) \
            .build()

        return packet.send(self._timeout)

    def moveMotorInDirection(self, motorName, direction, velocity=None, units=RotationUnits.RADIANS.value) -> Response:
        """move motor to a certain direction (relative to the motor's current position)
        
        Args:
            motorName (str): motor name (as configured on the configurator)
            direction (str): motor movement direction (left, right, stop)
            velocity (float, optional): motor movement speed (in units / sec). Defaults to None.
            units (RotationUnits, optional): rotation units. Defaults to 'radians'.
        
        Returns:
            Response: response containing execution result
        """
        direction_code = -1 if direction.lower() == 'left' else 1 if direction.lower() == 'right' else 0
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('move') \
            .addArguments(motorName, direction_code) \
            .addKeyValuePair('velocity', velocity) \
            .addKeyValuePair('units', units) \
            .addParameter('continuously') \
            .build()

        return packet.send(self._timeout)

    # def moveMotorInSteps(self, motorName, direction, steps, velocity=None, interpolator=None, units=RotationUnits.RADIANS.value) -> Response:
    #     """move motor a certain amount of steps (relative to the motor's current position)

    #     Args:
    #         motorName (str): motor name (as configured on the configurator)
    #         direction (str): motor movement direction (left, right, stop)
    #         steps (str): amount of steps to move
    #         velocity (float, optional): motor movement speed (in units / sec). Defaults to None.
    #         interpolator (str, optional): interpolation function. Defaults to None.
    #         units (RotationUnits, optional): rotation units. Defaults to 'radians'.

    #     Returns:
    #         Response: response containing execution result
    #     """
    #     direction_code = -1 if direction.lower() == 'left' else 1 if direction.lower() == 'right' else 0
    #     packet = PacketBuilder(self.ip, self.port, self.protocol) \
    #         .addCommand('move') \
    #         .addArguments(motorName, direction_code) \
    #         .addKeyValuePair('steps', steps) \
    #         .addKeyValuePair('velocity', velocity) \
    #         .addKeyValuePair('interpolator', interpolator) \
    #         .addKeyValuePair('units', units) \
    #         .build()

    #     return packet.send(self._timeout)

    def playAnimation(self, animationName, lenient=False, relative=False) -> Response:
        """Play animation on the robot
        
        Args:
            animationName (str): animation name
            lenient (bool, optional): wait for current playing animation (if present) to finish . Defaults to False.
            relative (bool, optional): play animation relative to the current robot position. Defaults to False.
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('animate') \
            .addArgument(animationName) \
            .addKeyValuePair("lenient", lenient) \
            .addKeyValuePair("relative", relative) \
            .build()

        return packet.send(self._timeout)

    def pauseAnimation(self) -> Response:
        """Pause currently playing animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('animate') \
            .addParameter('pause') \
            .build()

        return packet.send(self._timeout)

    def resumeAnimation(self) -> Response:
        """Resume currently paused animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('animate') \
            .addParameter('resume') \
            .build()

        return packet.send(self._timeout)

    def stopAnimation(self) -> Response:
        """Stop currently playing animation (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('animate') \
            .addParameter('stop') \
            .build()

        return packet.send(self._timeout)

    def clearAnimation(self) -> Response:
        """Clear animation queue (if available)
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('animate') \
            .addParameter('clear') \
            .build()

        return packet.send(self._timeout)

    def playAudio(self, fileName) -> Response:
        """Play audio on the robot
        
        Args:
            fileName (str): audio asset name
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('audio') \
            .addArgument(fileName) \
            .build()

        return packet.send(self._timeout)

    def pauseAudio(self) -> Response:
        """Pause current audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('audio') \
            .addParameter('pause') \
            .build()

        return packet.send(self._timeout)

    def resumeAudio(self) -> Response:
        """Resume currently paused audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('audio') \
            .addParameter('resume') \
            .build()

        return packet.send(self._timeout)

    def stopAudio(self) -> Response:
        """Stop current audio playback (if available) on the robot
        
        Returns:
            Response: response containing execution result
        """
        packet = PacketBuilder(self.ip, self.port, self.protocol) \
            .addCommand('audio') \
            .addParameter('stop') \
            .build()

        return packet.send(self._timeout)
