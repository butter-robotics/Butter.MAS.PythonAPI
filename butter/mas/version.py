from .environment import app_name, __version__
from packaging.version import Version
import sys
import requests
from requests.exceptions import HTTPError


class VersionValidations:
    """ Version and compatibility validations """

    @staticmethod
    def _getLatestAppVersion():
        version = None
        response = requests.get('https://pypi.org/pypi/{}/json'.format(app_name))

        if (response):
            app_info = response.json()
            if app_info and app_info['info'] and app_info['info']['version']:
                version = app_info['info']['version']

        return version

    @staticmethod
    def _getFirmwareVersions(ip, port=3000):
        versions = None
        response = None

        try:
            response = requests.get('http://{}:{}/api/information/versions'.format(ip, port))

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            pass
            # print('HTTP error occurred while trying to fetch firmware version: {}'.format(http_err), file=sys.stderr)
        except Exception as error:
            pass
            # print('Some error occurred while trying to fetch firmware version: {}'.format(error), file=sys.stderr)
        else:
            versions = response.json()

        return versions

    @staticmethod
    def checkForUpdates():
        """checks if this package is up to date
        
        Returns:
            boolean: true, if this package is up to date, otherwise, false
        """
        has_update = False
        latest_version = VersionValidations._getLatestAppVersion()

        if latest_version is None:
            print('Update check failed!', file=sys.stderr)
            print('Please check for updates manually at https://pypi.org/project/{}/'.format(app_name), file=sys.stderr)
        elif Version(__version__) < Version(latest_version):
            print('Update available! your version: {}, latest: {}'.format(__version__, latest_version))
            print('Execute `pip install -U {}` to update'.format(app_name))
            has_update = True
        else:
            print('Up to Date!')

        return has_update

    @staticmethod
    def checkCompatibility(ip):
        """checks that this package is compatible with the robot that listening on the given ip
        
        Args:
            ip (str): robot's ip address
        
        Returns:
            boolean: true, if this package and the robot firmware are compatible, otherwise, false
        """

        is_compatible = False
        firmware_version = VersionValidations._getFirmwareVersions(ip)

        if firmware_version is None or firmware_version.get('software', {}).get('mas'):
            print('Compatibility check failed!', file=sys.stderr)
        else:
            if __version__.split('.')[0] != firmware_version.get('software', {}).get('mas').split('.')[0]:
                print('This software is not compatible with {}'.format(ip))
                print('Please update your robot firmware')
            else:
                print('This software is compatible with {}'.format(ip))
                is_compatible = False

        return is_compatible
