# Packet Factory


### class butter.mas.packets.packet_factory.PacketFactory()
Packet factory for different types of protocols


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
