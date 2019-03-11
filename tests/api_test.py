import unittest

from api.api import Client
from tests.utils.packet_test import TestPacketMethods
from tests.utils.packet_builder_test import TestPacketBuilderMethods

class TestClientApiMethods(unittest.TestCase):
    def testSetUp(self):
        self.client = Client('localhost')

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
        self.assertIsNotNone(self.client.setMotorRegister('base', 'goal_position'))

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

def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestPacketMethods('test packet class methods'))
    suite.addTest(TestPacketBuilderMethods('test packet builder class methods'))
    suite.addTest(TestClientApiMethods('test client api class methods'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())