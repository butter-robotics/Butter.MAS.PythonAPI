# Internal API

## Packet Factory


#### class butter.mas.utils.packet_factory.PacketFactory()
Packet factory for diffrent types of protocols


#### getPacket(ip, port, query, protocol='http')
Creates new packet


* **Parameters**

    * **ip** (*str*) – robot IP

    * **port** (*int*) – robot port

    * **query** (*str*) – packet payload

    * **protocol** (*str**, **optional*) – communication protocol. defaults to “http”.



* **Returns**

    data packet



* **Return type**

    Packet



#### getPacketClass(protocol='http')
Get packet class


* **Parameters**

    **protocol** (*str**, **optional*) – communication protocol. defaults to “http”.



* **Returns**

    data packet



* **Return type**

    Packet


## Packet Builder


#### class butter.mas.utils.packet_builder.PacketBuilder(ip, port, protocol='http')
Builds a command packet using the builder design pattern


#### addArgument(argument)
Add argument


* **Parameters**

    **argument** (*str*) – argument



* **Returns**

    self



* **Return type**

    PacketBuilder



#### addArguments(\*arguments)
Add arguments


* **Returns**

    self



* **Return type**

    PacketBuilder



#### addCommand(command)
Add command


* **Parameters**

    **command** (*str*) – command



* **Returns**

    self



* **Return type**

    PacketBuilder



#### addKeyValuePair(key, value)
Add key value pair


* **Parameters**

    * **key** (*str*) – attribute key

    * **value** (*str*) – attribute value



* **Returns**

    self



* **Return type**

    PacketBuilder



#### addParameter(parameter)
Add parameter


* **Parameters**

    **parameter** (*str*) – parameter



* **Returns**

    self



* **Return type**

    PacketBuilder



#### addParameters(\*parameters)
Add parameters


* **Returns**

    self



* **Return type**

    PacketBuilder



#### build()
Builds the packet


* **Returns**

    data packet



* **Return type**

    Packet


## HTTP Packet

HttpPacket extends Packet


#### class butter.mas.utils.packet_http.HttpPacket(ip, port, query)
Represents a http data packet


#### send(timeout=5)
Send packet


* **Parameters**

    **timeout** (*int**, **optional*) – packet timeout. defaults to 5.



* **Returns**

    response containing the response



* **Return type**

    Response


## TCP Packet

TcpPacket extends Packet


#### class butter.mas.utils.packet_tcp.TcpPacket(ip, port, query)
Represents a tcp data packet


#### send(timeout=5)
Send packet


* **Parameters**

    **timeout** (*int**, **optional*) – packet timeout. defaults to 5.



* **Returns**

    response containing the response



* **Return type**

    Response


## UDP Packet

HttpPacket extends Packet


#### class butter.mas.utils.packet_udp.UdpPacket(ip, port, query)
Represents a udp data packet


#### send(timeout=5)
Send packet


* **Parameters**

    **timeout** (*int**, **optional*) – packet timeout. defaults to 5.



* **Returns**

    response containing the response



* **Return type**

    Response


## Packet


#### class butter.mas.utils.packet.Packet(ip, port, query)
Represents an abstract data packet


#### abstract send(timeout=None)
Send packet abstract methud


* **Parameters**

    **timeout** (*int**, **optional*) – packet timeout. defaults to None.
