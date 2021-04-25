from __future__ import annotations
from typing import List, Union
from requests import Response


class ResponseDataPacket:
    status: str
    data: Union[List[ResponseDataPacket], str]
    metadata: str
    asynchronous: bool


class RobotResponse:
    """ *** This Type should be updated together with MAS#ResponseBuilder *** """

    command: str
    parameters: List[str]
    executed: bool
    response: ResponseDataPacket


class RobotResponseWrapper:
    def __init__(self, response: Response):
        self.response = response

    def raw(self):
        """ Raw robot response """
        return self.response

    def content(self):
        """ Robot response as bytes """
        return self.response.content

    def json(self):
        """ Robot response as json object """
        return ResponseParser.parse(self.response)

    def text(self):
        """ Robot response as text """
        return self.response.text


class ResponseParser:
    """ Parses API response data into a typed aware dictionary object """

    @staticmethod
    def _compose(response: Response) -> RobotResponseWrapper:
        return RobotResponseWrapper(response)

    @staticmethod
    def parse(response: Response) -> RobotResponse:
        return response.json()
