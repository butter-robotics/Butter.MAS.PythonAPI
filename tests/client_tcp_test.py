import unittest

from butter.mas.api import TcpClient

class TestTcpClientApiMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.client = TcpClient('localhost')

    def testGetAvailableHandlers(self):
        self.assertIsNotNone(self.client.getAvailableHandlers())

    def testGetAvailableAnimations(self):
        self.assertIsNotNone(self.client.getAvailableAnimations())

    def testGetAvailableSounds(self):
        self.assertIsNotNone(self.client.getAvailableSounds())

    def testGetAvailableMotorRegisters(self):
        self.assertIsNotNone(self.client.getAvailableMotorRegisters('base'))

    def testGetMotorRegister(self):
        self.assertIsNotNone(self.client.getMotorRegister('base', 'goal_position'))

    def testSetMotorRegister(self):
        self.assertIsNotNone(self.client.setMotorRegister('base', 'goal_position', '2048'))

    def testPlayAnimation(self):
        self.assertIsNotNone(self.client.playAnimation('welcome'))

    def testPauseAnimation(self):
        self.assertIsNotNone(self.client.pauseAnimation())

    def testResumeAnimation(self):
        self.assertIsNotNone(self.client.resumeAnimation())

    def testStopAnimation(self):
        self.assertIsNotNone(self.client.stopAnimation())

    def testPlayAudio(self):
        self.assertIsNotNone(self.client.playAudio('hello'))

    def testPauseAudio(self):
        self.assertIsNotNone(self.client.pauseAudio())

    def testResumeAudio(self):
        self.assertIsNotNone(self.client.resumeAudio())

    def testStopAudio(self):
        self.assertIsNotNone(self.client.stopAudio())
