# Response Parser


#### class butter.mas.utils.response_parser.MetadataDataPacket()

#### asynchronous( = None)
command executed asynchronously


#### duration( = None)
packet round trip duration


#### exception( = None)
packet exception


#### handler( = None)
packet handler name


#### timestamp( = None)
packet creation timestamp


#### class butter.mas.utils.response_parser.RequestDataPacket()

#### parameters( = None)
request query parameters


#### query( = None)
request query


#### class butter.mas.utils.response_parser.ResponseDataPacket()

#### data( = None)
packet execution data


#### metadata( = None)
packet execution metadata


#### status( = None)
packet execution status


#### class butter.mas.utils.response_parser.ResponseParser()
Parses API response data into a typed aware dictionary object


#### static parse(response: requests.models.Response)
Parses API response data


#### class butter.mas.utils.response_parser.RobotResponse()
Robots response content
**Note:** This Type should be updated together with MAS#ResponseBuilder


#### executed( = None)
robot data packet executed


#### request( = None)
robot request data packet


#### response( = None)
robot response data packet


#### class butter.mas.utils.response_parser.RobotResponseWrapper(response: requests.models.Response)

#### content()
Robot response as bytes


#### json()
Robot response as json object


#### raw()
Raw robot response


#### text()
Robot response as text
