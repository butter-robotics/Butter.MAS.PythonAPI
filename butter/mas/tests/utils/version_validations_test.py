import unittest

from butter.mas.api import VersionValidations


class TestVersionValidationsMethods(unittest.TestCase):

    def testGetLatestAppVersion(self):
        self.assertIsNotNone(VersionValidations._getLatestAppVersion())

    def testCheckForUpdates(self):
        self.assertFalse(VersionValidations.checkForUpdates())

    def testGetFirmwareVersions(self):
        self.assertIsNotNone(VersionValidations._getFirmwareVersions('localhost'))

    def testCheckCompatibility(self):
        self.assertTrue(VersionValidations.checkCompatibility('localhost'))
