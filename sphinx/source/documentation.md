# Documentation

## Importing Client Factory

Client Factory is a factory class responsible for creating new clients.
In order to use the factory, we will need to import it first:

```python
from butter.mas.api import ClientFactory
```

## Creating New Client

In order to use communicate with the robot, we will need to create a client.
There are to types of clients: HttpClient and UdpClient.
Both clients extends the Client class.

Creating new HTTP client:

```python
butterHttpClient = ClientFactory().getClient('192.168.0.100', protocol='http')  # use you robot ip here
```

Creating new TCP client:

```python
butterTcpClient = ClientFactory().getClient('192.168.0.100', protocol='tcp')  # use you robot ip here
```

Creating new UDP client:

```python
butterUdpClient = ClientFactory().getClient('192.168.0.100', protocol='udp')    # use you robot ip here
```

The IP address should be the same as the current IP address of the robot on your local network.

## Interaction With the robot

We can send a command through one of the available functions of the client.

I.e., we can play animation with the following command:

```python
result = butterHttpClient.playAnimation('welcome')
```

## Receiving Responses from the robot

Each command we send will return (no matter what protocol we use) an Response object.
We can parse the response using the built in json method like that:

```python
print(result.json())
```
