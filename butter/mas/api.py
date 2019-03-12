from .utils.packet_builder import PacketBuilder

class Client():
    ''' Butter MAS HTTP client API '''

    def __init__(self, ip, port=5555):
        self.ip = ip
        self.port = port

    def getAvailableHandlers(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('list').build()

        return packet.send()

    def getAvailableAnimations(self, reload=False):
        packet = PacketBuilder(self.ip, self.port).addCommand('animate').addParameter('list').build()

        return packet.send()

    def getAvailableSounds(self, reload=False):
        packet = PacketBuilder(self.ip, self.port).addCommand('audio').addParameter('list').build()

        return packet.send()

    def getAvailableMotorRegisters(self, motorName, writeableOnly=False):
        packet = PacketBuilder(self.ip, self.port).addCommand('get').addParameter('list').build()

        return packet.send()

    def getMotorRegister(self, motorName, registerName):
        packet = PacketBuilder(self.ip, self.port).addCommand('get').addArguments(motorName, registerName).build()

        return packet.send()

    def setMotorRegister(self, motorName, registerName, value):
        packet = PacketBuilder(self.ip, self.port).addCommand('set').addArguments(motorName, registerName, value).build()        

        return packet.send()

    def playAnimation(self, animationName):
        packet = PacketBuilder(self.ip, self.port).addCommand('animate').addArgument(animationName).build()        

        return packet.send()

    def pauseAnimation(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('animate').addParameter('pause').build()        

        return packet.send()

    def resumeAnimation(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('animate').addParameter('resume').build()        

        return packet.send()

    def stopAnimation(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('animate').addParameter('stop').build()        

        return packet.send() 

    def playAudio(self, fileName):
        packet = PacketBuilder(self.ip, self.port).addCommand('audio').addArgument(fileName).build()        

        return packet.send()

    def pauseAudio(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('audio').addParameter('pause').build()        

        return packet.send()

    def resumeAudio(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('audio').addParameter('resume').build()        

        return packet.send()

    def stopAudio(self):
        packet = PacketBuilder(self.ip, self.port).addCommand('audio').addParameter('stop').build()        

        return packet.send()

if __name__ == "__main__":
    client = Client('localhost')

    print(client.getAvailableHandlers().json())