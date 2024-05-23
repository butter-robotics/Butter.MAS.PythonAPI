# Response Parser

### *class* butter.mas.utils.response_parser.MetadataDataPacket

#### asynchronous *: bool*

command executed asynchronously

#### duration *: int*

packet round trip duration

#### exception *: str*

packet exception

#### handler *: str*

packet handler name

#### timestamp *: int*

packet creation timestamp

### *class* butter.mas.utils.response_parser.RequestDataPacket

#### parameters *: List[str]*

request query parameters

#### query *: str*

request query

### *class* butter.mas.utils.response_parser.ResponseDataPacket

#### data *: Union[List[[ResponseDataPacket](#butter.mas.utils.response_parser.ResponseDataPacket)], str]*

packet execution data

#### metadata *: [MetadataDataPacket](#butter.mas.utils.response_parser.MetadataDataPacket)*

packet execution metadata

#### status *: str*

packet execution status

### *class* butter.mas.utils.response_parser.ResponseParser

Parses API response data into a typed aware dictionary object

#### *static* parse(response: Response)

Parses API response data

### *class* butter.mas.utils.response_parser.RobotResponse

Robots response content
**Note:** This Type should be updated together with MAS#ResponseBuilder

#### executed *: bool*

robot data packet executed

#### request *: [RequestDataPacket](#butter.mas.utils.response_parser.RequestDataPacket)*

robot request data packet

#### response *: [ResponseDataPacket](#butter.mas.utils.response_parser.ResponseDataPacket)*

robot response data packet

### *class* butter.mas.utils.response_parser.RobotResponseWrapper(response: Response)

#### content()

Robot response as bytes

#### json()

Robot response as json object

#### raw()

Raw robot response

#### text()

Robot response as text
