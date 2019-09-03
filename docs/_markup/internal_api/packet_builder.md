# Packet Builder


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
