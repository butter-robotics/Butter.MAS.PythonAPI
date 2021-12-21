# Client Factory


### class butter.mas.clients.client_factory.ClientFactory()
Client factory for different types of protocols


#### getClient(ip, port=None, protocol='http')
Creates new client


* **Parameters**

    * **ip** (*str*) – robot IP

    * **port** (*int**, **optional*) – robot port. Defaults to None.

    * **protocol** (*str**, **optional*) – communication protocol. Defaults to “http”.



* **Returns**

    requested client



* **Return type**

    Client



#### getClientClass(protocol='http')
Get client class


* **Parameters**

    **protocol** (*str**, **optional*) – communication protocol. Defaults to “http”.



* **Returns**

    client class



* **Return type**

    Client
