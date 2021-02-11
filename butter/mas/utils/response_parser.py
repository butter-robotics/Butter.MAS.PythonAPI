from requests import Response


class RobotResponse:
    """ *** This Type should be updated together with MAS#ResponseBuilder *** """

    executed: bool
    result: str


class ResponseParser:
    """ Parses API response data into a typed aware dictionary object """

    @staticmethod
    def parse(response: Response) -> RobotResponse:
        return response.json()
