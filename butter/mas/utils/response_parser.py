from __future__ import annotations
from typing import List, Union
from requests import Response


class ResponseDataPacket:
    status: str                                     #: packet execution status
    data: Union[List[ResponseDataPacket], str]      #: packet execution data
    metadata: MetadataDataPacket                    #: packet execution metadata


class RequestDataPacket:
    query: str              #: request query
    parameters: List[str]   #: request query parameters


class MetadataDataPacket:
    handler: str            #: packet handler name
    asynchronous: bool      #: command executed asynchronously
    exception: str          #: packet exception
    timestamp: int          #: packet creation timestamp
    duration: int           #: packet round trip duration


class RobotResponse:
    """ 
    Robots response content
    **Note:** This Type should be updated together with MAS#ResponseBuilder 
    """

    request: RequestDataPacket      #: robot request data packet
    response: ResponseDataPacket    #: robot response data packet
    executed: bool                  #: robot data packet executed


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
        """ Composes API response data """
        return RobotResponseWrapper(response)

    @staticmethod
    def parse(response: Response) -> RobotResponse:
        """ Parses API response data """
        return response.json()
