from .utils.packet_builder import PacketBuilder

class Client():
    ''' Butter MAS client API '''

    def __init__(self, ip, port=5555, protocol='http'):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    def getAvailableHandlers(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('list').build()

        return packet.send()

    def getAvailableAnimations(self, reload=False):
        builder = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate')

        if reload:
            builder.addParameter('reload')

        packet = builder.addParameter('list').build()

        return packet.send()

    def getAvailableSounds(self, reload=False):
        builder = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio')

        if reload:
            builder.addParameter('reload')

        packet = builder.addParameter('list').build()

        return packet.send()

    def getAvailableMotorRegisters(self, motorName, readableOnly=False):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('get').addParameter('list') \
                    .addKeyValuePair('readableOnly', readableOnly).build()

        return packet.send()

    def getMotorRegister(self, motorName, registerName):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('get') \
                    .addArguments(motorName, registerName).build()

        return packet.send()

    def setMotorRegister(self, motorName, registerName, value):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('set') \
                    .addArguments(motorName, registerName, value).build()        

        return packet.send()

    def playAnimation(self, animationName):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addArgument(animationName).build()        

        return packet.send()

    def pauseAnimation(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('pause').build()        

        return packet.send()

    def resumeAnimation(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('resume').build()        

        return packet.send()

    def stopAnimation(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('animate').addParameter('stop').build()        

        return packet.send() 

    def playAudio(self, fileName):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addArgument(fileName).build()        

        return packet.send()

    def pauseAudio(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('pause').build()        

        return packet.send()

    def resumeAudio(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('resume').build()        

        return packet.send()

    def stopAudio(self):
        packet = PacketBuilder(self.ip, self.port, self.protocol).addCommand('audio').addParameter('stop').build()        

        return packet.send()
